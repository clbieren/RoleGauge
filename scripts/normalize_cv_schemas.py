import json
import os

base = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base\evidence"

def normalize_cv_json(role_dir):
    cv_path = os.path.join(base, role_dir, "cv.json")
    if not os.path.isfile(cv_path):
        return
        
    with open(cv_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    modified = False
    
    # 1. Handle roles with root 'sections' (data-engineer, machine-learning, mlops)
    if "sections" in data and "extraction_rules" not in data:
        root_sections = data.pop("sections")
        patterns = []
        new_sections = []
        
        for sec in root_sections:
            sec_id = sec.get("section_id", sec.get("section", "general"))
            base_str = sec.get("base_strength", 0.3)
            desc = sec.get("description", "")
            
            # Extract signal_extractors if present
            if "signal_extractors" in sec:
                for ext in sec["signal_extractors"]:
                    patterns.append({
                        "pattern": ext.get("pattern", ""),
                        "maps_to": ext.get("maps_to", []),
                        "strength_modifier": 1.0
                    })
                    
            new_sec = {
                "section": sec_id,
                "description": desc,
                "base_strength": base_str
            }
            new_sections.append(new_sec)
            
        data["extraction_rules"] = {
            "description": f"How to extract and weight information from CV content for {role_dir}.",
            "sections": new_sections
        }
        
        if "signal_mapping" not in data:
            data["signal_mapping"] = {
                "description": f"How CV mentions map to skill evidence using COMPOSITE KEYS for {role_dir}.",
                "patterns": patterns
            }
        modified = True
        
    # 2. Handle roles with signal_mapping but missing extraction_rules (blockchain-developer, ux-designer)
    elif "signal_mapping" in data and "extraction_rules" not in data:
        data["extraction_rules"] = {
            "description": f"How to extract and weight information from CV content for {role_dir}.",
            "sections": [
                {
                    "section": "skills_list",
                    "description": "Explicit list of technologies and tools in skills section.",
                    "base_strength": 0.3
                },
                {
                    "section": "work_experience",
                    "description": "Job descriptions describing technical achievements and responsibilities.",
                    "base_strength": 0.5
                },
                {
                    "section": "projects",
                    "description": "Personal or open-source projects demonstrating domain depth.",
                    "base_strength": 0.4
                },
                {
                    "section": "education",
                    "description": "Relevant computer science, engineering, or domain degrees.",
                    "base_strength": 0.2
                },
                {
                    "section": "certifications",
                    "description": "Professional certifications relevant to the role.",
                    "base_strength": 0.2
                }
            ]
        }
        modified = True
        
    # 3. Handle minimal roles (data-analyst, network-engineer)
    elif "extraction_rules" not in data:
        data["extraction_rules"] = {
            "description": f"How to extract and weight information from CV content for {role_dir}.",
            "sections": [
                {
                    "section": "skills_list",
                    "description": "Explicit list of technologies and tools in skills section.",
                    "base_strength": 0.3
                },
                {
                    "section": "work_experience",
                    "description": "Job descriptions describing technical achievements and responsibilities.",
                    "base_strength": 0.5
                },
                {
                    "section": "projects",
                    "description": "Personal or open-source projects demonstrating domain depth.",
                    "base_strength": 0.4
                },
                {
                    "section": "education",
                    "description": "Relevant academic degrees.",
                    "base_strength": 0.2
                },
                {
                    "section": "certifications",
                    "description": "Professional certifications relevant to the role.",
                    "base_strength": 0.2
                }
            ]
        }
        if "signal_mapping" not in data:
            data["signal_mapping"] = {
                "description": f"How CV mentions map to skill evidence using COMPOSITE KEYS for {role_dir}.",
                "patterns": []
            }
        modified = True
        
    if modified:
        with open(cv_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[NORMALIZED] {role_dir}/cv.json")

for r in sorted(os.listdir(base)):
    normalize_cv_json(r)
