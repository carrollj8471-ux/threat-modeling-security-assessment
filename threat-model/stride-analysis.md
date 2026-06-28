\# STRIDE Threat Analysis



\## Overview



This project uses STRIDE to identify threats across a cloud-hosted customer portal architecture.



STRIDE categories:



| Category | Meaning |

|---|---|

| Spoofing | Pretending to be another user or service |

| Tampering | Modifying data, requests, files, or configurations |

| Repudiation | Performing actions without reliable audit evidence |

| Information Disclosure | Exposing sensitive data |

| Denial of Service | Reducing availability of a system |

| Elevation of Privilege | Gaining unauthorized permissions |



\## STRIDE Findings Summary



| STRIDE Category | Example Finding |

|---|---|

| Spoofing | Stolen credentials used to access customer portal |

| Tampering | Unsafe API request manipulation or SQL injection |

| Repudiation | Admin actions not logged |

| Information Disclosure | Public object storage or leaked CI/CD secrets |

| Denial of Service | Public API overwhelmed by automated traffic |

| Elevation of Privilege | Broken object-level authorization or overprivileged IAM role |



\## Security Engineering Value



STRIDE helps convert architecture review into specific security requirements. Instead of only identifying vulnerabilities after deployment, this process helps identify design weaknesses before implementation.

