# Case 007: The RAM Ghost 👻
### *Volatile Memory Analysis & Network Correlation*

<div align="center">
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTk5Njh5ZGNheDRzMHV2bndiYm5sMjl3bWdoODFrMDJzc29kNzd1eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/k3fTc8vOmbZRU8BCXW/giphy.gif" width="250" alt="Ghost Search Gif">
</div>

## 🚩 The Scenario: A Digital Exorcism
The SOC reported a "Poltergeist" on a workstation—bandwidth was disappearing, but the Task Manager showed nothing but "healthy" processes. The intruder wasn't just hiding; they were **fileless**. Traditional disk-based scans returned clean, suggesting the presence of malware residing strictly in the system's volatile memory (RAM). I was called in to perform a digital exorcism using **Volatility 3**.

## 🎯 Investigation Objectives
1. **Identify Anomalies:** Locate processes in the memory dump with missing or suspicious names.
2. **Determine Persistence:** Map the Parent Process ID (PPID) to understand the execution chain.
3. **Correlate Network Traffic:** Link suspicious Process IDs (PIDs) to active network sockets.

## 🛠️ The Detective's Kit
* **Volatility 3:** The "X-Ray" used for parsing raw memory structures.
* **Python 3:** The automation engine used to "bridge" disparate artifacts.
* **Regex (`re`):** My digital magnet for pulling PIDs and IPs out of the noise.

## 📂 Forensic Artifacts
* `memory_report.txt`: A simulated Volatility 3 output containing the Process List and Netstat tables.
* `phantom_hunter.py`: A custom-built triage script designed to connect the dots between the "brain" (RAM) and the "wire" (Network).

## 🕵️‍♀️ The Investigation Flow
1. **The Scan:** Analyzing the process list uncovered a process labeled `<unknown>` (PID 9999). 
2. **The Pivot:** I executed `phantom_hunter.py` to perform a two-pass correlation.
3. **The Find:** The script successfully matched the "Ghost" PID 9999 to an established connection with **45.33.22.11** on port **1337**.

## 📝 Detective's Notes
* **Caffeine Level:** Dangerously low during initial triage, but stabilized by Step 2.
* **The Smoking Gun:** PID 9999. It had no name and a very suspicious habit of talking to an unidentified IP on port 1337. Classic "Elite Hacker" cliché, but effective.
* **Pro-Tip:** If the process list looks too clean, start digging for the "Unknown." Malware is like a toddler; if it's too quiet, it's definitely up to something.

## 🚀 Key Learning: Memory Doesn't Lie
This case highlights the power of volatile memory forensics. While an attacker can wipe logs or delete files from a hard drive, a process **must** exist in RAM to function. By automating the correlation between memory-resident processes and network traffic, I turned a "ghost story" into an actionable firewall block.

---
**Status:** `Exorcism Complete` | **Integrity:** `SHA-256 Verified` | **Case:** `Closed`