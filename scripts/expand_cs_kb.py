import os
import json
import shutil

base_dir = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base"
skills_dir = os.path.join(base_dir, "skills", "cyber-security")
evidence_dir = os.path.join(base_dir, "evidence", "cyber-security")
roles_dir = os.path.join(base_dir, "roles", "cyber-security")

# Remove old files if they exist to avoid orphans
for old_file in ["cs_os_security.json", "cs_risk_compliance.json"]:
    p = os.path.join(skills_dir, old_file)
    if os.path.exists(p):
        os.remove(p)

# 1. 11 Skills Data
skills_data = {
    # Existing / Renamed Skills
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
            "junior": {"expected_subskills": ["tcp_ip", "subnetting", "packet_analysis"], "description": "Understands network protocols and can analyze basic traffic."},
            "mid": {"expected_subskills": ["firewalls", "ids_ips", "vpns"], "description": "Can manage security boundaries and secure tunnels."},
            "senior": {"expected_subskills": ["network_segmentation", "zero_trust", "ddos_mitigation"], "description": "Designs enterprise network security architectures.", "additional_expectations": ["Can architect a complete zero-trust migration."]}
        }
    },
    "cs_operating_systems": {
        "skill_id": "cs_operating_systems",
        "name": "Operating Systems",
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
            "github": [{"signal": "Hardening scripts", "detection": "content_analysis", "pattern": "SELINUX=enforcing|auditd", "strength": 0.8, "maps_to": ["cs_operating_systems.mac", "cs_operating_systems.auditing"]}],
            "cv": [{"signal": "Linux hardening experience", "strength": 0.7, "maps_to": ["cs_operating_systems.hardening", "cs_operating_systems.patch_management"]}],
            "linkedin": [{"signal": "Linux Security endorsement", "strength": 0.3, "maps_to": ["cs_operating_systems.hardening"]}],
            "assessment": [{"signal": "Can implement MAC and kernel tuning", "strength": 1.0, "maps_to": ["cs_operating_systems.mac", "cs_operating_systems.kernel_tuning"]}]
        },
        "levels": {
            "junior": {"expected_subskills": ["user_management", "file_permissions", "auditing"], "description": "Can manage basic permissions and read logs."},
            "mid": {"expected_subskills": ["hardening", "patch_management", "mac"], "description": "Can apply CIS benchmarks and manage SELinux/AppArmor."},
            "senior": {"expected_subskills": ["pam_config", "kernel_tuning", "malware_analysis"], "description": "Deep understanding of kernel security and authentication.", "additional_expectations": ["Can analyze compromised systems and write custom PAM modules."]}
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
            "junior": {"expected_subskills": ["symmetric_enc", "asymmetric_enc", "hashing"], "description": "Understands core cryptographic concepts."},
            "mid": {"expected_subskills": ["digital_signatures", "tls_ssl", "pki"], "description": "Can configure TLS and manage basic certificates."},
            "senior": {"expected_subskills": ["key_management", "hsm", "post_quantum"], "description": "Architects enterprise key management systems.", "additional_expectations": ["Understands HSM operational requirements and PQC transitions."]}
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
            "junior": {"expected_subskills": ["nmap", "wireshark", "vuln_scanners"], "description": "Can run scans and analyze basic traffic."},
            "mid": {"expected_subskills": ["metasploit", "burp_suite", "siem_basics"], "description": "Can perform basic web tests and query SIEMs."},
            "senior": {"expected_subskills": ["edr", "siem_arch", "threat_hunting"], "description": "Architects logging pipelines and hunts threats.", "additional_expectations": ["Maps defenses to MITRE ATT&CK framework."]}
        }
    },
    "cs_frameworks_compliance": {
        "skill_id": "cs_frameworks_compliance",
        "name": "Frameworks & Compliance",
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
            "github": [{"signal": "Policies in repo", "detection": "file_presence", "pattern": "SECURITY.md|threat-model", "strength": 0.5, "maps_to": ["cs_frameworks_compliance.security_policies", "cs_frameworks_compliance.threat_modeling"]}],
            "cv": [{"signal": "Led audits", "strength": 0.9, "maps_to": ["cs_frameworks_compliance.iso27001", "cs_frameworks_compliance.soc2"]}],
            "linkedin": [{"signal": "Compliance skills", "strength": 0.4, "maps_to": ["cs_frameworks_compliance.risk_assessment", "cs_frameworks_compliance.nist_csf"]}],
            "assessment": [{"signal": "Can build complete ISMS", "strength": 1.0, "maps_to": ["cs_frameworks_compliance.iso27001", "cs_frameworks_compliance.soc2", "cs_frameworks_compliance.third_party_risk"]}]
        },
        "levels": {
            "junior": {"expected_subskills": ["risk_assessment", "security_policies", "iso27001"], "description": "Understands basic risk concepts and policies."},
            "mid": {"expected_subskills": ["threat_modeling", "nist_csf", "data_privacy"], "description": "Applies frameworks and models threats."},
            "senior": {"expected_subskills": ["soc2", "third_party_risk", "compliance_automation"], "description": "Leads audit programs and automates compliance.", "additional_expectations": ["Successfully guided an organization through SOC2 Type II."]}
        }
    },
    
    # New Skills (6)
    "cs_security_fundamentals": {
        "skill_id": "cs_security_fundamentals",
        "name": "Security Fundamentals",
        "category": "fundamentals",
        "description": "Core cybersecurity concepts including CIA Triad, Defense in Depth, and Zero Trust.",
        "subskills": [
            {"id": "cia_triad", "name": "CIA Triad", "description": "Confidentiality, Integrity, Availability.", "keywords": ["CIA", "Confidentiality", "Integrity", "Availability"]},
            {"id": "auth_vs_authz", "name": "Auth vs AuthZ", "description": "Authentication vs Authorization.", "keywords": ["Authentication", "Authorization", "RBAC", "ABAC", "OAuth", "SAML"]},
            {"id": "mfa_2fa", "name": "MFA/2FA", "description": "Multi-factor authentication concepts.", "keywords": ["MFA", "2FA", "TOTP", "WebAuthn"]},
            {"id": "defense_in_depth", "name": "Defense in Depth", "description": "Layered security approach.", "keywords": ["Defense in Depth", "Layered Security", "Onion model"]},
            {"id": "risk_concepts", "name": "Risk Concepts", "description": "Understanding vulnerabilities and threats.", "keywords": ["Risk", "Threat", "Vulnerability", "Exploit"]},
            {"id": "isolation", "name": "Isolation", "description": "Separation of duties and resources.", "keywords": ["Isolation", "Sandboxing", "Separation of Duties"]},
            {"id": "red_blue_purple", "name": "Red/Blue/Purple Teams", "description": "Security team methodologies.", "keywords": ["Red Team", "Blue Team", "Purple Team", "Adversary emulation"]},
            {"id": "zero_trust", "name": "Zero Trust Concepts", "description": "Never trust, always verify.", "keywords": ["Zero Trust", "BeyondCorp", "Continuous Verification"]}
        ],
        "evidence": {
            "github": [{"signal": "MFA or Auth config", "detection": "content_analysis", "pattern": "mfa_required|oauth|saml", "strength": 0.6, "maps_to": ["cs_security_fundamentals.auth_vs_authz", "cs_security_fundamentals.mfa_2fa"]}],
            "cv": [{"signal": "Implemented Zero Trust", "strength": 0.8, "maps_to": ["cs_security_fundamentals.zero_trust", "cs_security_fundamentals.defense_in_depth"]}],
            "linkedin": [{"signal": "Red Teaming", "strength": 0.4, "maps_to": ["cs_security_fundamentals.red_blue_purple"]}],
            "assessment": [{"signal": "Can architect Defense in Depth", "strength": 1.0, "maps_to": ["cs_security_fundamentals.defense_in_depth", "cs_security_fundamentals.zero_trust", "cs_security_fundamentals.isolation"]}]
        },
        "levels": {
            "junior": {"expected_subskills": ["cia_triad", "auth_vs_authz", "mfa_2fa"], "description": "Understands basic security principles."},
            "mid": {"expected_subskills": ["defense_in_depth", "risk_concepts", "isolation"], "description": "Applies layered security principles."},
            "senior": {"expected_subskills": ["zero_trust", "red_blue_purple"], "description": "Architects modern trust models.", "additional_expectations": ["Can lead Purple Team exercises."]}
        }
    },
    "cs_threats_and_attacks": {
        "skill_id": "cs_threats_and_attacks",
        "name": "Threats and Attacks",
        "category": "threats",
        "description": "Knowledge of various attack vectors, OWASP Top 10, and malware types.",
        "subskills": [
            {"id": "social_engineering", "name": "Social Engineering", "description": "Phishing, vishing, smishing.", "keywords": ["Phishing", "Vishing", "Whaling", "Baiting"]},
            {"id": "malware_types", "name": "Malware Types", "description": "Ransomware, trojans, worms.", "keywords": ["Ransomware", "Trojan", "Worm", "Rootkit", "Spyware"]},
            {"id": "spoofing", "name": "Spoofing", "description": "IP, ARP, DNS spoofing.", "keywords": ["ARP Spoofing", "DNS Spoofing", "IP Spoofing"]},
            {"id": "owasp_top_10", "name": "OWASP Top 10", "description": "Standard web app vulnerabilities.", "keywords": ["OWASP", "Injection", "Broken Authentication", "Sensitive Data Exposure"]},
            {"id": "sql_injection", "name": "SQL Injection", "description": "Database injection attacks.", "keywords": ["SQLi", "Blind SQLi", "Time-based SQLi"]},
            {"id": "xss_csrf", "name": "XSS & CSRF", "description": "Cross-site scripting and request forgery.", "keywords": ["XSS", "CSRF", "Reflected XSS", "Stored XSS"]},
            {"id": "dos_ddos", "name": "DoS/DDoS/MITM", "description": "Denial of service and interception.", "keywords": ["DDoS", "Botnet", "MITM", "Amplification Attack"]},
            {"id": "buffer_overflow", "name": "Buffer Overflow", "description": "Memory corruption attacks.", "keywords": ["Buffer Overflow", "Stack Smashing", "Heap Spraying"]},
            {"id": "priv_escalation", "name": "Privilege Escalation", "description": "Gaining higher privileges.", "keywords": ["Privilege Escalation", "Vertical Escalation", "Horizontal Escalation"]}
        ],
        "evidence": {
            "github": [{"signal": "Input validation or parameterized queries", "detection": "content_analysis", "pattern": "execute_prepared|xss_clean|htmlentities", "strength": 0.6, "maps_to": ["cs_threats_and_attacks.sql_injection", "cs_threats_and_attacks.xss_csrf"]}],
            "cv": [{"signal": "Penetration testing or bug bounty", "strength": 0.8, "maps_to": ["cs_threats_and_attacks.owasp_top_10", "cs_threats_and_attacks.priv_escalation"]}],
            "linkedin": [{"signal": "Web Application Security", "strength": 0.4, "maps_to": ["cs_threats_and_attacks.owasp_top_10", "cs_threats_and_attacks.xss_csrf"]}],
            "assessment": [{"signal": "Can perform advanced privilege escalation", "strength": 1.0, "maps_to": ["cs_threats_and_attacks.priv_escalation", "cs_threats_and_attacks.buffer_overflow", "cs_threats_and_attacks.dos_ddos"]}]
        },
        "levels": {
            "junior": {"expected_subskills": ["social_engineering", "malware_types", "spoofing"], "description": "Understands common attack vectors."},
            "mid": {"expected_subskills": ["owasp_top_10", "sql_injection", "xss_csrf"], "description": "Can identify and mitigate web vulnerabilities."},
            "senior": {"expected_subskills": ["dos_ddos", "buffer_overflow", "priv_escalation"], "description": "Understands complex systemic and memory-based attacks.", "additional_expectations": ["Can reverse-engineer simple buffer overflows."]}
        }
    },
    "cs_incident_response_forensics": {
        "skill_id": "cs_incident_response_forensics",
        "name": "Incident Response & Forensics",
        "category": "operations",
        "description": "Managing security incidents and performing digital forensics.",
        "subskills": [
            {"id": "ir_preparation", "name": "IR Preparation", "description": "Planning for incidents.", "keywords": ["IR Plan", "Playbooks", "Tabletop Exercise"]},
            {"id": "forensics_basics", "name": "Forensics Basics", "description": "Principles of digital forensics.", "keywords": ["Digital Forensics", "Disk Image", "Hash Verification"]},
            {"id": "chain_of_custody", "name": "Chain of Custody", "description": "Legal evidence handling.", "keywords": ["Chain of Custody", "Evidence Preservation"]},
            {"id": "ir_identification", "name": "IR Identification", "description": "Detecting incidents.", "keywords": ["Triage", "IOCs", "Alert Verification"]},
            {"id": "forensic_tools", "name": "Forensic Tools", "description": "Using FTK Imager, Autopsy, WinHex.", "keywords": ["FTK Imager", "Autopsy", "WinHex", "Sleuth Kit"]},
            {"id": "root_cause_analysis", "name": "Root Cause Analysis", "description": "Finding the origin of an incident.", "keywords": ["RCA", "Lessons Learned", "Post-mortem"]},
            {"id": "ir_containment", "name": "IR Containment & Eradication", "description": "Stopping the spread.", "keywords": ["Containment", "Eradication", "Quarantine"]},
            {"id": "threat_hunting", "name": "Threat Hunting", "description": "Proactive searching for IOCs.", "keywords": ["Threat Hunting", "Hypothesis-driven", "Beaconing analysis"]},
            {"id": "memory_analysis", "name": "Memory Analysis", "description": "Analyzing RAM dumps.", "keywords": ["Volatility", "memdump", "RAM forensics"]}
        ],
        "evidence": {
            "github": [{"signal": "IR Playbooks or scripts", "detection": "file_presence", "pattern": "playbook|ir-script", "strength": 0.6, "maps_to": ["cs_incident_response_forensics.ir_preparation", "cs_incident_response_forensics.ir_identification"]}],
            "cv": [{"signal": "Led incident response team", "strength": 0.9, "maps_to": ["cs_incident_response_forensics.ir_containment", "cs_incident_response_forensics.root_cause_analysis"]}],
            "linkedin": [{"signal": "Digital Forensics", "strength": 0.4, "maps_to": ["cs_incident_response_forensics.forensics_basics", "cs_incident_response_forensics.forensic_tools"]}],
            "assessment": [{"signal": "Can perform complete memory analysis", "strength": 1.0, "maps_to": ["cs_incident_response_forensics.memory_analysis", "cs_incident_response_forensics.threat_hunting", "cs_incident_response_forensics.forensic_tools"]}]
        },
        "levels": {
            "junior": {"expected_subskills": ["ir_preparation", "forensics_basics", "chain_of_custody"], "description": "Understands IR processes and basic evidence handling."},
            "mid": {"expected_subskills": ["ir_identification", "forensic_tools", "root_cause_analysis"], "description": "Can triage alerts and use forensic tools."},
            "senior": {"expected_subskills": ["ir_containment", "threat_hunting", "memory_analysis"], "description": "Leads major incidents and performs deep memory forensics.", "additional_expectations": ["Can reverse-engineer in-memory malware artifacts."]}
        }
    },
    "cs_hardening_defense": {
        "skill_id": "cs_hardening_defense",
        "name": "Hardening & Defense",
        "category": "operations",
        "description": "Securing infrastructure through hardening, IDPs, and endpoint security.",
        "subskills": [
            {"id": "os_hardening", "name": "OS Hardening", "description": "Applying security baselines.", "keywords": ["OS Hardening", "CIS", "STIG", "GPO"]},
            {"id": "acls", "name": "ACLs", "description": "Access Control Lists.", "keywords": ["ACL", "Firewall Rules", "Network ACLs"]},
            {"id": "secure_protocols", "name": "Secure Protocols", "description": "Using SFTP, TLS over insecure ones.", "keywords": ["SFTP", "SSH", "TLS", "HTTPS"]},
            {"id": "ids_ips", "name": "IDS/IPS Deployment", "description": "Network intrusion systems.", "keywords": ["IDS", "IPS", "NIDS", "HIDS"]},
            {"id": "endpoint_security", "name": "EDR/DLP/AV", "description": "Endpoint defense.", "keywords": ["EDR", "DLP", "Antivirus", "Antimalware"]},
            {"id": "jump_servers", "name": "Jump Servers & Bastion", "description": "Secure administrative access.", "keywords": ["Jump Server", "Bastion Host", "PAM"]},
            {"id": "honeypots", "name": "Honeypots", "description": "Deception technology.", "keywords": ["Honeypot", "Honeynet", "Tarpit"]},
            {"id": "nac_mac", "name": "NAC/MAC-based Control", "description": "Network Access Control.", "keywords": ["NAC", "802.1X", "MAC Filtering"]},
            {"id": "sinkholes", "name": "DNS Sinkholing", "description": "Redirecting malicious traffic.", "keywords": ["DNS Sinkhole", "Pi-hole", "Malware C2 blocking"]}
        ],
        "evidence": {
            "github": [{"signal": "Bastion host or ACL IaC", "detection": "content_analysis", "pattern": "bastion|network_acl", "strength": 0.7, "maps_to": ["cs_hardening_defense.jump_servers", "cs_hardening_defense.acls"]}],
            "cv": [{"signal": "Deployed EDR or NAC", "strength": 0.8, "maps_to": ["cs_hardening_defense.endpoint_security", "cs_hardening_defense.nac_mac"]}],
            "linkedin": [{"signal": "Infrastructure Security", "strength": 0.4, "maps_to": ["cs_hardening_defense.os_hardening", "cs_hardening_defense.secure_protocols"]}],
            "assessment": [{"signal": "Can architect complex deception networks", "strength": 1.0, "maps_to": ["cs_hardening_defense.honeypots", "cs_hardening_defense.sinkholes", "cs_hardening_defense.ids_ips"]}]
        },
        "levels": {
            "junior": {"expected_subskills": ["os_hardening", "acls", "secure_protocols"], "description": "Can apply basic hardening and access controls."},
            "mid": {"expected_subskills": ["ids_ips", "endpoint_security", "jump_servers"], "description": "Manages endpoint defenses and secure access points."},
            "senior": {"expected_subskills": ["honeypots", "nac_mac", "sinkholes"], "description": "Implements advanced network defenses and deception.", "additional_expectations": ["Can design a comprehensive deception technology strategy."]}
        }
    },
    "cs_cloud_security": {
        "skill_id": "cs_cloud_security",
        "name": "Cloud Security",
        "category": "cloud",
        "description": "Securing cloud environments, SaaS/PaaS/IaaS, and Serverless.",
        "subskills": [
            {"id": "cloud_concepts", "name": "Cloud Security Concepts", "description": "Shared responsibility model.", "keywords": ["Shared Responsibility Model", "Cloud Security", "Multi-tenant"]},
            {"id": "cloud_models", "name": "Cloud Models", "description": "Private, Public, Hybrid.", "keywords": ["Private Cloud", "Public Cloud", "Hybrid Cloud"]},
            {"id": "saas_paas_iaas", "name": "SaaS/PaaS/IaaS", "description": "Service models.", "keywords": ["SaaS", "PaaS", "IaaS"]},
            {"id": "aws_security", "name": "AWS Security", "description": "AWS specific security.", "keywords": ["IAM", "Security Groups", "GuardDuty", "CloudTrail"]},
            {"id": "azure_security", "name": "Azure Security", "description": "Azure specific security.", "keywords": ["Azure AD", "NSG", "Azure Security Center"]},
            {"id": "gcp_security", "name": "GCP Security", "description": "GCP specific security.", "keywords": ["Cloud IAM", "VPC Service Controls", "Security Command Center"]},
            {"id": "iac_security", "name": "IaC Security", "description": "Securing Infrastructure as Code.", "keywords": ["Terraform security", "cfn-nag", "checkov", "tfsec"]},
            {"id": "serverless_security", "name": "Serverless Security", "description": "Securing Lambda/Functions.", "keywords": ["Serverless", "AWS Lambda", "Azure Functions"]},
            {"id": "cspm", "name": "CSPM", "description": "Cloud Security Posture Management.", "keywords": ["CSPM", "Prisma Cloud", "Wiz", "CWPP"]}
        ],
        "evidence": {
            "github": [{"signal": "IaC security scanning in CI", "detection": "content_analysis", "pattern": "checkov|tfsec", "strength": 0.8, "maps_to": ["cs_cloud_security.iac_security"]}],
            "cv": [{"signal": "Managed AWS/Azure security", "strength": 0.8, "maps_to": ["cs_cloud_security.aws_security", "cs_cloud_security.azure_security"]}],
            "linkedin": [{"signal": "Cloud Security", "strength": 0.4, "maps_to": ["cs_cloud_security.cloud_concepts", "cs_cloud_security.saas_paas_iaas"]}],
            "assessment": [{"signal": "Can design CSPM and Serverless security", "strength": 1.0, "maps_to": ["cs_cloud_security.cspm", "cs_cloud_security.serverless_security", "cs_cloud_security.iac_security"]}]
        },
        "levels": {
            "junior": {"expected_subskills": ["cloud_concepts", "cloud_models", "saas_paas_iaas"], "description": "Understands cloud service models and shared responsibility."},
            "mid": {"expected_subskills": ["aws_security", "azure_security", "gcp_security"], "description": "Can secure major cloud provider environments."},
            "senior": {"expected_subskills": ["iac_security", "serverless_security", "cspm"], "description": "Architects automated cloud security and posture management.", "additional_expectations": ["Can enforce security-as-code across a multi-cloud environment."]}
        }
    },
    "cs_programming_scripting": {
        "skill_id": "cs_programming_scripting",
        "name": "Programming & Scripting",
        "category": "development",
        "description": "Scripting for security automation and understanding secure coding.",
        "subskills": [
            {"id": "bash_scripting", "name": "Bash Scripting", "description": "Shell scripting for automation.", "keywords": ["bash", "shell", "awk", "sed"]},
            {"id": "powershell", "name": "PowerShell", "description": "Windows automation.", "keywords": ["PowerShell", "PS1", "cmdlet"]},
            {"id": "js_security", "name": "JavaScript Security", "description": "Understanding JS vulnerabilities.", "keywords": ["JavaScript", "Node.js", "DOM XSS"]},
            {"id": "python_scripting", "name": "Python Scripting", "description": "Python for security tooling.", "keywords": ["Python", "boto3", "requests", "scapy"]},
            {"id": "api_security", "name": "API Security", "description": "Securing REST/GraphQL APIs.", "keywords": ["REST", "GraphQL", "JWT", "API Gateway"]},
            {"id": "secure_coding", "name": "Secure Coding Practices", "description": "Writing secure applications.", "keywords": ["Secure SDLC", "Input Validation", "Output Encoding"]},
            {"id": "go_programming", "name": "Go Programming", "description": "Go for security tooling.", "keywords": ["Golang", "Go", "concurrency"]},
            {"id": "cpp_programming", "name": "C/C++ Programming", "description": "Low level memory analysis.", "keywords": ["C++", "C", "pointers", "memory management"]},
            {"id": "security_automation", "name": "Security Automation", "description": "SOAR and pipeline automation.", "keywords": ["SOAR", "Security Automation", "CI/CD Security"]}
        ],
        "evidence": {
            "github": [{"signal": "Python or Bash scripts in repo", "detection": "file_presence", "pattern": "*.py|*.sh", "strength": 0.6, "maps_to": ["cs_programming_scripting.python_scripting", "cs_programming_scripting.bash_scripting"]}],
            "cv": [{"signal": "Built security automation tools", "strength": 0.8, "maps_to": ["cs_programming_scripting.security_automation", "cs_programming_scripting.python_scripting"]}],
            "linkedin": [{"signal": "Scripting or Secure Coding", "strength": 0.4, "maps_to": ["cs_programming_scripting.secure_coding", "cs_programming_scripting.bash_scripting"]}],
            "assessment": [{"signal": "Can write C/C++ memory exploits or complex Go tooling", "strength": 1.0, "maps_to": ["cs_programming_scripting.cpp_programming", "cs_programming_scripting.go_programming", "cs_programming_scripting.security_automation"]}]
        },
        "levels": {
            "junior": {"expected_subskills": ["bash_scripting", "powershell", "js_security"], "description": "Can write basic shell scripts and understand JS concepts."},
            "mid": {"expected_subskills": ["python_scripting", "api_security", "secure_coding"], "description": "Can write Python tools and secure APIs."},
            "senior": {"expected_subskills": ["go_programming", "cpp_programming", "security_automation"], "description": "Develops advanced security tooling and fully automates security processes.", "additional_expectations": ["Can audit low-level C++ code for memory safety."]}
        }
    }
}

