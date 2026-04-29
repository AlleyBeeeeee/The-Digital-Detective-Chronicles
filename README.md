# Digital Data Chronicles 🛡️
**Master Forensic Case Files & IR Documentation**

This repository is a collection of technical investigations and automated solutions developed for Digital Forensics and Incident Response (DFIR). Each directory represents a standalone case or toolset.

## 📂 Active Case Files

### [Case 001: CloudNano Triage](./Case-001-CloudNano-Triage)
* **Objective:** Rapid risk-based prioritization of cloud-based artifacts.
* **Status:** Completed
* **Key Tech:** Python, Log Analysis

### [Case 002: Digital Evidence Parser](./Case-002-Evidence-Parser)
* **Objective:** Automation of repetitive log parsing to accelerate timeline creation.
* **Status:** In Development
* **Key Tech:** Python, Regex, JSON

### [Case 003: Network Forensics & Lateral Movement](./Case-003-Network-Forensics)
* **Objective:** Identifying unauthorized access and movement within a virtualized network.
* **Status:** Planned

---
*Created and maintained to bridge technical foundations with high-level IR strategy.*

### digital-data-chronicles/
├── .gitignore
├── README.md 
├── Case-001-CloudNano-Triage/
│   ├── evidence/           # Evidence metadata (not raw large files)
│   ├── scripts/            # Triage automation (Python/Bash)
│   ├── findings/           # Analysis & Risk-Prioritization report
│   └── README.md           # Case-specific summary
├── Case-002-Evidence-Parser/
│   ├── src/                # The Python parser code
│   ├── samples/            # Example log files
│   └── docs/               # Tool documentation
├── Case-003-Network-Forensics/
├── Case-004-Memory-Analysis/
└── IR-Playbooks/           # General strategy and response procedures