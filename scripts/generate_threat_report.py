import csv
from collections import Counter, defaultdict
from pathlib import Path


INPUT_FILE = Path("threat-model/threat-register.csv")
OUTPUT_FILE = Path("reports/threat-model-assessment-report.md")


def load_threats():
    with INPUT_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def clean(value):
    return str(value).replace("|", "-").replace("\n", " ").strip()


def count_by(threats, field):
    return Counter(t[field] for t in threats)


def average_score(threats):
    scores = [int(t["risk_score"]) for t in threats]
    return round(sum(scores) / len(scores), 1) if scores else 0


def main():
    threats = load_threats()
    threats_sorted = sorted(threats, key=lambda t: int(t["risk_score"]), reverse=True)

    rating_counts = count_by(threats, "risk_rating")
    stride_counts = count_by(threats, "stride")
    owner_counts = count_by(threats, "owner")

    owner_risk = defaultdict(int)
    for threat in threats:
        owner_risk[threat["owner"]] += int(threat["risk_score"])

    lines = [
        "# Threat Model Assessment Report",
        "",
        "## Executive Summary",
        "",
        "This report summarizes the threat model for a fictional cloud-hosted customer portal.",
        "",
        "The assessment used STRIDE to identify architecture-level threats, assign risk ratings, and map risks to recommended security controls.",
        "",
        "## Key Metrics",
        "",
        f"- Total threats identified: {len(threats)}",
        f"- Average risk score: {average_score(threats)}",
        f"- Critical threats: {rating_counts.get('Critical', 0)}",
        f"- High threats: {rating_counts.get('High', 0)}",
        f"- Medium threats: {rating_counts.get('Medium', 0)}",
        "",
        "## Risk Rating Breakdown",
        "",
        "| Rating | Count |",
        "|---|---|",
    ]

    for rating in ["Critical", "High", "Medium", "Low"]:
        lines.append(f"| {rating} | {rating_counts.get(rating, 0)} |")

    lines.extend([
        "",
        "## STRIDE Breakdown",
        "",
        "| STRIDE Category | Count |",
        "|---|---|",
    ])

    for category, count in stride_counts.most_common():
        lines.append(f"| {clean(category)} | {count} |")

    lines.extend([
        "",
        "## Ownership View",
        "",
        "| Owner | Threat Count | Total Risk Score |",
        "|---|---|---|",
    ])

    for owner, count in owner_counts.most_common():
        lines.append(f"| {clean(owner)} | {count} | {owner_risk[owner]} |")

    lines.extend([
        "",
        "## Top Threats",
        "",
        "| ID | Threat | STRIDE | Asset | Risk Score | Rating | Recommended Controls | Owner |",
        "|---|---|---|---|---|---|---|---|",
    ])

    for threat in threats_sorted[:10]:
        lines.append(
            f"| {clean(threat['id'])} "
            f"| {clean(threat['threat'])} "
            f"| {clean(threat['stride'])} "
            f"| {clean(threat['asset'])} "
            f"| {clean(threat['risk_score'])} "
            f"| {clean(threat['risk_rating'])} "
            f"| {clean(threat['recommended_controls'])} "
            f"| {clean(threat['owner'])} |"
        )

    lines.extend([
        "",
        "## Security Engineering Recommendations",
        "",
        "### Priority 1: Fix Critical Authorization and IAM Risks",
        "",
        "- Enforce object-level authorization on all API requests.",
        "- Review cloud IAM roles for least privilege.",
        "- Add deployment approval gates for privileged infrastructure changes.",
        "",
        "### Priority 2: Improve CI/CD and Secret Protection",
        "",
        "- Enable secret scanning.",
        "- Store secrets in a vault.",
        "- Rotate exposed or suspected secrets immediately.",
        "- Prevent deployments when critical security findings are detected.",
        "",
        "### Priority 3: Reduce Data Exposure Risk",
        "",
        "- Block public access to object storage.",
        "- Encrypt sensitive data at rest and in transit.",
        "- Redact tokens, passwords, and customer data from logs.",
        "",
        "### Priority 4: Strengthen Monitoring and Auditability",
        "",
        "- Log admin actions centrally.",
        "- Monitor authentication and authorization failures.",
        "- Alert on suspicious access patterns.",
        "",
        "## Conclusion",
        "",
        "This threat model demonstrates how security engineering can identify design-level risks before deployment and translate them into security requirements, control recommendations, and risk-based remediation priorities.",
    ])

    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")

    print("Threat model report generated:")
    print(f"- {OUTPUT_FILE}")


if __name__ == "__main__":
    main()