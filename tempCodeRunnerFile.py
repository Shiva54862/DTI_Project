from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Store generated OTPs and associated phone numbers
otp_database = {}

# Generate a 6-digit OTP
def generate_otp():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

# Route for sending OTP
@app.route('/send_otp', methods=['GET', 'POST'])
def send_otp():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        otp = generate_otp()
        # Send OTP to the user's phone number (you need to implement this part)
        # For simplicity, we'll just print the OTP here
        print(f"OTP sent to {phone_number}: {otp}")
        otp_database[phone_number] = otp
        return "OTP sent successfully!"
    return render_template('send_otp.html')

# Route for verifying OTP
@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        user_otp = request.form.get('otp')
        if phone_number in otp_database and otp_database[phone_number] == user_otp:
            return "OTP verified successfully!"
        else:
            return "Invalid OTP. Please try again."
    return render_template('verify_otp.html')

if __name__ == '__main__':
    app.run(debug=True)
