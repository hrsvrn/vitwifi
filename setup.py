import json
import subprocess
import sys

def run_setup():
    print("--- WiFi Login One-Time Setup ---")
    
    # Install dependencies
    
    # Get User Credentials
    user_id = input("Enter your WiFi Username: ")
    password = input("Enter your WiFi Password: ")
    
    config = {
        "userId": user_id,
        "password": password,
        "serviceName": "ProntoAuthentication",
        "Submit22": "Login"
    }
    
    # Save to local config file
    with open("config.json", "w") as f:
        json.dump(config, f)
    
    print("\nSetup Complete. 'config.json' created.")
    print("You can now run your login script.")

if __name__ == "__main__":
    run_setup()
