# Case 004: Memory Analysis (The Ghost Hunter) 🧠🔍

> **Investigation Log:** *"The hard drive tells me what happened in the past. The RAM tells me what is happening RIGHT NOW. In forensics, the memory is the only place where 'fileless' malware has nowhere to hide."*

---

## 🎯 Objective
To identify **Fileless Malware** and unauthorized background processes by scanning system memory (RAM) snapshots for known malicious signatures.

## 🧐 What is Memory Analysis? (The "Why")
Advanced attackers often use "Fileless" techniques—malware that lives entirely in the computer's memory and never saves a file to the hard drive. 
* **The Problem:** Traditional antivirus scans the hard drive and misses these "ghosts."
* **The Solution:** We capture a "Memory Dump" (a snapshot of the brain) and scan it for active threats.



## 🛠️ What We Did (The Methodology)
1. **Evidence Creation:** We generated a mock memory dump (`mem_dump.log`) simulating a list of active system processes and their Process IDs (PIDs).
2. **Signature-Based Scanning:** We built a Python tool (`mem_scanner.py`) that performs a real-time audit of every running process.
3. **Threshold Alerting:** The script cross-references every active process against a "Blacklist" of known malicious signatures (e.g., miners and RATs).

## 💻 Python Script Breakdown
* **`pathlib.Path`**: Used to ensure the script can find the evidence folder regardless of the operating system.
* **`for line in file`**: An efficient way to scan large memory files without crashing the system.
* **Conditional Matching**: We used the `if threat in line` logic to trigger immediate alerts only when a high-risk signature is identified.

## 💡 Why This Matters
In a real Security Operations Center (SOC), memory analysis is critical because:
* **It catches "Live" threats:** You can see an attacker currently typing commands or stealing data.
* **It reveals encryption keys:** Often, the password to an encrypted drive is sitting right there in the RAM in plain text.
* **It finds hidden PIDs:** Hackers try to hide processes from the Task Manager, but they cannot hide from a raw memory scan.

---

## 📂 Artifacts
* `scripts/mem_scanner.py`: The RAM interrogation engine.
* `data/mem_dump.log`: The captured "Volatile" evidence file.

---
**Status:** ✅ Case Resolved | **Findings:** Identified 'temp_malware.exe' and 'miner.sh' active in system memory.