import os
import json

base_dir = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base"
skills_dir = os.path.join(base_dir, "skills", "cyber-security")
evidence_dir = os.path.join(base_dir, "evidence", "cyber-security")
scoring_dir = os.path.join(base_dir, "scoring", "cyber-security")

os.makedirs(skills_dir, exist_ok=True)
os.makedirs(evidence_dir, exist_ok=True)
os.makedirs(scoring_dir, exist_ok=True)

# 1. Skills
skills_data = {
    "cs_networking": {
        "skill_id": "cs_networking",
        "name": "Networking Fundamentals",
        "category": "networking",
        "description": "Understanding of network protocols, architecture, and security devices.",
        "subskills": [
            {"id": "tcp_ip", "name": "TCP/IP & OSI Model", "description": "Understanding network layers and protocols.", "keywords": ["TCP", "UDP", "OSI", "IPv4", "IPv6"]},
            {"id": "firewalls", "name": "Firewalls & IDS/IPS", "description": "Configuring and managing network security boundaries.", "keywords": ["iptables", "pfsense", "snort", "suricata", "WAF", "IDS", "IPS"]},
            {"id": "vpns", "name": "VPNs & Secure Tunnels", "description": "Implementing secure communication channels.", "keywords": ["IPSec", "OpenVPN", "WireGuard", "IKEv2"]}
        ],
        "evidence": {
            "github": [{"signal": "Firewall rules or VPN configs in repo", "detection": "file_presence", "pattern": "iptables.rules|openvpn.conf", "strength": 0.7, "maps_to": ["cs_networking.firewalls", "cs_networking.vpns"]}],
            "cv": [{"signal": "Configured firewalls or VPNs", "strength": 0.8, "maps_to": ["cs_networking.firewalls", "cs_networking.vpns"]}],
            "linkedin": [{"signal": "Networking or Firewalls in skills", "strength": 0.4, "maps_to": ["cs_networking.tcp_ip", "cs_networking.firewalls"]}],
            "assessment": [{"signal": "Can design secure network architecture", "strength": 1.0, "maps_to": ["cs_networking.tcp_ip", "cs_networking.firewalls", "cs_networking.vpns"]}]
        },
        "levels": {
            "junior": {"expected_subskills": ["tcp_ip"], "description": "Understands basic networking concepts."},
            "mid": {"expected_subskills": ["firewalls"], "description": "Can manage firewalls and IDS/IPS."},
            "senior": {"expected_subskills": ["vpns"], "description": "Designs complex secure network architectures and VPNs."}
        }
    },
    "cs_os_security": {
        "skill_id": "cs_os_security",
        "name": "Linux/Operating Systems Security",
        "category": "os_security",
        "description": "Securing and hardening operating systems against attacks.",
        "subskills": [
            {"id": "hardening", "name": "OS Hardening", "description": "Applying security baselines and patches.", "keywords": ["CIS benchmarks", "hardening", "patch management"]},
            {"id": "access_control", "name": "Access Control & IAM", "description": "Managing user permissions and authentication.", "keywords": ["PAM", "SELinux", "AppArmor", "RBAC", "Active Directory"]},
            {"id": "auditing", "name": "Auditing & Logging", "description": "Monitoring system logs for suspicious activity.", "keywords": ["auditd", "syslog", "journalctl", "event logs"]}
        ],
        "evidence": {
            "github": [{"signal": "Hardening scripts or SELinux policies", "detection": "content_analysis", "pattern": "SELINUX=enforcing|auditd", "strength": 0.8, "maps_to": ["cs_os_security.access_control", "cs_os_security.auditing"]}],
            "cv": [{"signal": "Experience with Linux hardening", "strength": 0.7, "maps_to": ["cs_os_security.hardening"]}],
            "linkedin": [{"signal": "Linux Security endorsement", "strength": 0.3, "maps_to": ["cs_os_security.hardening"]}],
            "assessment": [{"signal": "Can implement zero-trust access control", "strength": 1.0, "maps_to": ["cs_os_security.hardening", "cs_os_security.access_control", "cs_os_security.auditing"]}]
        },
        "levels": {
            "junior": {"expected_subskills": ["auditing"], "description": "Can monitor and review system logs."},
            "mid": {"expected_subskills": ["hardening"], "description": "Can apply CIS benchmarks and hardening scripts."},
            "senior": {"expected_subskills": ["access_control"], "description": "Designs enterprise-wide access control and IAM strategies."}
        }
    },
    "cs_cryptography": {
        "skill_id": "cs_cryptography",
        "name": "Cryptography",
        "category": "cryptography",
        "description": "Applied cryptography, encryption, and certificate management.",
        "subskills": [
            {"id": "encryption_hashing", "name": "Encryption & Hashing", "description": "Symmetric/Asymmetric encryption and hash algorithms.", "keywords": ["AES", "RSA", "SHA-256", "bcrypt"]},
            {"id": "pki", "name": "PKI & Key Management", "description": "Managing certificates and cryptographic keys.", "keywords": ["PKI", "X.509", "Let's Encrypt", "KMS", "HSM"]},
            {"id": "tls", "name": "TLS/SSL Configurations", "description": "Securing data in transit.", "keywords": ["TLS 1.3", "SSL", "OpenSSL"]}
        ],
        "evidence": {
            "github": [{"signal": "TLS config or encryption implementations", "detection": "content_analysis", "pattern": "ssl_certificate|ssl_protocols TLSv1.2 TLSv1.3", "strength": 0.8, "maps_to": ["cs_cryptography.tls"]}],
            "cv": [{"signal": "Implemented PKI or KMS", "strength": 0.8, "maps_to": ["cs_cryptography.pki"]}],
            "linkedin": [{"signal": "Cryptography skills", "strength": 0.4, "maps_to": ["cs_cryptography.encryption_hashing"]}],
            "assessment": [{"signal": "Can design secure key lifecycle management", "strength": 1.0, "maps_to": ["cs_cryptography.encryption_hashing", "cs_cryptography.pki", "cs_cryptography.tls"]}]
        },
        "levels": {
            "junior": {"expected_subskills": ["encryption_hashing"], "description": "Understands basic encryption and hashing algorithms."},
            "mid": {"expected_subskills": ["tls"], "description": "Can configure secure TLS/SSL for web servers."},
            "senior": {"expected_subskills": ["pki"], "description": "Manages enterprise PKI and hardware security modules (HSM)."}
        }
    },
    "cs_security_tools": {
        "skill_id": "cs_security_tools",
        "name": "Security Tools (Wireshark/Nmap)",
        "category": "security_tools",
        "description": "Proficiency with industry-standard security analysis and penetration testing tools.",
        "subskills": [
            {"id": "network_analysis", "name": "Network Sniffing & Analysis", "description": "Using Wireshark and tcpdump to analyze traffic.", "keywords": ["Wireshark", "tcpdump", "PCAP"]},
            {"id": "vuln_scanning", "name": "Vulnerability Scanning", "description": "Identifying system vulnerabilities.", "keywords": ["Nmap", "Nessus", "OpenVAS", "Qualys"]},
            {"id": "siem", "name": "SIEM & Log Analysis", "description": "Aggregating and analyzing security events.", "keywords": ["Splunk", "ELK", "QRadar", "AlienVault"]}
        ],
        "evidence": {
            "github": [{"signal": "Nmap scripts or PCAP analysis scripts", "detection": "file_presence", "pattern": "*.nse|*.pcap", "strength": 0.6, "maps_to": ["cs_security_tools.vuln_scanning", "cs_security_tools.network_analysis"]}],
            "cv": [{"signal": "Managed SIEM deployments", "strength": 0.9, "maps_to": ["cs_security_tools.siem"]}],
            "linkedin": [{"signal": "Wireshark or Nmap endorsements", "strength": 0.3, "maps_to": ["cs_security_tools.network_analysis", "cs_security_tools.vuln_scanning"]}],
            "assessment": [{"signal": "Can perform advanced packet analysis and SIEM query creation", "strength": 1.0, "maps_to": ["cs_security_tools.network_analysis", "cs_security_tools.vuln_scanning", "cs_security_tools.siem"]}]
        },
        "levels": {
            "junior": {"expected_subskills": ["vuln_scanning"], "description": "Can run basic Nmap scans and identify open ports."},
            "mid": {"expected_subskills": ["network_analysis"], "description": "Can analyze PCAP files and troubleshoot network anomalies."},
            "senior": {"expected_subskills": ["siem"], "description": "Architects SIEM deployments and creates complex correlation rules."}
        }
    },
    "cs_risk_compliance": {
        "skill_id": "cs_risk_compliance",
        "name": "Risk & Compliance",
        "category": "risk_compliance",
        "description": "Governance, risk management, and compliance frameworks.",
        "subskills": [
            {"id": "risk_assessment", "name": "Risk Assessment", "description": "Identifying and quantifying security risks.", "keywords": ["Risk Assessment", "Threat Modeling", "STRIDE", "DREAD"]},
            {"id": "frameworks", "name": "Security Frameworks (ISO 27001/NIST)", "description": "Implementing standard security frameworks.", "keywords": ["ISO 27001", "NIST CSF", "SOC2", "CIS Controls"]},
            {"id": "regulations", "name": "Regulatory Compliance", "description": "Ensuring adherence to legal regulations.", "keywords": ["GDPR", "CCPA", "HIPAA", "PCI-DSS"]}
        ],
        "evidence": {
            "github": [{"signal": "Security policies or threat models in repo", "detection": "file_presence", "pattern": "SECURITY.md|threat-model.md", "strength": 0.5, "maps_to": ["cs_risk_compliance.risk_assessment"]}],
            "cv": [{"signal": "Led ISO 27001 or SOC2 audits", "strength": 0.9, "maps_to": ["cs_risk_compliance.frameworks", "cs_risk_compliance.regulations"]}],
            "linkedin": [{"signal": "Compliance and Risk Management in skills", "strength": 0.4, "maps_to": ["cs_risk_compliance.risk_assessment", "cs_risk_compliance.frameworks"]}],
            "assessment": [{"signal": "Can build a complete compliance program from scratch", "strength": 1.0, "maps_to": ["cs_risk_compliance.risk_assessment", "cs_risk_compliance.frameworks", "cs_risk_compliance.regulations"]}]
        },
        "levels": {
            "junior": {"expected_subskills": ["risk_assessment"], "description": "Assists with basic risk assessments and threat modeling."},
            "mid": {"expected_subskills": ["regulations"], "description": "Ensures systems comply with GDPR/HIPAA or similar regulations."},
            "senior": {"expected_subskills": ["frameworks"], "description": "Leads organizational implementation of ISO 27001 or NIST CSF."}
        }
    }
}

