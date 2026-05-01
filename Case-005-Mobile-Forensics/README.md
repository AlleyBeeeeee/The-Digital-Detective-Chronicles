# 📡 Case 005: The Mobile Privacy Auditor
---

## I’ve got my eye on the UI (and the MIC) !
---

### 🕵️‍♀️ Investigation Brief
Ever feel like your phone is listening to you? For Case 005, I decided to stop wondering and start auditing. While the hardware was looking "phoney" (get it?), I went deep into the software to see which apps were overstaying their welcome in the background.

---

### 🛠️ The Technical "Byte"
Mobile apps love to ask for permissions like they’re collecting infinity stones. I built an automated auditor to find the apps that have "boundary issues."

How it works (The low-down on the high-tech):

The Script: I wrote privacy_auditor.py to play detective.

The Logic: It doesn't just look for what an app is doing, but when.

The "Sleepy" Sensor: If an app is touching the Microphone or GPS at 3:00 AM, my script flags it faster than a waiter at a busy brunch.

---

### 🚀 The "Aha!" Moment
I caught CalculatorPro red-handed (or red-circuited).

The Crime: Accessing the Microphone and GPS at 03:22 AM.

The Verdict: Unless you're doing trigonometry in your sleep, that’s a major privacy "mis-calculation." 🚩

📂 Repo Tour
scripts/: Where the Python magic happens.

data/: The manifest files (a.k.a. the "paper trail").

reports/: My formal Incident Report. It’s very professional, I promise.

assets/: Pictures of the crime scene (terminal screenshots).

### 📑 Formal Documentation
If you want the full, serious, "put-on-a-suit" breakdown of how I handled this breach, check out the:
👉 Case 005 Incident Report

---

### 💡 The Takeaway
As a tech professional who bridges the gap between hardware repair and cybersecurity, I know that sometimes the best way to fix a device is to look at the code, not the screen. I’m here to secure the data and fix the hardware—one pun at a time.

