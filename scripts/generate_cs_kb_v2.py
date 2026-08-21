import os
import json
import shutil

base_dir = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base"
skills_dir = os.path.join(base_dir, "skills", "cyber-security")
evidence_dir = os.path.join(base_dir, "evidence", "cyber-security")
roles_dir = os.path.join(base_dir, "roles", "cyber-security")
scoring_dir = os.path.join(base_dir, "scoring", "cyber-security")

os.makedirs(skills_dir, exist_ok=True)
os.makedirs(evidence_dir, exist_ok=True)
os.makedirs(roles_dir, exist_ok=True)

# 1. Delete incorrect scoring engine for cyber-security to keep single source of truth
engine_path = os.path.join(scoring_dir, "engine.json")
if os.path.exists(engine_path):
    os.remove(engine_path)
    print(f"Deleted {engine_path}")

# 2. Roles Data
roles_data = {
    "junior": {
        "role_id": "cyber_security",
        "level": "junior",
        "title": "Junior Cyber Security Analyst",
        "description": "Entry-level security position focused on foundational networking, OS security, and basic tool usage.",
        "experience_range": "0-2 years",
        "skills": [
            {"skill_id": "cs_networking", "importance": 0.95, "rationale": "Foundation for all security work; understanding traffic is non-negotiable"},
            {"skill_id": "cs_os_security", "importance": 0.90, "rationale": "Daily interaction with OS permissions and logs"},
            {"skill_id": "cs_security_tools", "importance": 0.85, "rationale": "Must use basic scanners and analyzers effectively"},
            {"skill_id": "cs_cryptography", "importance": 0.60, "rationale": "Basic understanding of hashing and encryption required"},
            {"skill_id": "cs_risk_compliance", "importance": 0.50, "rationale": "Awareness of policies and basic risk concepts"}
        ],
        "scoring": {
            "method": "weighted_average",
            "description": "Each skill score is multiplied by its importance weight. Final score is sum divided by sum of weights.",
            "thresholds": {
                "not_ready": {"min": 0.0, "max": 0.3, "label": "Not Ready", "description": "Significant gaps in foundations"},
                "developing": {"min": 0.3, "max": 0.5, "label": "Developing", "description": "Some foundations, needs learning"},
                "approaching": {"min": 0.5, "max": 0.7, "label": "Approaching Ready", "description": "Most foundations present"},
                "ready": {"min": 0.7, "max": 0.85, "label": "Ready", "description": "Meets junior expectations"},
                "exceeds": {"min": 0.85, "max": 1.0, "label": "Exceeds Expectations", "description": "Exceeds junior expectations"}
            }
        }
    },
    "mid": {
        "role_id": "cyber_security",
        "level": "mid",
        "title": "Cyber Security Engineer",
        "description": "Mid-level position requiring hands-on implementation of firewalls, SIEM, and vulnerability management.",
        "experience_range": "3-5 years",
        "skills": [
            {"skill_id": "cs_networking", "importance": 0.85, "rationale": "Configuring VPNs and firewalls is a core duty"},
            {"skill_id": "cs_os_security", "importance": 0.85, "rationale": "Advanced hardening and patching"},
            {"skill_id": "cs_security_tools", "importance": 0.90, "rationale": "Proficient use of SIEM and offensive/defensive tools"},
            {"skill_id": "cs_cryptography", "importance": 0.75, "rationale": "Managing certificates and PKI components"},
            {"skill_id": "cs_risk_compliance", "importance": 0.70, "rationale": "Conducting threat models and ensuring framework compliance"}
        ],
        "scoring": {
            "method": "weighted_average",
            "description": "Each skill score is multiplied by its importance weight. Final score is sum divided by sum of weights.",
            "thresholds": {
                "not_ready": {"min": 0.0, "max": 0.4, "label": "Not Ready", "description": "Significant gaps in mid-level skills"},
                "developing": {"min": 0.4, "max": 0.6, "label": "Developing", "description": "Growing into mid-level role"},
                "approaching": {"min": 0.6, "max": 0.75, "label": "Approaching Ready", "description": "Almost fully capable"},
                "ready": {"min": 0.75, "max": 0.9, "label": "Ready", "description": "Solid mid-level performer"},
                "exceeds": {"min": 0.9, "max": 1.0, "label": "Exceeds Expectations", "description": "Ready for senior responsibilities"}
            }
        }
    },
    "senior": {
        "role_id": "cyber_security",
        "level": "senior",
        "title": "Senior Cyber Security Architect",
        "description": "Senior-level position focused on architecture, zero-trust, enterprise compliance, and advanced threat hunting.",
        "experience_range": "6+ years",
        "skills": [
            {"skill_id": "cs_networking", "importance": 0.90, "rationale": "Designing zero-trust and enterprise network segmentation"},
            {"skill_id": "cs_os_security", "importance": 0.80, "rationale": "Enterprise IAM and kernel-level security"},
            {"skill_id": "cs_security_tools", "importance": 0.85, "rationale": "Architecting SIEM and custom threat hunting solutions"},
            {"skill_id": "cs_cryptography", "importance": 0.85, "rationale": "Enterprise key management and HSM strategies"},
            {"skill_id": "cs_risk_compliance", "importance": 0.95, "rationale": "Owning SOC2/ISO27001 programs and third-party risk"}
        ],
        "scoring": {
            "method": "weighted_average",
            "description": "Each skill score is multiplied by its importance weight. Final score is sum divided by sum of weights.",
            "thresholds": {
                "not_ready": {"min": 0.0, "max": 0.5, "label": "Not Ready", "description": "Lacks architectural depth"},
                "developing": {"min": 0.5, "max": 0.7, "label": "Developing", "description": "Has some senior traits but needs broader impact"},
                "approaching": {"min": 0.7, "max": 0.85, "label": "Approaching Ready", "description": "Strong candidate with minor gaps"},
                "ready": {"min": 0.85, "max": 0.95, "label": "Ready", "description": "Meets senior expectations"},
                "exceeds": {"min": 0.95, "max": 1.0, "label": "Exceeds Expectations", "description": "Exceptional architectural mastery"}
            }
        }
    }
}