for k, v in skills_data.items():
    with open(os.path.join(skills_dir, f"{k}.json"), "w") as f:
        json.dump(v, f, indent=2)

# 2. Evidence Files
evidence_data = {
    "github": {
        "source_id": "github",
        "name": "GitHub Repository Analysis - Cyber Security",
        "description": "Signals extracted from GitHub repositories to evidence Cyber Security skills.",
        "preprocessing_pipeline": {
            "description": "Steps the backend takes.",
            "steps": [
                {
                    "step": 1,
                    "name": "file_tree_scan",
                    "description": "Scan the repository file tree for Security-relevant files.",
                    "target_files": [
                        {"pattern": "iptables.rules|openvpn.conf", "skill": "cs_networking", "priority": "high"},
                        {"pattern": "SELINUX=enforcing|auditd", "skill": "cs_os_security", "priority": "high"},
                        {"pattern": "ssl_certificate|ssl_protocols TLSv1.2 TLSv1.3", "skill": "cs_cryptography", "priority": "high"},
                        {"pattern": "*.nse|*.pcap", "skill": "cs_security_tools", "priority": "medium"},
                        {"pattern": "SECURITY.md|threat-model.md", "skill": "cs_risk_compliance", "priority": "low"}
                    ]
                }
            ]
        },
        "ai_analysis_instructions": {
            "description": "What AI should do with the preprocessed data.",
            "tasks": ["Map identified files and patterns to specific subskills using COMPOSITE KEYS."],
            "output_format": {
                "composite_key_example": "cs_networking.firewalls"
            }
        }
    },
    "cv": {
        "source_id": "cv",
        "name": "CV/Resume Analysis - Cyber Security",
        "description": "Extracting Cyber Security experience from CVs."
    },
    "linkedin": {
        "source_id": "linkedin",
        "name": "LinkedIn Profile Analysis - Cyber Security",
        "description": "Extracting Cyber Security endorsements and skills."
    },
    "assessment": {
        "source_id": "assessment",
        "name": "Technical Assessment - Cyber Security",
        "description": "Results from hands-on cyber security labs."
    }
}

