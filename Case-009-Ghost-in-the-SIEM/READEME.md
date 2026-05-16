<div align="center">

# Case 009: Ghost in the SIEM
**Automating Log Correlation & Catching Anti-Forensic Tampering**

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeW9zOHQxaGthOTY4Y29ka3Jod3IzNHA1c3oxY3R5MDNlZDJpdDIzNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/42wQXwITfQbDGKqUP7/giphy.gif" width="300" alt="Anime Detective Glasses Flash Gif">

### *An adversary can manipulate host logs, but they can't change the laws of data ingestion.*

---
`INCIDENT_TYPE: Host Compromise` • `THREAT_LEVEL: Critical` • `STATUS: Closed & Remediated`
---

</div>

---

## 🎯 The Mission Brief
An adversary gained unauthorized access to a core Linux production environment, executed privileged operations, and maliciously purged the host authorization logs (`/var/log/auth.log`) to wipe their digital footprints and blend into the shadows. 

Because local evidence was destroyed, standard host-based triage turns up blank. **The Solution:** Build a lightweight, custom SIEM parser in Python to analyze the infrastructure's centralized log backup data lake, reconstruct the attack timeline, and expose the intruder.

---

## 🛠️ The Tech Arsenal
* **Languages:** Python 3.x (`re` text-parsing engine)
* **Concepts:** Regular Expressions (Regex), Tokenization, Log Aggregation, Centralized Ingestion Pipelines
* **Environment:** Isolated Python Virtual Environment (`venv`), Ubuntu Linux

---

## 🔬 Forensic Evidence & Output
By executing `siem_parser.py` inside our clean room laboratory environment, we tokenized the unstructured data stream and extracted the critical Indicators of Compromise (IoCs):

```text
🕵️‍♀️ [ALLEYBEE SIEM ENGINE ACTIVATED] Triage Processing Started...

[⚠️ AUTH FAILED] Account: admin | Source IP: 203.0.113.5
[⚠️ AUTH FAILED] Account: admin | Source IP: 203.0.113.5
[⚠️ AUTH FAILED] Account: admin | Source IP: 203.0.113.5

🚨 [CRITICAL ALERT: BREACH CONFIRMED]
-> Unauthorized access detected to account [admin] from External IP [203.0.113.5]!

🔥 [ANTI-FORENSICS DETECTED]
-> Compromised user executed log destruction command: /usr/bin/rm -rf /var/log/auth.log

🔬 Triage Completed. Evidence isolated.
