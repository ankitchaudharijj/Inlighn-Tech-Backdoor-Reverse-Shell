
# 🕵️‍♂️ Backdoor (Reverse Shell) - Cyber Security Project

This project demonstrates how a **reverse shell backdoor** works — a common technique used by ethical hackers and cybersecurity professionals to understand remote access methods and potential system vulnerabilities.

> ⚠️ **Disclaimer:** This project is for **educational and ethical hacking** purposes only. Do NOT use it on any unauthorized system or network.

---

## 🚀 Features

- Remote shell command execution
- TCP connection-based communication
- Persistent connection retry
- Minimal and clear Python implementation
- Ideal for beginners and cybersecurity learners

---

## 📁 Project Files

```
Backdoor-Reverse-Shell/
├── server.py    # Runs on attacker's machine, sends commands
├── client.py    # Runs on victim's machine, receives and executes commands
└── README.md    # Project documentation with author details
```

---

## ⚙️ How It Works

### `server.py` (Attacker)
- Waits for incoming connections on a specified port.
- Sends commands to the client.
- Receives command outputs and displays them.

### `client.py` (Victim)
- Tries to connect to the attacker’s IP and port.
- Waits for shell commands.
- Executes them locally and sends back the output.

---

## 🛠️ Setup & Usage

### ✅ Requirements
- Python 3.x on both attacker and victim machines
- Both machines on same network or port-forwarded

### 🖥️ Attacker (Run First)
```bash
python3 server.py
```

### 💻 Victim (Modify IP and Run)
In `client.py`, change:
```python
ATTACKER_IP = 'your.attacker.ip.address'
```

Then run:
```bash
python3 client.py
```

### 🧪 Shell Usage Example
```bash
Shell> whoami
Shell> ls
Shell> ipconfig
Shell> exit
```

---

## 🎯 Educational Purpose

This project is designed for:
- Demonstrating reverse shell attacks in labs
- Understanding ethical hacking tools
- Practicing detection & defense strategies

Great for students, ethical hackers, and cybersecurity enthusiasts.

---

## ⚠️ Legal Disclaimer

- Do NOT run this script on any system or network you don’t own or have explicit permission to use.
- Unauthorized access is a **cybercrime**.
- This project is shared **only** for **learning and awareness**.
- The author is **not responsible** for any misuse.

---

## 👤 Author Details

**Name:** Ankit Chaudhari  
**Education:** B.Tech in Computer Science & Engineering (Cyber Security)  
**University:** Delhi Skill and Entrepreneurship University (DSEU)  
**Certifications:** CEH v12 - Certified Ethical Hacker  
**Internships Completed:** 4 (in AI and Cybersecurity domains)  
**Technical Skills:**  
- Network Auditing  
- Web Application Penetration Testing (VAPT)  
- Vulnerability Assessment  
- Python-based security tools  
- Reverse Shells, Botnets, Port Scanners, Password Crackers  
- Red Teaming Fundamentals  

**GitHub:** [https://github.com/ankitchaudharijj](https://github.com/ankitchaudharijj)  
**LinkedIn:** [https://www.linkedin.com/in/ankit-chaudhari-40346b318/](https://www.linkedin.com/in/ankit-chaudhari-40346b318/)

---

## 📘 License

This project is released under the **MIT License** — feel free to use it in your learning labs and test setups.
