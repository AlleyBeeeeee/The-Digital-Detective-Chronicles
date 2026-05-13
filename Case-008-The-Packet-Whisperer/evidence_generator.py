from scapy.all import IP, TCP, wrpcap, Raw

# The 'Envelope'
packet_list = []
target_ip = "45.33.22.11" # The Hacker's Server
local_ip = "192.168.1.5"   # The Compromised Host

# The 'Secret Letter' inside
payload = "SECRET_PROJECT_NEPTUNE_DATA_EXFILTRATED"

# Stacking the layers: IP -> TCP -> Data
print(f"🛰️ Generating malicious packet for {target_ip}...")
pkt = IP(src=local_ip, dst=target_ip)/TCP(sport=54321, dport=4444)/Raw(load=payload)

packet_list.append(pkt)

# Saving the capture
wrpcap('evidence.pcap', packet_list)
print("💾 Evidence secured: evidence.pcap is ready for analysis.")