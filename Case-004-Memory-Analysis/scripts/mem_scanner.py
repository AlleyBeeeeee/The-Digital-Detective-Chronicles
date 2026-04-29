from pathlib import Path

def scan_memory_dump(dump_path):
    print("🧠 [MEMORY ANALYSIS INITIALIZED]")
    print(f"🔍 Scanning RAM Snapshot: {dump_path.name}\n" + "-"*40)

    # A list of names that 'Bad Programs' often use to hide
    SUSPICIOUS_NAMES = ["temp_malware.exe", "hidden_rat.py", "miner.sh", "cmd_bypass.exe"]
    
    found_threats = 0

    try:
        print("--- Currently scanning the memory dump... ---")
        with open(dump_path, 'r') as file:
            for line in file:
                # We are looking for any line that contains our suspicious names
                for threat in SUSPICIOUS_NAMES:
                    if threat in line:
                        print(f"🚨 [CRITICAL]: Found {threat} running in memory!")
                        found_threats += 1
        
        if found_threats == 0:
            print("✅ Memory appears clean. No known malicious processes detected.")
        else:
            print(f"\n📊 Scan Complete: {found_threats} memory threats identified.")

    except FileNotFoundError:
        print("❌ Error: Memory dump file not found.")

if __name__ == "__main__":
    base = Path(__file__).parent.parent
    # We'll point this to a mock memory file
    dump_file = base / "data" / "mem_dump.log"
    scan_memory_dump(dump_file)