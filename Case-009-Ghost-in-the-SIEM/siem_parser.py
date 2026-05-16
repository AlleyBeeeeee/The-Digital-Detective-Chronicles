import re

# Define the log file destination to parse
LOG_FILE = "centralized_logs.txt"

# Regex pattern to isolate IP address, username, and the action status
# Breakdown: Look for Failed/Accepted keywords, capture user, capture the source IP
log_pattern = re.compile(r"(Accepted|Failed) password for (?:invalid user )?(\w+) from ([\d\.]+\b)")
sudo_pattern = re.compile(r"COMMAND=(.*)")

print("🕵️‍♀️ [ALLEYBEE SIEM ENGINE ACTIVATED] Triage Processing Started...\n")

with open(LOG_FILE, "r") as file:
    for line in file:
        # Check for authentication traffic
        auth_match = log_pattern.search(line)
        if auth_match:
            status = auth_match.group(1)   # Accepted or Failed
            username = auth_match.group(2) # The account targeted
            ip_address = auth_match.group(3) # Attacker IP
            
            if status == "Failed":
                print(#🟢 Low Threat Notice
                    f"[⚠️ AUTH FAILED] Account: {username} | Source IP: {ip_address}"
                )
            elif status == "Accepted" and ip_address != "192.168.1.50": # Flag non-local IPs
                print(
                    f"\n🚨 [CRITICAL ALERT: BREACH CONFIRMED]\n"
                    f"-> Unauthorized access detected to account [{username}] from External IP [{ip_address}]!\n"
                )
                
        # Check for anti-forensic log tampering commands
        if "rm -rf" in line:
            sudo_match = sudo_pattern.search(line)
            if sudo_match:
                print(
                    f"🔥 [ANTI-FORENSICS DETECTED]\n"
                    f"-> Compromised user executed log destruction command: {sudo_match.group(1)}\n"
                )

print("🔬 Triage Completed. Evidence isolated.")
