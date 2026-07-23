# 🧩 Threat Modeling Security Assessment

![Focus](https://img.shields.io/badge/Focus-Threat%20Modeling-blue)
![Methodology](https://img.shields.io/badge/Methodology-STRIDE-purple)
![Diagrams](https://img.shields.io/badge/Diagrams-Mermaid-teal)
![Language](https://img.shields.io/badge/Automation-Python-yellow)
![Type](https://img.shields.io/badge/Type-Security%20Architecture-informational)

A STRIDE-based threat model and security-requirements assessment for a cloud-hosted customer portal — identifying threats, mapping trust boundaries, scoring risk, and tracing threats to controls.

> **TL;DR** — STRIDE analysis of a cloud customer portal: trust boundaries, data-flow analysis, a threat register, attack scenarios, prioritized security requirements, and threat-to-control mapping, output as an automated assessment report.

---

## 📌 Overview

This project demonstrates a threat modeling and security requirements assessment for a fictional cloud-hosted customer portal.

The assessment uses STRIDE to identify threats, document trust boundaries, score risk, map threats to security controls, and generate a professional threat model report.

---

## 🗺️ Scenario

The modeled application includes:

- Customer browser
- Web application
- API backend
- Authentication service
- Customer database
- Object storage
- Admin portal
- Logging/SIEM
- GitHub repository
- CI/CD pipeline
- Cloud deployment environment

---

## 🗺️ Data Flow & Trust Boundaries

```mermaid
flowchart TB
    subgraph INET["🌐 Internet (Untrusted)"]
        CUST["Customer Browser"]
        ADM["Admin User"]
    end

    subgraph APP["🔒 Application Tier"]
        WEB["Web Application"]
        API["API Backend"]
        AUTH["Authentication Service"]
        ADMP["Admin Portal"]
    end

    subgraph DATA["🗄️ Data Tier"]
        DB["Customer Database"]
        OBJ["Object Storage"]
    end

    subgraph OPS["📊 Monitoring / CI-CD"]
        SIEM["Logging / SIEM"]
        CICD["CI/CD Pipeline"]
    end

    CUST -->|HTTPS| WEB
    ADM -->|HTTPS| ADMP
    WEB --> API
    ADMP --> API
    API --> AUTH
    API --> DB
    API --> OBJ
    API -.logs.-> SIEM
    CICD -.deploys.-> WEB
```

Each boundary between subgraphs is a **trust boundary** where STRIDE threats are analyzed (e.g. spoofing at the Internet → Application edge, tampering/EoP at the Application → Data edge).

---

## 🧰 Tools Used

- STRIDE methodology
- Markdown
- CSV
- Python
- Mermaid diagrams
- GitHub

---

## 🧠 Skills Demonstrated

- Threat modeling
- Security architecture review
- Trust boundary identification
- Data flow analysis
- Application security risk analysis
- Cloud security risk analysis
- Risk scoring
- Security control mapping
- Security requirements definition
- Professional security reporting

---

## 📁 Project Structure

| Folder | Description |
|---|---|
| architecture | Data flow diagram and trust boundary documentation |
| threat-model | STRIDE analysis, attack scenarios, and threat register |
| controls | Security requirements and threat-to-control mapping |
| reports | Generated threat model assessment report |
| scripts | Python report generation script |
| notes | Methodology documentation |
| screenshots | Project evidence screenshots |

---

## 📦 Key Deliverables

- Data flow diagram
- Trust boundary analysis
- STRIDE threat analysis
- Threat register
- Attack scenarios
- Security requirements
- Threat-to-control mapping
- Automated assessment report

---

## 📸 Screenshots

### Data Flow Diagram

![Data Flow Diagram](screenshots/01-data-flow-diagram.png)

### Threat Register

![Threat Register](screenshots/02-threat-register.png)

### Threat Model Report

![Threat Model Report](screenshots/03-threat-model-assessment-report.png)

### Security Requirements

![Security Requirements](screenshots/04-security-requirements.png)

---

## 🔑 Security Takeaway

Threat modeling helps identify security risks before deployment. This project demonstrates how security engineering can turn architecture review into actionable security requirements, prioritized controls, and risk-based remediation planning.

---

*Author: Josh · Security Architecture portfolio project*
