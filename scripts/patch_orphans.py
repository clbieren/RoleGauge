import json
import os
import glob

base_dir = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base"
skills_dir = os.path.join(base_dir, "skills")
devops_ev_dir = os.path.join(base_dir, "evidence")
cs_ev_dir = os.path.join(base_dir, "evidence", "cyber-security")

# 1. DELETE / MERGE
to_delete = {
    "cs_networking": ["subnetting"],
    "cs_operating_systems": ["file_permissions"],
    "ansible": ["adhoc_commands", "error_handling", "handlers"],
    "git": ["git_history"],
    "scripting": ["environment_config"]
}

for root, _, files in os.walk(skills_dir):
    for file in files:
        if file.endswith(".json"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            skill_id = data.get("skill_id")
            if skill_id in to_delete:
                d_list = to_delete[skill_id]
                
                # Remove from subskills
                if "subskills" in data:
                    data["subskills"] = [s for s in data["subskills"] if s["id"] not in d_list]
                
                # Remove from expected_subskills
                if "levels" in data:
                    for lvl in data["levels"].values():
                        if "expected_subskills" in lvl:
                            lvl["expected_subskills"] = [s for s in lvl["expected_subskills"] if s not in d_list]
                
                with open(filepath, 'w') as f:
                    json.dump(data, f, indent=2)

# Helper function to append mapping to cv/linkedin signal_mapping.patterns
def add_evidence_pattern(evidence_file, pattern_text, maps_to, strength=0.8):
    if not os.path.exists(evidence_file): return
    with open(evidence_file, 'r') as f:
        data = json.load(f)
    
    if "signal_mapping" in data and "patterns" in data["signal_mapping"]:
        data["signal_mapping"]["patterns"].append({
            "pattern": pattern_text,
            "maps_to": maps_to,
            "strength_modifier": strength
        })
        with open(evidence_file, 'w') as f:
            json.dump(data, f, indent=2)

# Helper for github
def add_github_pattern(evidence_file, step_name, target_file_obj=None, dependency=None, commit_pattern=None):
    if not os.path.exists(evidence_file): return
    with open(evidence_file, 'r') as f:
        data = json.load(f)
    
    for step in data.get("preprocessing_pipeline", {}).get("steps", []):
        if step["name"] == step_name:
            if target_file_obj and "target_files" in step:
                step["target_files"].append(target_file_obj)
            if commit_pattern and "data_points" in step:
                # find the one that starts with 'commit message patterns'
                for i, dp in enumerate(step["data_points"]):
                    if dp.startswith("commit message"):
                        step["data_points"][i] = dp.replace(")", f", '{commit_pattern}')")
    
    with open(evidence_file, 'w') as f:
        json.dump(data, f, indent=2)

# Helper for assessment
def add_assessment_question(evidence_file, composite_key, question_obj):
    if not os.path.exists(evidence_file): return
    with open(evidence_file, 'r') as f:
        data = json.load(f)
    
    if "sample_questions_by_composite_key" in data:
        if composite_key not in data["sample_questions_by_composite_key"]:
            data["sample_questions_by_composite_key"][composite_key] = []
        data["sample_questions_by_composite_key"][composite_key].append(question_obj)
        with open(evidence_file, 'w') as f:
            json.dump(data, f, indent=2)

# 2. ADD EVIDENCE TO DEVOPS
devops_cv = os.path.join(devops_ev_dir, "cv.json")
devops_li = os.path.join(devops_ev_dir, "linkedin.json")
devops_gh = os.path.join(devops_ev_dir, "github.json")
devops_as = os.path.join(devops_ev_dir, "assessment.json")

# CV
add_evidence_pattern(devops_cv, "Managed Nexus or Artifactory", ["cicd.artifact_management"])
add_evidence_pattern(devops_cv, "Reduced AWS costs by X%", ["cloud_platforms.cost_management"])
add_evidence_pattern(devops_cv, "Managed RDS, Aurora, or DynamoDB", ["cloud_platforms.databases"])
add_evidence_pattern(devops_cv, "Implemented CloudWatch or Stackdriver alerting", ["cloud_platforms.monitoring_cloud"])

# LinkedIn
add_evidence_pattern(devops_li, "Cloud Cost Optimization", ["cloud_platforms.cost_management"])
add_evidence_pattern(devops_li, "SLA/SLO/SLI Management", ["monitoring_observability.sla_slo_sli"])

# Github
add_github_pattern(devops_gh, "file_tree_scan", {"pattern": "aws_ec2.yml|inventory*.py", "skill": "ansible", "priority": "high"})
add_github_pattern(devops_gh, "file_tree_scan", {"pattern": "*StatefulSet*|*DaemonSet*", "skill": "kubernetes", "priority": "high"})
add_github_pattern(devops_gh, "file_tree_scan", {"pattern": "*.tf", "skill": "terraform", "priority": "high"})
add_github_pattern(devops_gh, "file_tree_scan", {"pattern": "lvcreate|vgcreate", "skill": "linux", "priority": "medium"})

# Assessment (DevOps Theoretical)
devops_theory = {
    "docker.container_performance_optimization": "How do you optimize a Dockerfile to reduce image size and build time?",
    "linux.basic_filesystem": "Explain the Linux filesystem hierarchy (e.g., /etc, /var, /usr).",
    "monitoring_observability.sla_slo_sli": "What is the difference between SLA, SLO, and SLI?",
    "networking.http_https": "Describe the HTTP request lifecycle.",
    "networking.ssh_protocol": "How does SSH key exchange work?",
    "scripting.regex": "Write a regex to match a valid IPv4 address."
}
for key, q in devops_theory.items():
    add_assessment_question(devops_as, key, {"level": "mid", "type": "conceptual", "question": q, "expected_answer_keywords": []})

# 3. ADD EVIDENCE TO CYBER SECURITY
cs_cv = os.path.join(cs_ev_dir, "cv.json")
cs_li = os.path.join(cs_ev_dir, "linkedin.json")
cs_gh = os.path.join(cs_ev_dir, "github.json")
cs_as = os.path.join(cs_ev_dir, "assessment.json")

# CV
add_evidence_pattern(cs_cv, "Managed GCP Security and VPC Controls", ["cs_cloud_security.gcp_security"])
add_evidence_pattern(cs_cv, "GDPR or CCPA compliance audits", ["cs_frameworks_compliance.data_privacy"])
add_evidence_pattern(cs_cv, "Reverse engineered malware", ["cs_incident_response_forensics.reverse_engineering"])
add_evidence_pattern(cs_cv, "Mitigated DDoS attacks via Akamai/Cloudflare", ["cs_networking.ddos_mitigation"])
add_evidence_pattern(cs_cv, "Deployed Snort or Suricata", ["cs_networking.ids_ips"])
add_evidence_pattern(cs_cv, "Architected VLANs and DMZs", ["cs_networking.network_segmentation"])
add_evidence_pattern(cs_cv, "Wrote PowerShell automation scripts", ["cs_programming_scripting.powershell"])
add_evidence_pattern(cs_cv, "Deployed EDR solutions", ["cs_security_tools.edr"])

# LinkedIn
add_evidence_pattern(cs_li, "Data Privacy (GDPR/CCPA)", ["cs_frameworks_compliance.data_privacy"])
add_evidence_pattern(cs_li, "Endpoint Detection and Response (EDR)", ["cs_security_tools.edr"])

# Github
add_github_pattern(cs_gh, "file_tree_scan", {"pattern": "*.tf|*.yml", "skill": "cs_cloud_security", "priority": "high"})
add_github_pattern(cs_gh, "file_tree_scan", {"pattern": "*.rules|snort.conf", "skill": "cs_networking", "priority": "high"})
add_github_pattern(cs_gh, "file_tree_scan", {"pattern": "pam.d", "skill": "cs_operating_systems", "priority": "high"})
add_github_pattern(cs_gh, "file_tree_scan", {"pattern": "*.ps1", "skill": "cs_programming_scripting", "priority": "medium"})

# For missing CS keys that need assessment mappings
add_assessment_question(cs_as, "cs_cryptography.digital_signatures", {"level": "mid", "type": "conceptual", "question": "Explain how digital signatures provide non-repudiation.", "expected_answer_keywords": []})
add_assessment_question(cs_as, "cs_operating_systems.pam_config", {"level": "senior", "type": "scenario", "question": "How do you enforce MFA using PAM?", "expected_answer_keywords": []})
add_assessment_question(cs_as, "cs_operating_systems.user_management", {"level": "junior", "type": "conceptual", "question": "Explain the difference between user and group permissions.", "expected_answer_keywords": []})
add_assessment_question(cs_as, "cs_programming_scripting.api_security", {"level": "mid", "type": "scenario", "question": "How do you secure a REST API?", "expected_answer_keywords": []})
add_assessment_question(cs_as, "cs_programming_scripting.js_security", {"level": "mid", "type": "scenario", "question": "How do you prevent DOM XSS?", "expected_answer_keywords": []})

# Assessment (CS Theoretical)
cs_theory = {
    "cs_cloud_security.cloud_models": "What is the difference between Public, Private, and Hybrid clouds?",
    "cs_cryptography.asymmetric_enc": "Explain how RSA encryption works conceptually.",
    "cs_cryptography.post_quantum": "What is the threat of quantum computing to modern cryptography?",
    "cs_incident_response_forensics.chain_of_custody": "Describe the chain of custody procedure for a seized hard drive.",
    "cs_operating_systems.malware_analysis": "What is the difference between static and dynamic malware analysis?",
    "cs_security_fundamentals.cia_triad": "Define Confidentiality, Integrity, and Availability.",
    "cs_security_fundamentals.risk_concepts": "Explain the relationship between risk, threat, and vulnerability.",
    "cs_threats_and_attacks.malware_types": "What is the difference between a worm and a virus?",
    "cs_threats_and_attacks.social_engineering": "Give an example of a spear-phishing attack.",
    "cs_threats_and_attacks.spoofing": "How does ARP spoofing work?"
}
for key, q in cs_theory.items():
    add_assessment_question(cs_as, key, {"level": "mid", "type": "conceptual", "question": q, "expected_answer_keywords": []})

print("Patched 45 orphaned subskills across skills and evidence files.")
