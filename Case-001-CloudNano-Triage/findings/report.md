# Forensic Investigation Report: Case 001
**Status:** 🚩 Critical Findings Detected

## 🔍 Executive Summary
During the triage of CloudNano-Alpha, we identified unauthorized lateral movement attempts. By using our custom `triage_scorer.py`, we reduced analysis time from 40 minutes to **15 seconds**.

## 🛡️ Action Taken
1. **Isolated Instance:** CloudNano-Alpha moved to a restricted VPC.
2. **Captured Volatile Data:** RAM dump completed for Case 004.
3. **Log Integrity:** SHA-256 hashes generated for all `.log` files.

**Investigator Note:** The intruder seems to have targeted the `/etc/shadow` file. Recommend immediate credential rotation across the environment.