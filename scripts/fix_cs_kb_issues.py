import os
import json

base_dir = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base"
skills_dir = os.path.join(base_dir, "skills", "cyber-security")
evidence_dir = os.path.join(base_dir, "evidence", "cyber-security")

# 1. Fix additional_expectations in skills
for filename in os.listdir(skills_dir):
    if not filename.endswith(".json"): continue
    
    filepath = os.path.join(skills_dir, filename)
    with open(filepath, 'r') as f:
        data = json.load(f)
        
    for level in ["junior", "mid", "senior"]:
        if level in data.get("levels", {}):
            lvl_data = data["levels"][level]
            if "additional_expectations" in lvl_data:
                if level in ["junior", "mid"]:
                    # Remove from junior and mid to match DevOps exactly
                    del lvl_data["additional_expectations"]
                elif level == "senior":
                    # Convert to list if it's a string
                    if isinstance(lvl_data["additional_expectations"], str):
                        lvl_data["additional_expectations"] = [lvl_data["additional_expectations"]]
                        
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# 2. Fix github.json pipeline
github_path = os.path.join(evidence_dir, "github.json")
with open(github_path, 'r') as f:
    github_data = json.load(f)

# Re-introduce the 6 steps from DevOps, adapted for Cyber Security
github_data["preprocessing_pipeline"] = {
    "description": "Steps the backend takes BEFORE sending any data to AI for analysis.",
    "steps": [
        {
            "step": 1,
            "name": "repository_metadata",
            "description": "Collect basic repository information via GitHub API.",
            "data_points": [
                "repository name and description",
                "primary language and all languages used (with byte counts)",
                "stars, forks, and contributor count",
                "creation date and last push date",
                "license type",
                "topics/tags"
            ]
        },
        {
            "step": 2,
            "name": "file_tree_scan",
            "description": "Scan the repository file tree for Security-relevant files.",
            "target_files": [
                {"pattern": "iptables.rules|openvpn.conf", "skill": "cs_networking", "priority": "high"},
                {"pattern": "SELINUX=enforcing|auditd", "skill": "cs_os_security", "priority": "high"},
                {"pattern": "ssl_certificate|ssl_protocols", "skill": "cs_cryptography", "priority": "high"},
                {"pattern": "*.nse|*.pcap|*.yara|*.sig", "skill": "cs_security_tools", "priority": "medium"},
                {"pattern": "SECURITY.md|threat-model.md", "skill": "cs_risk_compliance", "priority": "low"}
            ]
        },
        {
            "step": 3,
            "name": "dependency_extraction",
            "description": "Extract dependencies from package manager files to identify security tools and crypto libraries.",
            "relevant_dependencies": {
                "cryptography": ["cryptography", "pycrypto", "bouncycastle", "libsodium", "openssl", "bcrypt", "argon2"],
                "security_tools": ["bandit", "brakeman", "checkov", "trivy", "snort", "suricata"],
                "os_security": ["pam", "selinux", "apparmor"]
            }
        },
        {
            "step": 4,
            "name": "readme_extraction",
            "description": "Extract README.md content for project description, architecture, and technology mentions.",
            "data_points": [
                "project description and purpose",
                "architecture diagrams or threat models",
                "security considerations or deployment instructions"
            ]
        },
        {
            "step": 5,
            "name": "relevant_content_extraction",
            "description": "For each identified Security-relevant file, extract the file content for AI analysis.",
            "rules": [
                "Only extract files identified in step 2 as relevant",
                "For large files (>500 lines), extract only the first 200 lines and key sections",
                "Never send entire application source code unless it contains security configuration patterns"
            ]
        },
        {
            "step": 6,
            "name": "commit_analysis",
            "description": "Analyze recent commit history for security patterns (patching, vulnerability fixing).",
            "data_points": [
                "commit frequency and recency",
                "commit message patterns (e.g., 'patched CVE', 'fixed auth bypass', 'updated crypto', 'security fix')",
                "files changed in security-related commits"
            ],
            "limit": "Last 100 commits or 6 months, whichever is less"
        }
    ]
}

with open(github_path, 'w') as f:
    json.dump(github_data, f, indent=2)

print("Fixed additional_expectations and github pipeline issues.")
