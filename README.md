# 🔐 Splunk Brute-Force Detector

![Dashboard Preview](https://raw.githubusercontent.com/mortuja001/splunk-brute-force-detector/main/images/dashboard_preview.png)

A complete Splunk project to detect and alert brute-force attacks and credential abuse across:

- 🐧 Linux SSH (`Failed password`)
- 🪟 Windows (`EventCode=4625`)
- 🌐 Web Application Login Abuse
- 🕵️ Threat User-Agents (e.g., `curl`, `sqlmap`, `python-requests`, etc.)

---

## 📊 Features

- 🔍 Brute-force detection for SSH, Windows logon, and Web login POSTs
- 🧠 Correlation with known threat user-agents (malicious automation tools)
- 🔔 Alerts via Email & Slack
- 📈 Sleek Splunk Dashboard for visual analysis
- 📁 Fully structured deployment folder
- 🛠️ Includes macros, inputs, savedsearches, alert scripts

---

## 📁 Folder Structure
splunk-brute-force-detector/
├── alerts/
│ ├── brute_force_alerts.csv # Sample generated alert output
├── bin/
│ └── slack_alert.py # Slack alerting script
├── default/
│ ├── savedsearches.conf # Saved searches (alerts)
│ ├── macros.conf # Macros for clean SPL
│ └── inputs.conf # Scheduled input configuration
├── local/
│ └── README-placeholder.txt # Place for local overrides
├── dashboards/
│ └── brute_force_dashboard.xml # Splunk dashboard XML
├── images/
│ └── dashboard_preview.png # Dashboard screenshot
└── README.md