for k, v in skills_data.items():
    with open(os.path.join(skills_dir, f"{k}.json"), "w") as f:
        json.dump(v, f, indent=2)

# 2. Roles Data
roles_data = {
    "junior": {
        "role_id": "cyber_security",
        "level": "junior",
        "title": "Junior Cyber Security Analyst",
        "description": "Entry-level security position focused on foundational concepts, OS security, and basic tool usage.",
        "experience_range": "0-2 years",
        "skills": [
            {"skill_id": "cs_networking", "importance": 0.95, "rationale": "Foundation for all security work"},
            {"skill_id": "cs_operating_systems", "importance": 0.90, "rationale": "Daily interaction with OS permissions"},
            {"skill_id": "cs_security_tools", "importance": 0.85, "rationale": "Must use basic scanners"},
            {"skill_id": "cs_security_fundamentals", "importance": 0.95, "rationale": "CIA triad and basic concepts are critical"},
            {"skill_id": "cs_threats_and_attacks", "importance": 0.80, "rationale": "Understanding how attacks work"},
            {"skill_id": "cs_incident_response_forensics", "importance": 0.60, "rationale": "Awareness of incident processes"},
            {"skill_id": "cs_hardening_defense", "importance": 0.70, "rationale": "Basic hardening knowledge"},
            {"skill_id": "cs_cloud_security", "importance": 0.60, "rationale": "Cloud concepts awareness"},
            {"skill_id": "cs_programming_scripting", "importance": 0.60, "rationale": "Basic shell scripting required"},
            {"skill_id": "cs_cryptography", "importance": 0.60, "rationale": "Basic hashing/encryption concepts"},
            {"skill_id": "cs_frameworks_compliance", "importance": 0.50, "rationale": "Awareness of policies"}
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
        "description": "Mid-level position requiring hands-on implementation across multiple domains.",
        "experience_range": "3-5 years",
        "skills": [
            {"skill_id": "cs_networking", "importance": 0.85, "rationale": "Configuring VPNs and firewalls"},
            {"skill_id": "cs_operating_systems", "importance": 0.85, "rationale": "Advanced hardening"},
            {"skill_id": "cs_security_tools", "importance": 0.90, "rationale": "Proficient use of SIEM"},
            {"skill_id": "cs_security_fundamentals", "importance": 0.80, "rationale": "Applying defense in depth"},
            {"skill_id": "cs_threats_and_attacks", "importance": 0.85, "rationale": "Identifying vulnerabilities"},
            {"skill_id": "cs_incident_response_forensics", "importance": 0.80, "rationale": "Triaging and using forensic tools"},
            {"skill_id": "cs_hardening_defense", "importance": 0.85, "rationale": "Managing endpoint defenses"},
            {"skill_id": "cs_cloud_security", "importance": 0.80, "rationale": "Securing cloud environments"},
            {"skill_id": "cs_programming_scripting", "importance": 0.75, "rationale": "Writing Python tools"},
            {"skill_id": "cs_cryptography", "importance": 0.75, "rationale": "Managing certificates"},
            {"skill_id": "cs_frameworks_compliance", "importance": 0.70, "rationale": "Conducting threat models"}
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
            {"skill_id": "cs_networking", "importance": 0.90, "rationale": "Designing zero-trust network segmentation"},
            {"skill_id": "cs_operating_systems", "importance": 0.80, "rationale": "Enterprise IAM and kernel-level security"},
            {"skill_id": "cs_security_tools", "importance": 0.85, "rationale": "Architecting SIEM solutions"},
            {"skill_id": "cs_security_fundamentals", "importance": 0.95, "rationale": "Architecting zero trust models"},
            {"skill_id": "cs_threats_and_attacks", "importance": 0.80, "rationale": "Understanding complex systemic attacks"},
            {"skill_id": "cs_incident_response_forensics", "importance": 0.90, "rationale": "Leading major incident response"},
            {"skill_id": "cs_hardening_defense", "importance": 0.90, "rationale": "Implementing advanced deception"},
            {"skill_id": "cs_cloud_security", "importance": 0.95, "rationale": "Enforcing security as code across multi-cloud"},
            {"skill_id": "cs_programming_scripting", "importance": 0.80, "rationale": "Developing advanced security tooling"},
            {"skill_id": "cs_cryptography", "importance": 0.85, "rationale": "Enterprise key management"},
            {"skill_id": "cs_frameworks_compliance", "importance": 0.95, "rationale": "Owning compliance programs"}
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

# 3. Evidence Files
evidence_data = {
    "cv": {
        "source_id": "cv",
        "name": "CV / Resume Analysis - Cyber Security",
        "description": "Signals extracted from the user's CV/resume to evidence Cyber Security skills.",
        "extraction_rules": {
            "description": "How to extract and weight information from CV content.",
            "sections": [
                {"section": "skills_list", "description": "Explicit list of technologies and tools mentioned in skills section.", "base_strength": 0.3},
                {"section": "work_experience", "description": "Job descriptions and responsibilities.", "base_strength": 0.5, "quality_indicators": ["Quantifiable outcomes", "Action verbs"]},
                {"section": "projects", "description": "Personal or academic projects.", "base_strength": 0.4},
                {"section": "education", "description": "Relevant courses, degrees.", "base_strength": 0.2},
                {
                    "section": "certifications", 
                    "description": "Professional certifications.", 
                    "base_strength": 0.2,
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
            "description": "How CV mentions map to skill evidence using COMPOSITE KEYS.",
            "patterns": [
                {"pattern": "Mentions configuring Palo Alto or Fortinet firewalls in production", "maps_to": ["cs_networking.firewalls"], "strength_modifier": 1.0},
                {"pattern": "Describes leading a SOC2 or ISO27001 audit", "maps_to": ["cs_frameworks_compliance.soc2", "cs_frameworks_compliance.iso27001", "cs_frameworks_compliance.compliance_automation"], "strength_modifier": 1.2},
                {"pattern": "Has OSCP certification", "maps_to": ["cs_security_tools.nmap", "cs_security_tools.metasploit", "cs_security_tools.burp_suite", "cs_threats_and_attacks.priv_escalation"], "strength_modifier": 1.0},
                {"pattern": "Implemented Zero Trust architecture", "maps_to": ["cs_security_fundamentals.zero_trust", "cs_networking.zero_trust"], "strength_modifier": 1.2},
                {"pattern": "Led Incident Response Team", "maps_to": ["cs_incident_response_forensics.ir_containment", "cs_incident_response_forensics.ir_preparation"], "strength_modifier": 1.0}
            ]
        },
        "important_notes": ["CV data is self-reported and inherently unreliable as standalone evidence"]
    },
    "linkedin": {
        "source_id": "linkedin",
        "name": "LinkedIn Profile Analysis - Cyber Security",
        "description": "Signals extracted from LinkedIn profiles to evidence Cyber Security skills.",
        "extraction_rules": {
            "sections": [
                {"section": "headline_summary", "description": "Profile headline and summary.", "base_strength": 0.2},
                {"section": "experience", "description": "Work experience entries.", "base_strength": 0.4},
                {"section": "skills_endorsements", "description": "Skills listed with endorsement counts.", "base_strength": 0.15},
                {"section": "certifications", "description": "Professional certifications.", "base_strength": 0.2},
                {"section": "projects", "description": "Projects section.", "base_strength": 0.3},
                {"section": "recommendations", "description": "Written recommendations.", "base_strength": 0.3},
                {"section": "posts_articles", "description": "Technical posts.", "base_strength": 0.3}
            ]
        },
        "signal_mapping": {
            "description": "How LinkedIn mentions map to skill evidence.",
            "patterns": [
                {"pattern": "Endorsement for 'Network Security'", "maps_to": ["cs_networking.firewalls"], "strength_modifier": 0.33},
                {"pattern": "Endorsement for 'Cloud Security'", "maps_to": ["cs_cloud_security.cloud_concepts"], "strength_modifier": 0.33},
                {"pattern": "Job experience explicitly describing threat hunting", "maps_to": ["cs_incident_response_forensics.threat_hunting", "cs_security_tools.threat_hunting"], "strength_modifier": 1.0}
            ]
        },
        "important_notes": ["ALL extracted signals MUST be mapped to COMPOSITE KEYS"]
    },
    "assessment": {
        "source_id": "assessment",
        "name": "Adaptive Technical Assessment - Cyber Security",
        "description": "Adaptive technical questions to verify skills.",
        "trigger_conditions": {
            "rules": [
                "When a subskill has status 'not_yet_evidenced'",
                "When a subskill has status 'insufficient_evidence'"
            ]
        },
        "question_types": [
            {"type": "conceptual", "strength": 0.6},
            {"type": "scenario", "strength": 0.8},
            {"type": "practical_task", "strength": 1.0}
        ],
        "adaptive_logic": {
            "rules": [
                "Start with a conceptual question",
                "Escalate to a scenario question"
            ]
        },
        "sample_questions_by_composite_key": {
            "cs_networking.firewalls": [
                {"level": "mid", "type": "scenario", "question": "Troubleshoot connection to port 443.", "expected_answer_keywords": ["traffic logs", "security policy"]}
            ],
            "cs_cloud_security.serverless_security": [
                {"level": "senior", "type": "scenario", "question": "How do you secure an AWS Lambda function accessing RDS?", "expected_answer_keywords": ["IAM Role", "VPC", "Security Group", "Secrets Manager"]}
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
            "description": "Steps the backend takes BEFORE sending any data to AI for analysis.",
            "steps": [
                {
                    "step": 1,
                    "name": "repository_metadata",
                    "description": "Collect basic repository information via GitHub API.",
                    "data_points": ["repository name and description", "primary language"]
                },
                {
                    "step": 2,
                    "name": "file_tree_scan",
                    "description": "Scan the repository file tree for Security-relevant files.",
                    "target_files": [
                        {"pattern": "iptables.rules|openvpn.conf", "skill": "cs_networking", "priority": "high"},
                        {"pattern": "SELINUX=enforcing|auditd", "skill": "cs_operating_systems", "priority": "high"},
                        {"pattern": "ssl_certificate|ssl_protocols", "skill": "cs_cryptography", "priority": "high"},
                        {"pattern": "*.nse|*.pcap|*.yara|*.sig", "skill": "cs_security_tools", "priority": "medium"},
                        {"pattern": "SECURITY.md|threat-model.md", "skill": "cs_frameworks_compliance", "priority": "low"},
                        {"pattern": "*.tf|*.yml", "skill": "cs_cloud_security", "priority": "medium"}
                    ]
                },
                {
                    "step": 3,
                    "name": "dependency_extraction",
                    "description": "Extract dependencies to identify security tools.",
                    "relevant_dependencies": {
                        "cryptography": ["cryptography", "bcrypt", "argon2"],
                        "security_tools": ["bandit", "brakeman", "checkov", "tfsec"]
                    }
                },
                {
                    "step": 4,
                    "name": "readme_extraction",
                    "description": "Extract README.md content.",
                    "data_points": ["architecture diagrams or threat models"]
                },
                {
                    "step": 5,
                    "name": "relevant_content_extraction",
                    "description": "Extract the file content for AI analysis.",
                    "rules": ["Only extract files identified in step 2"]
                },
                {
                    "step": 6,
                    "name": "commit_analysis",
                    "description": "Analyze recent commit history for security patterns.",
                    "data_points": ["commit message patterns (e.g., 'patched CVE', 'fixed auth bypass')"],
                    "limit": "Last 100 commits or 6 months"
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

print("Expanded Cyber Security KB files generated correctly.")
