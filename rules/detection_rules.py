def apply_rules(alert):
    findings = []
    if alert.get("status") == "FAILED" and alert.get("location") != "USA":
        findings.append("Geo-IP anomaly")
    if alert.get("user") == "admin" and alert.get("status") == "FAILED":
        findings.append("Brute-force pattern")
    return findings
