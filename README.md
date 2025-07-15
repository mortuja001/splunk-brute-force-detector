#  Splunk Brute-Force Detector

A complete Splunk project to detect and alert brute-force attacks and credential abuse across:

- 🐧 Linux SSH (`Failed password`)
- 🪟 Windows (`EventCode=4625`)
- 🌐 Web Application Login Abuse
- 🕵️ Threat User-Agents (e.g., `curl`, `sqlmap`, `python-requests`, etc.)

---

## Features::

- Brute-force detection for SSH, Windows logon, and Web login POSTs
- Correlation with known threat user-agents (malicious automation tools)
- Alerts via Email & Slack
- Sleek Splunk Dashboard for visual analysis
- 🛠️ Includes macros, inputs, savedsearches, alert scripts

---
## 📊 Dashboard Panels:
- Linux SSH Brute Force
- Windows Login Failures
- Web Login Failures
- Threat User-Agent Tracker
  
![Dashboard Preview](https://raw.githubusercontent.com/mortuja001/splunk-brute-force-detector/main/images/dashboard_preview.png)

---

## 🛠️ Deployment:
1. Import the dashboard XML via Splunk Web > Dashboards > Import.
2. Configure alerts via `Settings > Searches, Reports, and Alerts`.
3. Adjust thresholds as needed.

---

## Reference: 
https://help.splunk.com/en/splunk-enterprise/create-dashboards-and-reports <br>
https://help.splunk.com/en/splunk-enterprise/search/spl2-search-manual/introduction/introduction


