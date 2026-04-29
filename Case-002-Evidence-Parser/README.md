# Case 002: Digital Evidence Parser 🔍🐍

> **Investigation Log:** *"If you're reading 10,000 lines of logs by hand, you're not an investigator; you're a human highlighter. Let's automate this."*

---

## 🎯 Objective
The goal of this mission was to build a robust, repeatable process for extracting **Indicators of Compromise (IOCs)** from raw system authentication logs. We want to move from "messy data" to "actionable intelligence" in seconds.

## 🧐 What’s Happening?
We are simulating a scenario where a server is under a brute-force attack. The system logs (`auth_audit.log`) are cluttered with standard system noise, successful logins, and—crucially—hundreds of failed password attempts from unauthorized IP addresses. 

This parser cuts through the noise to find the specific "fingerprints" of the attacker.

## 🛠️ How It’s Happening (The Technical Breakdown)
The tool utilizes **Python 3** and the **Regex (re)** library to perform the following:
* **Pattern Matching:** We use the regular expression `(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})` to identify IPv4 addresses within strings of text.
* **Conditional Filtering:** The script scans each line for the specific string "Failed password"—the signature of a brute-force attempt.
* **Path Resilience:** Using `pathlib`, the script is designed to find the evidence files regardless of which directory the investigator is running the script from.

## 💡 Why We Use This
In a real-world **Incident Response (IR)** scenario, time is the only currency that matters.
1. **Efficiency:** A script doesn't get tired or skip lines after 5 hours of work.
2. **Precision:** Regex ensures we grab the exact IP address without human error or typos.
3. **Scalability:** This same logic can be expanded to parse millions of lines across entire server clusters, creating a timeline of an attack that would be impossible to build manually.

---

## 📂 Artifacts
* `src/parser.py`: The Python "Engine" of the investigation.
* `samples/auth_audit.log`: The raw evidence (Log entries).
* `docs/`: Technical documentation and forensic notes.

---
**Status:** ✅ Case Resolved | **Findings:** Brute-force IOCs identified and logged.