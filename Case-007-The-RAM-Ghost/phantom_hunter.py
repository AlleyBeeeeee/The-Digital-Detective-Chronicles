import re

# Step 1: Read the evidence
with open('memory_report.txt', 'r') as f:
    lines = f.readlines()

ghost_pid = None

# Step 2: The First Pass - Finding the Ghost
# Say it: "I'm hunting for the PID of the unnamed process."
for line in lines:
    if "<unknown>" in line:
        # Use regex to grab the number (PID) from the line
        match = re.search(r'\s+(\d+)\s+', line)
        if match:
            ghost_pid = match.group(1)
            print(f"🎯 GHOST DETECTED! Suspicious PID found: {ghost_pid}")

# Step 3: The Second Pass - Connecting to the Network
# Say it: "Now I'm checking if this Ghost PID has an active network connection."
if ghost_pid:
    for line in lines:
        # Look for a line that starts with our ghost_pid in the network section
        if line.startswith(ghost_pid):
            # Grab the remote IP (the third column)
            parts = line.split()
            remote_ip = parts[2]
            print(f"🚩 ALARM: Ghost PID {ghost_pid} is communicating with {remote_ip}")
            print("🛑 RECOMMENDATION: Block this IP on the firewall immediately.")
else:
    print("✅ No hidden processes detected in this memory dump.")