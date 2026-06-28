\# Trust Boundaries



\## Overview



Trust boundaries identify where data crosses between different security zones, identities, or privilege levels.



These boundaries are important because threats often occur when untrusted data enters a trusted system.



\## Identified Trust Boundaries



| Boundary | Description | Security Concern |

|---|---|---|

| Internet to WAF/Web App | Public users access the application | Authentication bypass, injection, denial of service |

| Web App to API Backend | Frontend sends requests to backend services | Broken authorization, tampering, input validation |

| API Backend to Database | Application queries sensitive customer records | SQL injection, excessive access, data leakage |

| API Backend to Object Storage | Application reads and writes uploaded files | Public exposure, unsafe uploads, malware |

| Admin Portal to API | Privileged users perform support actions | Privilege abuse, lack of audit logging |

| Developer to GitHub | Developers push code to source control | Secret leakage, insecure code, dependency risk |

| GitHub to CI/CD Pipeline | Code is built and deployed | Supply chain compromise, excessive deployment permissions |

| CI/CD Pipeline to Cloud | Pipeline deploys infrastructure and workloads | Overprivileged IAM, unauthorized changes |

| Application to Logging/SIEM | Application sends security and audit logs | Sensitive data leakage, missing audit events |



