import requests
import os

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL")  # store in .env or shell

def send_slack_alert(alert, match_type):
    message = f"⚠️ {match_type} detected!\nUser: {alert['user']} | IP: {alert['ip']} | Location: {alert['location']}"
    payload = {"text": message}
    requests.post(SLACK_WEBHOOK, json=payload)
