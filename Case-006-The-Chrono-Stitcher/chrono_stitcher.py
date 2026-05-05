import json    # provides tools for parsing json data
import csv     # provides tools for reading comma-separated values
from datetime import datetime  # handles date and time conversions

class ChronoStitcher:
    def __init__(self):
        # initializes an empty list to store normalized event dictionaries
        self.master_timeline = []

    def normalize_time(self, time_str, fmt):
        # converts a string into a python datetime object based on a format string
        return datetime.strptime(time_str, fmt)

    def parse_auth_logs(self, filepath):
        # opens the text-based auth log for reading
        with open(filepath, 'r') as f:
            for line in f:
                clean_line = line.strip()
                # skips empty lines or comment lines starting with #
                if not clean_line or clean_line.startswith('#'):
                    continue
                
                parts = clean_line.split(' ', 3)
                timestamp_str = f"2026 {' '.join(parts[:3])}"
                dt = self.normalize_time(timestamp_str, "%Y %b %d %H:%M:%S")
                
                self.master_timeline.append({
                    "timestamp": dt,
                    "source": "AUTH_LOG",
                    "event": parts[3].strip()
                })

    def parse_file_activity(self, filepath):
        # opens the csv file for reading
        with open(filepath, 'r') as f:
            # filters out comment lines before handing data to the csv reader
            filtered_file = (line for line in f if not line.strip().startswith('#'))
            reader = csv.DictReader(filtered_file)
            for row in reader:
                dt = self.normalize_time(row['timestamp'], "%Y-%m-%d %H:%M:%S")
                self.master_timeline.append({
                    "timestamp": dt,
                    "source": "FILE_SYSTEM",
                    "event": f"{row['action']} -> {row['filename']}"
                })

    def parse_network_traffic(self, filepath):
        # loads the json data and handles potential comments if using a list
        with open(filepath, 'r') as f:
            data = json.load(f)
            for entry in data:
                # converts json timestamp to datetime object
                dt = self.normalize_time(entry['ts'], "%Y-%m-%dT%H:%M:%S")
                self.master_timeline.append({
                    "timestamp": dt,
                    "source": "NETWORK",
                    "event": f"outbound transfer to {entry['dest']} ({entry['size']})"
                })

    def display_timeline(self):
        # sorts the list of dictionaries chronologically by timestamp
        self.master_timeline.sort(key=lambda x: x['timestamp'])
        
        # prints the header for the forensic report
        print(f"\n{'timestamp':<20} | {'source':<12} | {'event'}")
        print("-" * 75)
        
        # outputs the final sorted timeline
        for entry in self.master_timeline:
            ts_str = entry['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{ts_str:<20} | {entry['source']:<12} | {entry['event']}")

# --- execution section ---
if __name__ == "__main__":
    stitcher = ChronoStitcher()
    try:
        stitcher.parse_auth_logs('auth_logs.txt')
        stitcher.parse_file_activity('file_activity.csv')
        stitcher.parse_network_traffic('network_traffic.json')
        stitcher.display_timeline()
    except Exception as e:
        print(f"error encountered: {e}")