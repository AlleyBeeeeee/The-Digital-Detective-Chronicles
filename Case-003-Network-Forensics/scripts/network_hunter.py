import csv
from pathlib import Path

def analyze_traffic(data_path, report_path):
    print("📡 [NETWORK HUNTER STARTING...]")
    connection_tally = {}
    
    try:
        # Step 1: Open the traffic data
        with open(data_path, mode='r') as file:
            reader = csv.DictReader(file)
            
            # Step 2: Open (or create) our findings file to write evidence
            with open(report_path, mode='w') as report:
                report.write("FORENSIC FINDINGS: CASE 003\n" + "="*30 + "\n")
                
                for row in reader:
                    pair = f"{row['source_ip']} -> {row['dest_ip']}"
                    connection_tally[pair] = connection_tally.get(pair, 0) + 1
                    
                    # Step 3: Logic - If we see it 3 times, log it as evidence
                    if connection_tally[pair] == 3:
                        msg = f"🚩 BEACON DETECTED: {pair} at {row['timestamp']}\n"
                        print(msg.strip())
                        report.write(msg) # This saves it to the file forever
        
        print("✅ Scan complete. Findings saved to logs/findings.txt")
    except FileNotFoundError:
        print("❌ Error: File not found.")

if __name__ == "__main__":
    base = Path(__file__).parent.parent
    traffic = base / "data" / "traffic_capture.csv"
    # We are sending the results to a new folder called 'logs'
    report = base / "logs" / "findings.txt"
    
    analyze_traffic(traffic, report)