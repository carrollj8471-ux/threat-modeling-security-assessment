# Threat Model Assessment Report

## Executive Summary

This report summarizes the threat model for a fictional cloud-hosted customer portal.

The assessment used STRIDE to identify architecture-level threats, assign risk ratings, and map risks to recommended security controls.

## Key Metrics

- Total threats identified: 15
- Average risk score: 14.8
- Critical threats: 3
- High threats: 5
- Medium threats: 7

## Risk Rating Breakdown

| Rating | Count |
|---|---|
| Critical | 3 |
| High | 5 |
| Medium | 7 |
| Low | 0 |

## STRIDE Breakdown

| STRIDE Category | Count |
|---|---|
| Information Disclosure | 5 |
| Spoofing | 3 |
| Elevation of Privilege | 3 |
| Tampering | 2 |
| Repudiation | 1 |
| Denial of Service | 1 |

## Ownership View

| Owner | Threat Count | Total Risk Score |
|---|---|---|
| Application Security | 6 | 89 |
| Cloud Security | 4 | 57 |
| SOC / Detection Engineering | 2 | 24 |
| DevSecOps | 2 | 36 |
| Identity Security | 1 | 16 |

## Top Threats

| ID | Threat | STRIDE | Asset | Risk Score | Rating | Recommended Controls | Owner |
|---|---|---|---|---|---|---|---|
| TM-002 | API authorization bypass exposes another customer's records | Elevation of Privilege | Customer data | 25 | Critical | Object-level authorization, deny-by-default access checks, automated authorization tests | Application Security |
| TM-005 | CI/CD secrets are exposed in source code repository | Information Disclosure | CI/CD pipeline | 20 | Critical | Secret scanning, pre-commit hooks, secret vaulting, key rotation | DevSecOps |
| TM-009 | Overly broad cloud IAM role allows privilege escalation | Elevation of Privilege | Cloud environment | 20 | Critical | Least privilege IAM, permission boundaries, role review, deployment approvals | Cloud Security |
| TM-001 | Stolen user credentials used to access the customer portal | Spoofing | User accounts | 16 | High | MFA, account lockout, impossible travel detection, login alerting | Identity Security |
| TM-006 | Public API is overwhelmed by automated requests | Denial of Service | API backend | 16 | High | Rate limiting, WAF rules, autoscaling, request throttling | Application Security |
| TM-015 | Vulnerable dependency is deployed into production | Elevation of Privilege | Application runtime | 16 | High | SCA scanning, dependency pinning, patch SLAs, build failure on critical findings | DevSecOps |
| TM-003 | Public object storage exposes uploaded customer files | Information Disclosure | Object storage | 15 | High | Private storage, bucket policies, encryption, access logging, CSPM checks | Cloud Security |
| TM-007 | SQL injection allows database access | Tampering | Database | 15 | High | Parameterized queries, input validation, SAST, DAST testing | Application Security |
| TM-004 | Admin actions are not logged | Repudiation | Admin portal | 12 | Medium | Centralized audit logging, immutable logs, admin activity monitoring | SOC / Detection Engineering |
| TM-008 | Weak service-to-service authentication allows internal spoofing | Spoofing | Internal services | 12 | Medium | mTLS, service identity, short-lived tokens, network segmentation | Cloud Security |

## Security Engineering Recommendations

### Priority 1: Fix Critical Authorization and IAM Risks

- Enforce object-level authorization on all API requests.
- Review cloud IAM roles for least privilege.
- Add deployment approval gates for privileged infrastructure changes.

### Priority 2: Improve CI/CD and Secret Protection

- Enable secret scanning.
- Store secrets in a vault.
- Rotate exposed or suspected secrets immediately.
- Prevent deployments when critical security findings are detected.

### Priority 3: Reduce Data Exposure Risk

- Block public access to object storage.
- Encrypt sensitive data at rest and in transit.
- Redact tokens, passwords, and customer data from logs.

### Priority 4: Strengthen Monitoring and Auditability

- Log admin actions centrally.
- Monitor authentication and authorization failures.
- Alert on suspicious access patterns.

## Conclusion

This threat model demonstrates how security engineering can identify design-level risks before deployment and translate them into security requirements, control recommendations, and risk-based remediation priorities.