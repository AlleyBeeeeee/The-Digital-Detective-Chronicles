# Case 001: CloudNano Triage 🔍

## 🔎 Investigation Brief
**Subject:** Cloud-Native Instance "CloudNano-Alpha"
**Incident Type:** Potential Unauthorized Access / Lateral Movement
**Date:** 2026-04

## 🛠️ The Mission
This case focuses on **Triage Automation**. In a high-pressure incident, we don't have time to copy the entire hard drive. This folder documents my process for:
* Collecting **Volatile Evidence** (RAM and Network connections).
* Performing **Risk-Based Prioritization** to identify which systems need immediate isolation.
* Analyzing **Auth Logs** for brute-force patterns.

## 📁 Evidence Inventory
| Item ID | Description | Format | Status |
| :--- | :--- | :--- | :--- |
| E001 | System Auth Logs | .log | Collected |
| E002 | Volatile RAM Dump | .mem | Metadata Only |
| E003 | Network Traffic (Port 22/80) | .pcap | Metadata Only |