for level, data in roles_data.items():
    with open(os.path.join(roles_dir, f"{level}.json"), "w") as f:
        json.dump(data, f, indent=2)

# 3. Skills Data - Deepened
skills_data = {
    "cs_networking": {
        "skill_id": "cs_networking",
        "name": "Networking Fundamentals",
        "category": "networking",
        "description": "Deep understanding of network protocols, security devices, and architectural models.",
        "subskills": [
            {"id": "tcp_ip", "name": "TCP/IP & OSI", "description": "Deep knowledge of packet structures and layers.", "keywords": ["TCP", "UDP", "OSI", "IPv4", "IPv6"]},
            {"id": "subnetting", "name": "Subnetting & Routing", "description": "Designing IP spaces and routing protocols.", "keywords": ["BGP", "OSPF", "CIDR", "VLAN"]},
            {"id": "packet_analysis", "name": "Packet Analysis", "description": "Analyzing raw network traffic.", "keywords": ["PCAP", "Wireshark", "tcpdump"]},
            {"id": "firewalls", "name": "Firewalls & NGFW", "description": "Configuring L3-L7 firewalls.", "keywords": ["iptables", "Palo Alto", "Fortinet", "pfSense"]},
            {"id": "ids_ips", "name": "IDS/IPS", "description": "Intrusion detection and prevention.", "keywords": ["Snort", "Suricata", "Zeek"]},
            {"id": "vpns", "name": "VPNs & Tunnels", "description": "Secure communications.", "keywords": ["IPSec", "OpenVPN", "WireGuard"]},
            {"id": "network_segmentation", "name": "Network Segmentation", "description": "Isolating network zones.", "keywords": ["Microsegmentation", "DMZ", "VLAN hopping mitigation"]},
            {"id": "zero_trust", "name": "Zero Trust Architecture", "description": "BeyondCorp and zero trust models.", "keywords": ["Zero Trust", "ZTA", "Identity-Aware Proxy"]},
            {"id": "ddos_mitigation", "name": "DDoS Mitigation", "description": "Defending against volumetric attacks.", "keywords": ["Cloudflare", "Akamai", "BGP Anycast", "Rate limiting"]}
        ],
        "evidence": {
            "github": [{"signal": "Firewall or routing configs", "detection": "file_presence", "pattern": "iptables.rules|*.pcap", "strength": 0.7, "maps_to": ["cs_networking.firewalls", "cs_networking.packet_analysis"]}],
            "cv": [{"signal": "Configured firewalls or VPNs", "strength": 0.8, "maps_to": ["cs_networking.firewalls", "cs_networking.vpns"]}],
            "linkedin": [{"signal": "Network security skills", "strength": 0.4, "maps_to": ["cs_networking.tcp_ip", "cs_networking.firewalls"]}],
            "assessment": [{"signal": "Can design secure network architecture", "strength": 1.0, "maps_to": ["cs_networking.tcp_ip", "cs_networking.firewalls", "cs_networking.vpns", "cs_networking.zero_trust"]}]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["tcp_ip", "subnetting", "packet_analysis"], 
                "description": "Understands network protocols and can analyze basic traffic.",
                "additional_expectations": "Can read PCAPs and explain OSI layers."
            },
            "mid": {
                "expected_subskills": ["firewalls", "ids_ips", "vpns"], 
                "description": "Can manage security boundaries and secure tunnels.",
                "additional_expectations": "Able to troubleshoot VPN connectivity and tune IDS rules."
            },
            "senior": {
                "expected_subskills": ["network_segmentation", "zero_trust", "ddos_mitigation"], 
                "description": "Designs enterprise network security architectures.",
                "additional_expectations": "Can architect a complete zero-trust migration."
            }
        }
    },
    "cs_os_security": {
        "skill_id": "cs_os_security",
        "name": "OS Security",
        "category": "os_security",
        "description": "Hardening, access control, and deep OS security mechanisms.",
        "subskills": [
            {"id": "user_management", "name": "User & Group Management", "description": "Basic IAM on OS.", "keywords": ["/etc/passwd", "groups", "sudoers"]},
            {"id": "file_permissions", "name": "File Permissions", "description": "POSIX ACLs and ownership.", "keywords": ["chmod", "chown", "ACLs", "SUID"]},
            {"id": "auditing", "name": "Auditing & Logging", "description": "System event logging.", "keywords": ["auditd", "syslog", "journalctl"]},
            {"id": "hardening", "name": "OS Hardening", "description": "Applying baselines.", "keywords": ["CIS benchmarks", "STIGs", "hardening"]},
            {"id": "patch_management", "name": "Patch Management", "description": "Keeping systems updated securely.", "keywords": ["wsus", "apt", "yum", "vulnerability patching"]},
            {"id": "mac", "name": "Mandatory Access Control", "description": "Advanced access control systems.", "keywords": ["SELinux", "AppArmor"]},
            {"id": "pam_config", "name": "PAM Configuration", "description": "Pluggable Authentication Modules.", "keywords": ["PAM", "authentication", "LDAP integration"]},
            {"id": "kernel_tuning", "name": "Kernel Security Tuning", "description": "Securing the OS kernel.", "keywords": ["sysctl", "grub", "ebpf", "seccomp"]},
            {"id": "malware_analysis", "name": "Basic Malware Analysis", "description": "Analyzing suspicious processes.", "keywords": ["strace", "lsof", "memory forensics"]}
        ],
        "evidence": {
            "github": [{"signal": "Hardening scripts", "detection": "content_analysis", "pattern": "SELINUX=enforcing|auditd", "strength": 0.8, "maps_to": ["cs_os_security.mac", "cs_os_security.auditing"]}],
            "cv": [{"signal": "Linux hardening experience", "strength": 0.7, "maps_to": ["cs_os_security.hardening", "cs_os_security.patch_management"]}],
            "linkedin": [{"signal": "Linux Security endorsement", "strength": 0.3, "maps_to": ["cs_os_security.hardening"]}],
            "assessment": [{"signal": "Can implement MAC and kernel tuning", "strength": 1.0, "maps_to": ["cs_os_security.mac", "cs_os_security.kernel_tuning"]}]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["user_management", "file_permissions", "auditing"], 
                "description": "Can manage basic permissions and read logs.",
                "additional_expectations": "Understands SUID/SGID concepts."
            },
            "mid": {
                "expected_subskills": ["hardening", "patch_management", "mac"], 
                "description": "Can apply CIS benchmarks and manage SELinux/AppArmor.",
                "additional_expectations": "Can troubleshoot SELinux denials."
            },
            "senior": {
                "expected_subskills": ["pam_config", "kernel_tuning", "malware_analysis"], 
                "description": "Deep understanding of kernel security and authentication.",
                "additional_expectations": "Can analyze compromised systems and write custom PAM modules."
            }
        }
    },
    "cs_cryptography": {
        "skill_id": "cs_cryptography",
        "name": "Cryptography",
        "category": "cryptography",
        "description": "Applied cryptography and key management.",
        "subskills": [
            {"id": "symmetric_enc", "name": "Symmetric Encryption", "description": "Block and stream ciphers.", "keywords": ["AES", "ChaCha20", "DES"]},
            {"id": "asymmetric_enc", "name": "Asymmetric Encryption", "description": "Public key cryptography.", "keywords": ["RSA", "ECC", "Diffie-Hellman"]},
            {"id": "hashing", "name": "Hashing Algorithms", "description": "One-way functions.", "keywords": ["SHA-256", "bcrypt", "Argon2"]},
            {"id": "digital_signatures", "name": "Digital Signatures", "description": "Non-repudiation.", "keywords": ["HMAC", "DSA", "signing"]},
            {"id": "tls_ssl", "name": "TLS/SSL", "description": "Transit encryption.", "keywords": ["TLS 1.3", "OpenSSL", "cipher suites"]},
            {"id": "pki", "name": "PKI", "description": "Public Key Infrastructure.", "keywords": ["X.509", "CA", "Let's Encrypt", "CRL", "OCSP"]},
            {"id": "key_management", "name": "Key Lifecycle Management", "description": "Managing secrets.", "keywords": ["KMS", "HashiCorp Vault", "rotation"]},
            {"id": "hsm", "name": "Hardware Security Modules", "description": "Physical key protection.", "keywords": ["HSM", "TPM", "YubiKey"]},
            {"id": "post_quantum", "name": "Post-Quantum Cryptography", "description": "Future-proofing encryption.", "keywords": ["PQC", "Lattice-based", "Kyber"]}
        ],
        "evidence": {
            "github": [{"signal": "TLS configs", "detection": "content_analysis", "pattern": "ssl_protocols TLSv1.2 TLSv1.3", "strength": 0.8, "maps_to": ["cs_cryptography.tls_ssl"]}],
            "cv": [{"signal": "PKI deployment", "strength": 0.8, "maps_to": ["cs_cryptography.pki", "cs_cryptography.key_management"]}],
            "linkedin": [{"signal": "Cryptography", "strength": 0.4, "maps_to": ["cs_cryptography.symmetric_enc", "cs_cryptography.hashing"]}],
            "assessment": [{"signal": "Can design KMS architecture", "strength": 1.0, "maps_to": ["cs_cryptography.key_management", "cs_cryptography.hsm"]}]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["symmetric_enc", "asymmetric_enc", "hashing"], 
                "description": "Understands core cryptographic concepts.",
                "additional_expectations": "Knows when to use hashing vs encryption."
            },
            "mid": {
                "expected_subskills": ["digital_signatures", "tls_ssl", "pki"], 
                "description": "Can configure TLS and manage basic certificates.",
                "additional_expectations": "Can debug TLS handshake failures."
            },
            "senior": {
                "expected_subskills": ["key_management", "hsm", "post_quantum"], 
                "description": "Architects enterprise key management systems.",
                "additional_expectations": "Understands HSM operational requirements and PQC transitions."
            }
        }
    },
    "cs_security_tools": {
        "skill_id": "cs_security_tools",
        "name": "Security Tools",
        "category": "security_tools",
        "description": "Proficiency with offensive and defensive security tooling.",
        "subskills": [
            {"id": "nmap", "name": "Network Scanning (Nmap)", "description": "Port scanning and discovery.", "keywords": ["nmap", "masscan", "port scanning"]},
            {"id": "wireshark", "name": "Traffic Analysis (Wireshark)", "description": "Deep packet inspection.", "keywords": ["wireshark", "tshark", "pcap analysis"]},
            {"id": "vuln_scanners", "name": "Vulnerability Scanners", "description": "Automated scanning.", "keywords": ["Nessus", "OpenVAS", "Qualys", "Tenable"]},
            {"id": "metasploit", "name": "Exploitation Frameworks", "description": "Using frameworks like Metasploit.", "keywords": ["Metasploit", "MSFconsole", "exploit"]},
            {"id": "burp_suite", "name": "Web Proxy (Burp Suite)", "description": "Web app testing.", "keywords": ["Burp Suite", "ZAP", "web proxy"]},
            {"id": "siem_basics", "name": "SIEM Usage", "description": "Querying logs.", "keywords": ["Splunk SPL", "KQL", "Elasticsearch queries"]},
            {"id": "edr", "name": "EDR/XDR", "description": "Endpoint detection.", "keywords": ["CrowdStrike", "Carbon Black", "SentinelOne"]},
            {"id": "siem_arch", "name": "SIEM Architecture", "description": "Designing log ingestion pipelines.", "keywords": ["Logstash", "Fluentd", "SIEM correlation rules"]},
            {"id": "threat_hunting", "name": "Threat Hunting", "description": "Proactive threat detection.", "keywords": ["YARA", "Sigma", "MITRE ATT&CK", "threat hunting"]}
        ],
        "evidence": {
            "github": [{"signal": "Nmap scripts or YARA rules", "detection": "file_presence", "pattern": "*.nse|*.yara|*.sig", "strength": 0.6, "maps_to": ["cs_security_tools.nmap", "cs_security_tools.threat_hunting"]}],
            "cv": [{"signal": "Managed SIEM deployments", "strength": 0.9, "maps_to": ["cs_security_tools.siem_basics", "cs_security_tools.siem_arch"]}],
            "linkedin": [{"signal": "Tool endorsements", "strength": 0.3, "maps_to": ["cs_security_tools.wireshark", "cs_security_tools.vuln_scanners"]}],
            "assessment": [{"signal": "Can write complex YARA and correlation rules", "strength": 1.0, "maps_to": ["cs_security_tools.siem_arch", "cs_security_tools.threat_hunting"]}]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["nmap", "wireshark", "vuln_scanners"], 
                "description": "Can run scans and analyze basic traffic.",
                "additional_expectations": "Can read Nessus reports and verify false positives."
            },
            "mid": {
                "expected_subskills": ["metasploit", "burp_suite", "siem_basics"], 
                "description": "Can perform basic web tests and query SIEMs.",
                "additional_expectations": "Can write basic Splunk/Elastic queries to find events."
            },
            "senior": {
                "expected_subskills": ["edr", "siem_arch", "threat_hunting"], 
                "description": "Architects logging pipelines and hunts threats.",
                "additional_expectations": "Maps defenses to MITRE ATT&CK framework."
            }
        }
    },
    "cs_risk_compliance": {
        "skill_id": "cs_risk_compliance",
        "name": "Risk & Compliance",
        "category": "risk_compliance",
        "description": "Governance, risk management, and compliance frameworks.",
        "subskills": [
            {"id": "risk_assessment", "name": "Risk Assessment", "description": "Identifying risks.", "keywords": ["Risk Matrix", "Likelihood", "Impact"]},
            {"id": "security_policies", "name": "Security Policies", "description": "Drafting policies.", "keywords": ["AUP", "Password Policy", "Incident Response Plan"]},
            {"id": "iso27001", "name": "ISO 27001 Basics", "description": "ISMS framework.", "keywords": ["ISMS", "ISO 27001", "Statement of Applicability"]},
            {"id": "threat_modeling", "name": "Threat Modeling", "description": "Designing secure systems.", "keywords": ["STRIDE", "DREAD", "PASTA"]},
            {"id": "nist_csf", "name": "NIST CSF", "description": "NIST framework.", "keywords": ["NIST", "Identify Protect Detect Respond Recover"]},
            {"id": "data_privacy", "name": "Data Privacy (GDPR/CCPA)", "description": "Privacy regulations.", "keywords": ["GDPR", "CCPA", "DPIA", "PII"]},
            {"id": "soc2", "name": "SOC 2", "description": "Service Organization Control.", "keywords": ["SOC 2 Type II", "Trust Services Criteria", "AICPA"]},
            {"id": "third_party_risk", "name": "Third-Party Risk", "description": "Vendor management.", "keywords": ["Vendor Assessment", "TPRM", "Supply Chain Risk"]},
            {"id": "compliance_automation", "name": "Compliance Automation", "description": "Automating evidence collection.", "keywords": ["Vanta", "Drata", "Compliance as Code"]}
        ],
        "evidence": {
            "github": [{"signal": "Policies in repo", "detection": "file_presence", "pattern": "SECURITY.md|threat-model", "strength": 0.5, "maps_to": ["cs_risk_compliance.security_policies", "cs_risk_compliance.threat_modeling"]}],
            "cv": [{"signal": "Led audits", "strength": 0.9, "maps_to": ["cs_risk_compliance.iso27001", "cs_risk_compliance.soc2"]}],
            "linkedin": [{"signal": "Compliance skills", "strength": 0.4, "maps_to": ["cs_risk_compliance.risk_assessment", "cs_risk_compliance.nist_csf"]}],
            "assessment": [{"signal": "Can build complete ISMS", "strength": 1.0, "maps_to": ["cs_risk_compliance.iso27001", "cs_risk_compliance.soc2", "cs_risk_compliance.third_party_risk"]}]
        },
        "levels": {
            "junior": {
                "expected_subskills": ["risk_assessment", "security_policies", "iso27001"], 
                "description": "Understands basic risk concepts and policies.",
                "additional_expectations": "Can assist in policy drafting and evidence gathering."
            },
            "mid": {
                "expected_subskills": ["threat_modeling", "nist_csf", "data_privacy"], 
                "description": "Applies frameworks and models threats.",
                "additional_expectations": "Can run a STRIDE threat modeling session."
            },
            "senior": {
                "expected_subskills": ["soc2", "third_party_risk", "compliance_automation"], 
                "description": "Leads audit programs and automates compliance.",
                "additional_expectations": "Successfully guided an organization through SOC2 Type II."
            }
        }
    }
}

