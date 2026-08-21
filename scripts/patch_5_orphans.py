import json
import os

devops_as = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base\evidence\assessment.json"
with open(devops_as, 'r') as f:
    data = json.load(f)

q = {
    "ansible.dynamic_inventory": "How do you configure dynamic inventory in Ansible for AWS EC2?",
    "kubernetes.statefulsets_daemonsets": "Explain the difference between a Deployment and a StatefulSet.",
    "linux.advanced_storage_lvm": "Walk me through how you would extend an LVM logical volume.",
    "scripting.cli_tool_development": "How do you structure command line arguments in Python?",
    "terraform.expressions_functions": "How do you use the for_each meta-argument in Terraform?"
}

for k, v in q.items():
    if "sample_questions_by_composite_key" not in data:
        data["sample_questions_by_composite_key"] = {}
    if k not in data["sample_questions_by_composite_key"]:
        data["sample_questions_by_composite_key"][k] = []
    data["sample_questions_by_composite_key"][k].append({"level": "senior", "type": "conceptual", "question": v, "expected_answer_keywords": []})

with open(devops_as, 'w') as f:
    json.dump(data, f, indent=2)
print("Added missing assessment questions.")
