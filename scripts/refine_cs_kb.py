import os
import json

base_dir = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base"
skills_dir = os.path.join(base_dir, "skills", "cyber-security")
evidence_dir = os.path.join(base_dir, "evidence", "cyber-security")

# 1. Update cs_incident_response_forensics.json
ir_path = os.path.join(skills_dir, "cs_incident_response_forensics.json")
with open(ir_path, 'r') as f:
    ir_data = json.load(f)

# Add reverse_engineering subskill and clarify boundaries
rev_eng = {
    "id": "reverse_engineering",
    "name": "Reverse Engineering",
    "description": "Decompiling and analyzing malicious binaries (static/dynamic analysis). Distinct from general 'malware_types' conceptual knowledge.",
    "keywords": ["Ghidra", "IDA Pro", "x64dbg", "Radare2", "Decompilation"]
}

# Update memory_analysis description to be clear
for sub in ir_data["subskills"]:
    if sub["id"] == "memory_analysis":
        sub["description"] = "Analyzing RAM dumps (distinct from static binary reverse engineering)."

ir_data["subskills"].append(rev_eng)
ir_data["levels"]["senior"]["expected_subskills"].append("reverse_engineering")

# Ensure additional_expectations is a list
if "additional_expectations" in ir_data["levels"]["senior"]:
    if isinstance(ir_data["levels"]["senior"]["additional_expectations"], str):
        ir_data["levels"]["senior"]["additional_expectations"] = [ir_data["levels"]["senior"]["additional_expectations"]]

with open(ir_path, 'w') as f:
    json.dump(ir_data, f, indent=2)

# 2. Update github.json
github_path = os.path.join(evidence_dir, "github.json")
with open(github_path, 'r') as f:
    github_data = json.load(f)

github_data["preprocessing_pipeline"]["steps"][2]["relevant_dependencies"].update({
    "programming_scripting": ["pwntools", "scapy", "impacket", "requests"],
    "cloud_security": ["boto3", "google-cloud-storage", "azure-mgmt-security", "aws-sdk"]
})

github_data["preprocessing_pipeline"]["steps"][5]["data_points"] = [
    "commit frequency and recency",
    "commit message patterns (e.g., 'patched CVE', 'fixed auth bypass', 'updated crypto', 'implemented MFA', 'fixed XSS', 'sanitized input')",
    "files changed in security-related commits"
]

# Ensure step 6 is actually fully populated
github_data["preprocessing_pipeline"]["steps"][5]["name"] = "commit_analysis"
github_data["preprocessing_pipeline"]["steps"][5]["description"] = "Analyze recent commit history for security patterns (patching, vulnerability fixing)."

with open(github_path, 'w') as f:
    json.dump(github_data, f, indent=2)

print("Refined IR forensics and github.json")
