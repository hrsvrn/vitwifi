import requests
import time
import urllib3

print("Wifi login script running...")

userId = "uruserid"
password = "urpasswd"

url = "http://phc.prontonetworks.com/cgi-bin/authlogin"
data = {
    "userId": userId,
    "password": password,
    "serviceName": "ProntoAuthentication",
    "Submit22": "Login",
}


def main():
    logged_in = False
    already = False
    retries = 0
    while not logged_in:
        try:
            response = requests.post(url, data)
        except urllib3.exceptions.NewConnectionError:
            print("No internet access\nTry again...")
        break

    already = "already" in response.text.lower()
    logged_in = "congratulations" in response.text.lower() or already

    if logged_in and already:
        print(f"Already logged in as {userId}.")
    elif logged_in:
        print(f"Logged in successfully as {userId}")
    else:
        print("Failed to login. Trying again in 3s...")
        retries += 1
        time.sleep(3)


if __name__ == "__main__":
    main()
