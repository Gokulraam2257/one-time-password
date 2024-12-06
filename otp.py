import secrets

import requests

url = 'https://graph.facebook.com/v16.0/104875019237687/messages'
    
h = {"Content-Type": "application/json",                         
     "Authorization": "Bearer EAAIlfUAt6BgBOZB1r8LWXmUkijsNIZC9l97OudJaLLPSXOM0OV6pqdL6L8ZCvJZC7pXbqNotV2utXbPWLGVnXZASB1nWOdNvkacBa1wdYNsO9w9oQwPs2giT1UDfh3ZABzb8BgXUyGN6tHSzoz6hzuZAagZCFZCQ7MckRHlZBpD83MSRzZCAZC9mXZCSWLSC6lAlN6XTJhEBDwXRBswDI5cFR1ZClwIykWzxMlg6EEqcxMCgYGojYZD"}


# Function to generate a random secret key
def generate_secret_key():
	return secrets.token_hex(16) # 16 bytes (32 hex characters)

# Function to generate a One Time Password (OTP) using the secret key
def generate_otp(secret_key, length=6):
	# Defining the characters allowed in the OTP
	allowed_characters = "0123456789"

	# Generating a random OTP using the secret key and allowed characters
	otp = ''.join(secrets.choice(allowed_characters) for _ in range(length))
	a = f"Your One-Time Password for verification is {otp}"
	d = {
	    "messaging_product": "whatsapp",
	    "to": "919489055173",
	    "type": "text",
	    "text": {
	    "preview_url": True,
	        "body": a,
	        
	    }
	}
	post =requests.post(url,json=d,headers=h)
	s = post.status_code
	js = post.json()
	print(s,js)
	return otp

# Example usage
if __name__ == "__main__":
	# Generate a random secret key (this should be kept secure)
	secret_key = generate_secret_key()

	# Simulate sending the OTP to the user
	otp = generate_otp(secret_key)

	# Simulating user input for OTP verification
	user_input = input("Please enter the received OTP: ")

	# Verify the OTP entered by the user
	if user_input == otp:
		print("OTP verification successful. Access granted!")
	else:
		print("OTP verification failed. Access denied!")
