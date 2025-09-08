# main.py
import json
from rules.detection_rules import apply_rules
from responders.slack_alert import send_slack_alert

def load_alerts(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def main():
    alerts = load_alerts('alerts/sample_alerts.json')
    for alert in alerts:
        matches = apply_rules(alert)
        for match in matches:
            print(f"[+] Detected: {match}")
            send_slack_alert(alert, match)

if __name__ == '__main__':
    main()