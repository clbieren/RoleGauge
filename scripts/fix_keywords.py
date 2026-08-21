import json

devops_as = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base\evidence\assessment.json"
with open(devops_as, 'r') as f:
    data = json.load(f)

keywords_map = {
    "ansible.dynamic_inventory": ["plugin", "aws_ec2", "boto3", "tags", "filters"],
    "kubernetes.statefulsets_daemonsets": ["persistent volume", "pvc", "sticky identity", "ordered deployment", "headless service"],
    "linux.advanced_storage_lvm": ["lvextend", "resize2fs", "xfs_growfs", "pvcreate", "vgextend"],
    "scripting.cli_tool_development": ["argparse", "click", "flags", "positional arguments", "help message"],
    "terraform.expressions_functions": ["map", "set", "dynamic block", "iteration", "each.key", "each.value"]
}

if "sample_questions_by_composite_key" in data:
    for k, v in keywords_map.items():
        if k in data["sample_questions_by_composite_key"]:
            for q in data["sample_questions_by_composite_key"][k]:
                if not q.get("expected_answer_keywords"):
                    q["expected_answer_keywords"] = v

with open(devops_as, 'w') as f:
    json.dump(data, f, indent=2)
print("Fixed missing keywords in DevOps.")

cs_as = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base\evidence\cyber-security\assessment.json"
with open(cs_as, 'r') as f:
    cs_data = json.load(f)

cs_keywords_map = {
    "cs_cryptography.digital_signatures": ["hashing", "private key", "public key verification", "integrity", "non-repudiation"],
    "cs_operating_systems.pam_config": ["pam.d", "required", "sufficient", "pam_google_authenticator", "sshd_config"],
    "cs_operating_systems.user_management": ["uid", "gid", "file ownership", "sudoers", "least privilege"],
    "cs_programming_scripting.api_security": ["jwt", "oauth2", "rate limiting", "input validation", "tls"],
    "cs_programming_scripting.js_security": ["content security policy", "csp", "input sanitization", "escape", "innertext vs innerhtml"],
    "cs_cloud_security.cloud_models": ["multi-tenant", "single-tenant", "on-premise", "scalability", "capex vs opex"],
    "cs_cryptography.asymmetric_enc": ["public key", "private key", "prime factorization", "key exchange", "computational hardness"],
    "cs_cryptography.post_quantum": ["shor's algorithm", "lattice-based", "kyber", "qkd", "larger key sizes"],
    "cs_incident_response_forensics.chain_of_custody": ["evidence log", "hashes", "secure storage", "tamper-evident", "documentation"],
    "cs_operating_systems.malware_analysis": ["reverse engineering", "sandboxing", "execution", "code analysis", "behavioral"],
    "cs_security_fundamentals.cia_triad": ["confidentiality", "integrity", "availability", "unauthorized access", "uptime"],
    "cs_security_fundamentals.risk_concepts": ["likelihood", "impact", "vulnerability exploitation", "asset value", "mitigation"],
    "cs_threats_and_attacks.malware_types": ["self-replicating", "network propagation", "file execution", "payload", "standalone"],
    "cs_threats_and_attacks.social_engineering": ["targeted", "specific individual", "reconnaissance", "trust", "deception"],
    "cs_threats_and_attacks.spoofing": ["mac address", "ip address", "gratuitous arp", "mitm", "layer 2"]
}

if "sample_questions_by_composite_key" in cs_data:
    for k, v in cs_keywords_map.items():
        if k in cs_data["sample_questions_by_composite_key"]:
            for q in cs_data["sample_questions_by_composite_key"][k]:
                if not q.get("expected_answer_keywords"):
                    q["expected_answer_keywords"] = v

with open(cs_as, 'w') as f:
    json.dump(cs_data, f, indent=2)
print("Fixed missing keywords in Cyber Security.")
