# Case 008: The Packet Whisperer 📡
### *Deep Packet Inspection & Network Forensic Integrity*

<div align="center">
  <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWgxemxmMjZkMHNldjcwM2c4czdsc3Rjd2UwM2VwcXR6dGFndHJ4MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7bufkPz3LRof205G/giphy.gif" width="300" alt="Packet Whisperer Gif">
</div>

## 🚩 The Scenario: The Leak in the Wire
A workstation was suspected of "leaking" project data to an external C2 (Command & Control) server. While the local logs were suspiciously "clean," I knew the network is the ultimate truth-teller. Even the most sophisticated malware has to talk to its boss eventually. I stepped in to perform **Deep Packet Inspection (DPI)** because, while an attacker can lie to the OS, they can't lie to the wire.

## 🎯 Investigation Objectives
1. **Maintain Forensic Integrity:** Isolate the tools using a Python Virtual Environment (`venv`). In this lab, we don't contaminate the "crime scene" (or the system Python).
2. **Simulate the Breach:** Craft raw network traffic to create a controlled forensic snapshot (PCAP).
3. **Analyze the Payload:** Use **Scapy** to bypass protocol headers and reconstruct the stolen data stream.

## 🛠️ The Technical Toolkit
* **Scapy:** The "Surgical Kit" for networking. Unlike standard libraries that only see the surface, Scapy lets me manipulate the **TCP/IP stack** at every level. 
* **Python 3 (venv):** Using a virtual environment was a professional necessity. It allowed me to bypass Linux system restrictions and ensure my forensic tools remained in their own "sandbox."
* **PCAP (Packet Capture):** The industry-standard "digital fingerprint" of network traffic.

## 🕵️‍♀️ The Investigation Flow
### **1. The Exfiltration (The "Crime")**
In `evidence_generator.py`, I didn't just write a string; I **encapsulated** it. I built a packet from the ground up: IP layer, TCP layer, and a `Raw` payload injected with the "Confidential" project data.

### **2. The Whisperer (The "Catch")**
My `packet_whisperer.py` script performed a three-step dissection:
* **Load:** Reconstructed the binary data into readable objects.
* **Filter:** Ignored the "handshake" noise and targeted the `Raw` data layer. 
* **Decode:** Translated the binary back into the plaintext evidence: `SECRET_PROJECT_NEPTUNE_DATA_EXFILTRATED`.

## 📝 Detective's Notes
* **Caffeine Level:** Peak efficiency. 5:00 AM is the "Golden Hour" for packet analysis.
* **Pro-Tip:** If the Host logs look too perfect, they probably are. Trust the wire, not the user.
* **Environment Logic:** Fighting the `externally-managed-environment` error is just another day in the life of a Linux admin. The `venv` isn't just a fix; it's a best practice.

## 🚀 Key Learning: The Wire Doesn't Lie
This case proved that **Defense-in-Depth** must include network forensics. An attacker can wipe their tracks on a hard drive or vanish from RAM on reboot, but they cannot recall the packets that have already crossed the router. 

---
**Status:** `Evidence Recovered` | **Motive:** `Exfiltration Confirmed` | **Case:** `Closed`