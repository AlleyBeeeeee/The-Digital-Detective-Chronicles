import re
from pathlib import Path

# The "Clue": This Regex pattern finds IP addresses
IP_PATTERN = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

def forensic_parse(log_path):
    print("🕵️‍♀️ [LOG ANALYSIS INITIALIZED]")
    print(f"📂 Source: {log_path}\n" + "-"*40)

    try:
        with open(log_path, 'r') as file:
            findings_count = 0
            for line in file:
                if "Failed password" in line:
                    ip = re.search(IP_PATTERN, line)
                    if ip:
                        findings_count += 1
                        print(f"🚩 [ALERT] Brute-force attempt detected from: {ip.group(0)}")
            
            if findings_count == 0:
                print("✅ No suspicious patterns found. System appears secure.")
            else:
                print(f"\n📊 Analysis Complete: {findings_count} IOCs identified.")

    except FileNotFoundError:
        print(f"❌ Error: Could not find file at {log_path}")
        print("💡 Hint: Make sure you are running the script from the Case-002-Evidence-Parser folder!")

if __name__ == "__main__":
    # This magic line finds the 'samples' folder regardless of where you run the script from
    base_path = Path(__file__).parent.parent
    log_file = base_path / "samples" / "auth_audit.log"
    
    forensic_parse(log_file)