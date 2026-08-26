import os
from flask import Flask, jsonify, send_from_directory, request
from sarvamai import SarvamAI
from dotenv import load_dotenv 

import razorpay
from flask import jsonify, request

load_dotenv()

app = Flask(__name__, static_folder='.')

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

rzp_client = razorpay.Client(auth=(os.getenv("TEST_KEY_ID"), os.getenv("TEST_KEY_SECRET")))

@app.route('/api/diagnose_and_recover', methods=['POST'])
def diagnose_recovery():
    payload = request.json
    user_phone = payload.get("contact")

    try:
        # Step 1: Fetch the last 50 transactions from Razorpay
        recent_payments = rzp_client.payment.all({"count": 50})
        
        # Step 2: Search for the most recent failed payment matching the phone number
        failed_txn = None
        for payment in recent_payments['items']:
            # Razorpay sometimes stores numbers with or without the country code
            if payment.get('contact') == user_phone or payment.get('contact') == f"+91{user_phone}":
                if payment.get('status') == 'failed':
                    failed_txn = payment
                    break # Stop at the first (most recent) match
        
        if not failed_txn:
            return jsonify({"error": f"Koi failed payment nahi mila is number ke liye: {user_phone}"})

        # Step 3: Extract the error details
        txn_id = failed_txn['id']
        failure_reason = failed_txn.get("error_description") or failed_txn.get("error_reason") or "Bank gateway timeout"
        txn_amount = failed_txn['amount'] # Amount is in paise

        # Step 4: Generate SMS-enabled Recovery Action
        recovery_link = rzp_client.payment_link.create({
            "amount": txn_amount,
            "currency": "INR",
            "description": f"Recovery for failed transaction {txn_id}",
            "customer": {"contact": user_phone},
            "notify": {"sms": True}
        })

        return jsonify({
            "status": "failed",
            "payment_id": txn_id,
            "error_reason": failure_reason,
            "recovery_url": recovery_link.get("short_url"),
            "amount_in_rupees": txn_amount / 100
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/config', methods=['GET'])
def get_config():
    return jsonify({
        "chatflowId": os.getenv("FLOWISE_CHATFLOW_ID", "YOUR_DEFAULT_CHATFLOW_ID"),
        "apiHost": os.getenv("FLOWISE_API_HOST", "https://cloud.flowiseai.com")
    })

@app.route('/v1/audio/transcriptions', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    audio_file = request.files['file']
    # Safely grab the actual extension provided by the browser (usually .webm)
    filename = audio_file.filename if audio_file.filename else "temp_audio.webm"
    temp_path = filename
    
    print(f"--- [START] Received Audio File: {filename} ---")
    audio_file.save(temp_path)
    
    try:
        print("Sending audio to Sarvam AI for transcription...")
        with open(temp_path, "rb") as f:
            response = client.speech_to_text.transcribe(
                file=f,
                model="saaras:v3",
                mode="transcribe"
            )
        
        print("Transcription successful!")
        transcript_text = getattr(response, 'transcript', None) or response.get('transcript', '')
        print(f"Text Generated: {transcript_text}")
        return jsonify({"text": transcript_text})
        
    except Exception as e:
        # If Sarvam crashes, it will print in red in your terminal
        print(f"--- [CRITICAL ERROR]: {str(e)} ---") 
        return jsonify({"error": str(e)}), 500
        
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)