for k, v in skills_data.items():
    with open(os.path.join(skills_dir, f"{k}.json"), "w") as f:
        json.dump(v, f, indent=2)

# 4. Evidence Files - Mirroring DevOps EXACTLY
evidence_data = {
    "cv": {
        "source_id": "cv",
        "name": "CV / Resume Analysis - Cyber Security",
        "description": "Signals extracted from the user's CV/resume to evidence Cyber Security skills.",
        "extraction_rules": {
            "description": "How to extract and weight information from CV content.",
            "sections": [
                {
                    "section": "skills_list",
                    "description": "Explicit list of technologies and tools mentioned in skills section.",
                    "base_strength": 0.3,
                    "notes": "Low strength because listing a skill doesn't prove proficiency."
                },
                {
                    "section": "work_experience",
                    "description": "Job descriptions and responsibilities mentioning security activities.",
                    "base_strength": 0.5,
                    "notes": "Higher strength when specific actions and outcomes are described.",
                    "quality_indicators": [
                        "Specific tools and technologies mentioned in context",
                        "Quantifiable outcomes (resolved X incidents, passed Y audits)",
                        "Action verbs indicating hands-on work (secured, analyzed, implemented, audited)",
                        "Duration and recency of experience"
                    ]
                },
                {
                    "section": "projects",
                    "description": "Personal or academic projects demonstrating security skills.",
                    "base_strength": 0.4,
                    "notes": "Higher strength if linked to GitHub repository or CVEs."
                },
                {
                    "section": "education",
                    "description": "Relevant courses, degrees, and academic background.",
                    "base_strength": 0.2
                },
                {
                    "section": "certifications",
                    "description": "Professional certifications (CISSP, CEH, OSCP, etc.).",
                    "base_strength": 0.2,
                    "notes": "Certifications alone are NOT evidence of practical skill. They indicate theoretical knowledge.",
                    "recognized_certifications": {
                        "networking": ["CCNA", "Network+"],
                        "security_general": ["Security+", "CISSP", "CISM"],
                        "offensive": ["OSCP", "CEH", "PNPT"],
                        "defensive": ["BTL1", "CySA+"],
                        "compliance": ["CISA", "CRISC"]
                    }
                }
            ]
        },
        "signal_mapping": {
            "description": "How CV mentions map to skill evidence using COMPOSITE KEYS ({skill_id}.{subskill_id}).",
            "patterns": [
                {
                    "pattern": "Mentions configuring Palo Alto or Fortinet firewalls in production",
                    "maps_to": ["cs_networking.firewalls"],
                    "strength_modifier": 1.0
                },
                {
                    "pattern": "Lists Wireshark or Nmap in skills section only",
                    "maps_to": ["cs_security_tools.wireshark", "cs_security_tools.nmap"],
                    "strength_modifier": 0.5
                },
                {
                    "pattern": "Describes leading a SOC2 or ISO27001 audit to successful certification",
                    "maps_to": ["cs_risk_compliance.soc2", "cs_risk_compliance.iso27001", "cs_risk_compliance.compliance_automation"],
                    "strength_modifier": 1.2
                },
                {
                    "pattern": "Has OSCP certification",
                    "maps_to": ["cs_security_tools.nmap", "cs_security_tools.metasploit", "cs_security_tools.burp_suite"],
                    "strength_modifier": 1.0
                }
            ]
        },
        "important_notes": [
            "CV data is self-reported and inherently unreliable as standalone evidence",
            "Always cross-validate CV claims with GitHub and LinkedIn data"
        ]
    },
    "linkedin": {
        "source_id": "linkedin",
        "name": "LinkedIn Profile Analysis - Cyber Security",
        "description": "Signals extracted from LinkedIn profiles to evidence Cyber Security skills.",
        "extraction_rules": {
            "sections": [
                {"section": "headline_summary", "description": "Profile headline and summary/about section.", "base_strength": 0.2},
                {
                    "section": "experience",
                    "description": "Work experience entries with job titles, companies, and descriptions.",
                    "base_strength": 0.4,
                    "quality_indicators": [
                        "Security-related job titles (Security Analyst, Penetration Tester, CISO)",
                        "Duration in security roles",
                        "Specific technology mentions in descriptions"
                    ]
                },
                {"section": "skills_endorsements", "description": "Skills listed with endorsement counts from connections.", "base_strength": 0.15},
                {"section": "certifications", "description": "Professional certifications with issuing organizations.", "base_strength": 0.2},
                {"section": "projects", "description": "Projects section with descriptions and links.", "base_strength": 0.3},
                {"section": "recommendations", "description": "Written recommendations from colleagues or managers.", "base_strength": 0.3},
                {"section": "posts_articles", "description": "Technical posts and articles published on LinkedIn.", "base_strength": 0.3}
            ]
        },
        "signal_mapping": {
            "description": "How LinkedIn mentions map to skill evidence using COMPOSITE KEYS.",
            "patterns": [
                {
                    "pattern": "LinkedIn skills endorsement for 'Network Security' or 'Firewalls'",
                    "maps_to": ["cs_networking.firewalls"],
                    "strength_modifier": 0.33
                },
                {
                    "pattern": "Job experience explicitly describing building SIEM correlation rules",
                    "maps_to": ["cs_security_tools.siem_arch", "cs_security_tools.threat_hunting"],
                    "strength_modifier": 1.0
                },
                {
                    "pattern": "Job experience mentioning implementation of Zero Trust",
                    "maps_to": ["cs_networking.zero_trust", "cs_networking.network_segmentation"],
                    "strength_modifier": 1.0
                }
            ]
        },
        "important_notes": [
            "ALL extracted signals MUST be mapped to COMPOSITE KEYS ({skill_id}.{subskill_id})"
        ]
    },
    "assessment": {
        "source_id": "assessment",
        "name": "Adaptive Technical Assessment - Cyber Security",
        "description": "Adaptive technical questions and practical tasks used to verify skills.",
        "trigger_conditions": {
            "rules": [
                "When a subskill has status 'not_yet_evidenced' (confidence = 0.0) for a required role skill",
                "When a subskill has status 'insufficient_evidence' and confidence < 0.4"
            ]
        },
        "question_types": [
            {"type": "conceptual", "strength": 0.6},
            {"type": "scenario", "strength": 0.8},
            {"type": "practical_task", "strength": 1.0}
        ],
        "adaptive_logic": {
            "rules": [
                "Start with a conceptual question for the target subskill",
                "If answered correctly, escalate to a scenario question"
            ]
        },
        "sample_questions_by_composite_key": {
            "cs_networking.firewalls": [
                {
                    "level": "mid",
                    "type": "scenario",
                    "question": "A user complains they cannot reach a server on port 443. Walk through how you would troubleshoot this on a Palo Alto firewall.",
                    "expected_answer_keywords": ["traffic logs", "security policy", "NAT", "packet capture"]
                }
            ],
            "cs_cryptography.tls_ssl": [
                {
                    "level": "mid",
                    "type": "conceptual",
                    "question": "What is the difference between symmetric and asymmetric encryption in a TLS handshake?",
                    "expected_answer_keywords": ["asymmetric for key exchange", "symmetric for data transfer", "performance"]
                }
            ]
        },
        "scoring_rules_reference": {
            "source": "knowledge-base/scoring/engine.json",
            "description": "Scoring rules for assessment are defined in engine.json"
        }
    },
    "github": {
        "source_id": "github",
        "name": "GitHub Repository Analysis - Cyber Security",
        "description": "Signals extracted from GitHub repositories to evidence Cyber Security skills.",
        "preprocessing_pipeline": {
            "steps": [
                {
                    "step": 1,
                    "name": "file_tree_scan",
                    "target_files": [
                        {"pattern": "iptables.rules|openvpn.conf", "skill": "cs_networking", "priority": "high"},
                        {"pattern": "SELINUX=enforcing|auditd", "skill": "cs_os_security", "priority": "high"},
                        {"pattern": "ssl_certificate|ssl_protocols", "skill": "cs_cryptography", "priority": "high"},
                        {"pattern": "*.nse|*.pcap|*.yara", "skill": "cs_security_tools", "priority": "medium"},
                        {"pattern": "SECURITY.md|threat-model.md", "skill": "cs_risk_compliance", "priority": "low"}
                    ]
                }
            ]
        },
        "ai_analysis_instructions": {
            "tasks": ["Map identified files and patterns to specific subskills using COMPOSITE KEYS."],
            "output_format": {
                "composite_key_example": "cs_networking.firewalls"
            }
        }
    }
}

for k, v in evidence_data.items():
    with open(os.path.join(evidence_dir, f"{k}.json"), "w") as f:
        json.dump(v, f, indent=2)

print("All Cyber Security KB files generated correctly.")
