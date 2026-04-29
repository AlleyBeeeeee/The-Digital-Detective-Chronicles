# Case 001: CloudNano Triage 🚩🚀

> **Investigation Log:** *"In a breach, the first 15 minutes are the most expensive. If the server is on fire, I’m not looking for a manual; I'm looking for the source."*

---

## 🎯 Objective
The goal of this case was to establish a **Rapid Triage Framework**. We needed a way to instantly score system events so that an investigator can ignore the "smoke" and head straight for the "fire."

## 🧐 What’s Happening?
We are simulating a high-pressure triage of the **CloudNano-Alpha** instance. The system is generating a flood of events. Without a scoring system, a human analyst might miss a critical "Mass File Deletion" event while looking at a "Failed sudo" attempt. 

This triage tool acts as a digital first responder, flagging critical threats for immediate isolation.

## 🛠️ How It’s Happening (The Technical Breakdown)
The investigation utilizes a **Python-based Risk Scorer** to process volatile data:
* **Severity Scoring:** Each event is assigned a numeric value (1–10). The script filters for anything > 7, ensuring that only high-priority alerts break the "noise" threshold.
* **Automated Alerting:** Instead of a static list, the script generates a live `[!] HIGH RISK ALERT` feed, mimicking a real-time Security Operations Center (SOC) dashboard.
* **Forensic Soundness:** Every action taken during triage is documented in the findings report to maintain the chain of custody for the "Digital Detective" master ledger.

## 💡 Why We Use This
Triage is the "ER" of Cybersecurity. We use this method because:
1. **Speed to Triage (MTTT):** We reduced the time to identify critical threats from 40 minutes of manual scrolling to **sub-second** automated detection.
2. **Resource Management:** By automating the "low-level" alerts, we free up the investigator to focus on complex lateral movement and containment.
3. **Accuracy:** Under pressure, humans miss things. Scripts don't.

---

## 📂 Artifacts
* `scripts/triage_scorer.py`: The rapid triage engine.
* `findings/report.md`: The formal executive summary of the incident.
* `evidence/`: (Reserved) Snapshots of volatile memory and hash logs.

---
**Status:** ✅ Case Resolved | **Findings:** Instance CloudNano-Alpha isolated and secured.