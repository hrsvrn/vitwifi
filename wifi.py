import requests
import json
import time

def main():
    # Load credentials from config
    try:
        with open("config.json", "r") as f:
            payload = json.load(f)
    except FileNotFoundError:
        print("Error: Config not found. Please run setup.py first.")
        return

    url = "http://phc.prontonetworks.com/cgi-bin/authlogin"
    
    print(f"Starting login monitoring for user: {payload['userId']}")
    
    while True:
        try:
            # Direct POST request bypasses the front-end dialog box
            response = requests.post(url, data=payload, timeout=10)
            res_text = response.text.lower()
            
            if "congratulations" in res_text or "already" in res_text:
                print(f"Status: Connected as {payload['userId']}.")
                # Break the loop if you only want to login once, 
                # or keep it running to auto-reconnect if you get logged out.
                break
            else:
                print("Status: Login failed. Retrying in 10 seconds...")
                
        except requests.exceptions.RequestException:
            print("Status: Network unreachable. Check WiFi connection. Retrying...")
        
        time.sleep(10)

if __name__ == "__main__":
    main()
