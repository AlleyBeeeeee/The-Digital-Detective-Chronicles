# 🕵️‍♀️ Case 006: The Chrono-Stitcher
> *"Because logs don't lie, but they certainly do like to whisper in different languages."*

## 📜 The Brief
The digital world is a messy place. When a security breach happens, you don't get a neatly typed confession; you get a pile of "evidence" that looks like a bowl of alphabet soup. 

In **Case 006**, my mission was to take three stubborn witnesses—a **Plain Text Log**, a **CSV Spreadsheet**, and a **JSON Object**—and force them to tell the same story at the same time.

## 🛠 The Detective’s Toolkit
* **Python 3:** The heavy lifter for automation.
* **`datetime`:** Our universal translator for time-traveling logs.
* **Ubuntu VM + VS Code SSH:** The mobile crime lab.
* **Logic:** Because `May 05` and `2026-05-05` are actually the same person in different outfits.

## 🧪 The Forensic Process
1.  **The Collection:** We gather raw data from `auth_logs`, `file_activity`, and `network_traffic`.
2.  **The Sanitization:** We scrub out empty lines and "detective notes" (comments) so they don't clog the engine.
3.  **The Normalization:** We inject years into logs that forgot them and convert ISO 8601 strings into something human.
4.  **The Stitch:** We aggregate everything into a master list and hit the "Sort" button.

## 🚨 The "Aha!" Moment
By stitching the timeline, we caught the **"Smoking Gun"** in high definition:
* **02:15:** Suspect walks in (Admin Login).
* **02:16:** Suspect gains "God Mode" (ROOT escalation).
* **02:18:** Database is staged in `/tmp`.
* **02:20:** **1.2GB of data vanishes into the void via outbound transfer.**

## 💻 How to Run the Lab

### Installation
Run these commands to set up the environment:

```bash
mkdir Case-006-The-Chrono-Stitcher
cd Case-006-The-Chrono-Stitcher
touch auth_logs.txt file_activity.csv network_traffic.json