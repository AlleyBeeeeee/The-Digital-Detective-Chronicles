from scapy.all import rdpcap, TCP, Raw

# Load the capture we just created
packets = rdpcap('evidence.pcap')

print("🕵️‍♀️ Analyzing traffic streams...")

for pkt in packets:
    # Only look at packets that have a data payload (Raw)
    if pkt.haslayer(Raw):
        # Reach into the packet and pull out the load
        # .decode() turns it from 'bytes' into a string
        message = pkt[Raw].load.decode('utf-8')
        
        print(f"\n[!] ALERT: EXFILTRATION DETECTED")
        print(f"MESSAGE FOUND: {message}")