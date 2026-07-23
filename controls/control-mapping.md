# Threat to Control Mapping



| Threat ID | Threat | Primary Controls |

|---|---|---|

| TM-001 | Stolen credentials | MFA, account lockout, login monitoring |

| TM-002 | API authorization bypass | Object-level authorization, automated authorization tests |

| TM-003 | Public object storage | Private bucket policy, encryption, storage access logging |

| TM-004 | Missing admin logs | Centralized audit logging, immutable logs |

| TM-005 | CI/CD secret exposure | Secret scanning, vaulting, key rotation |

| TM-006 | API denial of service | Rate limiting, WAF, request throttling |

| TM-007 | SQL injection | Parameterized queries, input validation, SAST/DAST |

| TM-008 | Weak service authentication | mTLS, service identity, short-lived tokens |

| TM-009 | Overprivileged IAM | Least privilege, permission boundaries, role review |

| TM-010 | Sensitive data in logs | Log redaction, filtering, access control |

| TM-011 | Unsafe file upload | File validation, malware scanning, signed URLs |

| TM-012 | Status endpoint leakage | Authentication, response minimization |

| TM-013 | No encryption at rest | Database encryption, key management |

| TM-014 | Weak cookie settings | Secure cookie flags, TLS, session rotation |

| TM-015 | Vulnerable dependency | SCA scanning, patch SLA, dependency pinning |

