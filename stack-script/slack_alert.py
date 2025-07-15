import sys
import json
import requests

WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

def main():
    message = sys.stdin.read()
    payload = {"text": f"🔐 *Splunk Alert*:\n```{message}```"}
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"Error sending Slack alert: {e}")

if __name__ == "__main__":
    main()