for k, v in evidence_data.items():
    with open(os.path.join(evidence_dir, f"{k}.json"), "w") as f:
        json.dump(v, f, indent=2)

# 3. Engine Config
engine_data = {
    "engine_version": "1.0",
    "role": "cyber-security",
    "scoring_formula": "Weighted sum based on evidence strength."
}
with open(os.path.join(scoring_dir, "engine.json"), "w") as f:
    json.dump(engine_data, f, indent=2)

# 4. Update validate_composite_keys.py
script_path = r"c:\Users\clbie\Desktop\Projects\RoleGauge\scripts\validate_composite_keys.py"
with open(script_path, "r", encoding="utf-8") as f:
    script_content = f.read()

# Make it search recursively
new_script = script_content.replace(
    r"skills_dir = r'c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base\skills\*.json'",
    r"skills_dir = r'c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base\skills\**\*.json'"
).replace(
    r"evidence_dir = r'c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base\evidence\*.json'",
    r"evidence_dir = r'c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base\evidence\**\*.json'"
)

# Also update glob to use recursive=True
new_script = new_script.replace("glob.glob(skills_dir)", "glob.glob(skills_dir, recursive=True)")
new_script = new_script.replace("glob.glob(evidence_dir)", "glob.glob(evidence_dir, recursive=True)")

with open(script_path, "w", encoding="utf-8") as f:
    f.write(new_script)
