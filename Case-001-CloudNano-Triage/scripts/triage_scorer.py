import os

# Simulated Forensic Artifacts
logs = [
    {"timestamp": "2026-04-28 10:01", "event": "Failed sudo attempt", "user": "intruder", "severity": 9},
    {"timestamp": "2026-04-28 10:05", "event": "SSH Login Success", "user": "abeee", "severity": 1},
    {"timestamp": "2026-04-28 10:15", "event": "Mass File Deletion", "user": "unknown", "severity": 10},
]

def analyze_risk(log_data):
    print("🕵️‍♀️ Starting CloudNano Triage Scorer...")
    high_risk_detected = False
    
    for entry in log_data:
        if entry['severity'] > 7:
            print(f"[!] HIGH RISK ALERT: {entry['event']} by {entry['user']} at {entry['timestamp']}")
            high_risk_detected = True
            
    if not high_risk_detected:
        print("[+] System looks clean. Coffee break time? ☕")
    else:
        print("[X] INVESTIGATION REQUIRED. Evidence locked.")

analyze_risk(logs)