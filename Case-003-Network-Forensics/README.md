# Case 003: Network Forensics (The Beacon Hunter) 📡🕵️‍♀️

> **Investigation Log:** *"The network doesn't lie. Users delete logs, but the packets always leave a trail in the dirt. If a computer is 'whispering' to the outside world, I'm going to hear it."*

---

## 🎯 Objective
The goal of this case was to identify **Command & Control (C2) Beaconing**. We wanted to catch malware that has already bypassed the firewall and is "calling home" to a hacker for instructions.

## 🧐 What is Beaconing? (The "Why")
Imagine a burglar has snuck into a building. They don't want to carry a heavy safe out immediately. Instead, they stay hidden and "tap" on a window every 5 minutes to tell their boss outside, *"I'm still here, what's next?"*

In cybersecurity, this "tap" is a small, regular network signal. While it's quiet, it's highly **repetitive**. We use this case to find that heartbeat.



## 🛠️ What We Did (The Methodology)
We built a Python-based **Traffic Analyzer** that performs a "Frequency Audit" on network metadata.
1. **Data Ingestion:** We processed `traffic_capture.csv` (a mock export from a tool like Wireshark).
2. **Frequency Analysis:** The script creates a "tally" for every unique connection (Source IP + Destination IP).
3. **Threshold Alerting:** If the script identifies the **exact same connection 3 times**, it flags it as a potential beacon.
4. **Forensic Logging:** Instead of just showing it on the screen, the script automatically writes the evidence to `logs/findings.txt` to maintain the **Chain of Custody**.

## 💻 How It Works (The Code Logic)
* **The Dictionary Tally:** We used a Python Dictionary (`{}`) to act as a "whiteboard" to keep track of every connection's count.
* **The File Handler:** We used a nested `with open()` block. This allows the script to **read** the evidence and **write** the findings at the same exact time.
* **Pathlib Integration:** We used the `pathlib` library to ensure the script can find its way home (to the data files) regardless of which folder it's launched from.

## 💡 Why This Matters
In a real Security Operations Center (SOC):
* **Accuracy:** You can't manually watch millions of packets. Automation ensures you never miss a "heartbeat."
* **Evidence Integrity:** By logging findings to a file, we create a permanent record that can be used in a legal or corporate investigation.

---

## 📂 Artifacts
* `scripts/network_hunter.py`: The "Brain" (The logic engine).
* `data/traffic_capture.csv`: The "Crime Scene" (The raw evidence).
* `logs/findings.txt`: The "Evidence Locker" (The recorded findings).

---
**Status:** ✅ Case Resolved | **Findings:** C2 Beaconing identified to IP 45.33.22.11.