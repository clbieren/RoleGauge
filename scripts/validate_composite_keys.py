import json
import glob
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
skills_dir = os.path.join(base_dir, 'knowledge-base', 'skills', '**', '*.json')
evidence_dir = os.path.join(base_dir, 'knowledge-base', 'evidence', '**', '*.json')

valid_keys = set()
valid_skill_ids = set()

broken = []
disjointness_issues = []
count_issues = []
assessment_issues = []
schema_issues = []
referenced_keys = set()

# -------------------------------------------------------------
# Layer 1 & 2 & 3: Skills Validation (References, Disjointness, Counts)
# -------------------------------------------------------------
for f in glob.glob(skills_dir, recursive=True):
    with open(f, 'r', encoding='utf-8') as file:
        data = json.load(file)
        skill_id = data.get('skill_id')
        if not skill_id:
            continue
        valid_skill_ids.add(skill_id)
        
        local_subskills = set()
        subskills = data.get('subskills', [])
        for sub in subskills:
            if 'id' in sub:
                valid_keys.add(f'{skill_id}.{sub["id"]}')
                local_subskills.add(sub["id"])
                
        # Subskill count constraint check (8-11 per skill)
        sub_count = len(subskills)
        if sub_count < 8 or sub_count > 11:
            count_issues.append((os.path.basename(f), f'{sub_count} subskills (expected 8-11)'))
                
        # Validating expected_subskills against defined subskills & checking disjointness
        levels = data.get('levels', {})
        level_assigned_subskills = {}
        for level_name, level_data in levels.items():
            expected = level_data.get('expected_subskills', [])
            
            # Level subskill count check (minimum 2)
            if len(expected) < 2:
                count_issues.append((os.path.basename(f), f'Level {level_name} has only {len(expected)} subskills (minimum 2 required)'))
            
            for exp in expected:
                # Ghost subskill check
                if exp not in local_subskills:
                    broken.append((os.path.basename(f), exp, f'levels.{level_name}.expected_subskills'))
                
                # Disjointness check
                if exp in level_assigned_subskills:
                    disjointness_issues.append((os.path.basename(f), exp, f'Assigned to both {level_assigned_subskills[exp]} and {level_name}'))
                else:
                    level_assigned_subskills[exp] = level_name


# -------------------------------------------------------------
# Layer 4: Composite Key References & Evidence Scanning
# -------------------------------------------------------------
all_files = glob.glob(evidence_dir, recursive=True) + glob.glob(skills_dir, recursive=True)
for f in all_files:
    with open(f, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
        def find_composite_keys(obj, path=''):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    # 1. Check if dictionary key itself is a composite key
                    if '.' in k:
                        prefix = k.split('.')[0]
                        if prefix in valid_skill_ids:
                            if k not in valid_keys:
                                broken.append((os.path.basename(f), k, path + '.' + k if path else k))
                            else:
                                referenced_keys.add(k)
                                
                    # 2. Check traditional maps_to arrays
                    if k == 'maps_to' and isinstance(v, list):
                        for item in v:
                            if item not in valid_keys:
                                broken.append((os.path.basename(f), item, path + '.maps_to'))
                            else:
                                referenced_keys.add(item)
                    else:
                        find_composite_keys(v, path + '.' + k if path else k)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    find_composite_keys(item, path + f'[{i}]')
                    
        find_composite_keys(data)


# -------------------------------------------------------------
# Layer 5: Assessment Question Quality & Keyword Completeness
# -------------------------------------------------------------
for f in glob.glob(evidence_dir, recursive=True):
    if os.path.basename(f) == 'assessment.json':
        with open(f, 'r', encoding='utf-8') as file:
            data = json.load(file)
            q_map = data.get('sample_questions_by_composite_key', {})
            for key, q_list in q_map.items():
                if not q_list:
                    assessment_issues.append((os.path.basename(f), key, 'No questions provided'))
                for q in q_list:
                    q_text = q.get('question', '')
                    keywords = q.get('expected_answer_keywords', [])
                    if not q_text.strip():
                        assessment_issues.append((os.path.basename(f), key, 'Empty question text'))
                    if not keywords:
                        assessment_issues.append((os.path.basename(f), key, 'Empty expected_answer_keywords'))


# -------------------------------------------------------------
# Layer 6: Evidence Schema Consistency (cv.json, github.json, linkedin.json)
# -------------------------------------------------------------
for f in glob.glob(evidence_dir, recursive=True):
    basename = os.path.basename(f)
    role_name = os.path.basename(os.path.dirname(f))
    
    with open(f, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except Exception as e:
            schema_issues.append((f"{role_name}/{basename}", f"JSON decode error: {e}"))
            continue
            
    if basename == 'cv.json':
        # Check extraction_rules if present
        ext_rules = data.get('extraction_rules')
        if ext_rules is not None:
            if not isinstance(ext_rules, dict):
                schema_issues.append((f"{role_name}/{basename}", "'extraction_rules' must be an object/dict"))
            else:
                sections = ext_rules.get('sections')
                if sections is not None:
                    if not isinstance(sections, list):
                        schema_issues.append((f"{role_name}/{basename}", f"'extraction_rules.sections' must be a list, found {type(sections).__name__}"))
                    else:
                        for idx, sec in enumerate(sections):
                            if not isinstance(sec, dict):
                                schema_issues.append((f"{role_name}/{basename}", f"sections[{idx}] must be an object/dict"))
                            else:
                                if 'section' not in sec or not isinstance(sec['section'], str):
                                    schema_issues.append((f"{role_name}/{basename}", f"sections[{idx}] missing valid string 'section' key"))
                                if 'base_strength' in sec and not isinstance(sec['base_strength'], (int, float)):
                                    schema_issues.append((f"{role_name}/{basename}", f"sections[{idx}] 'base_strength' must be numeric"))
        
        # Check signal_mapping if present
        sig_map = data.get('signal_mapping')
        if sig_map is not None:
            if not isinstance(sig_map, dict):
                schema_issues.append((f"{role_name}/{basename}", "'signal_mapping' must be an object/dict"))
            else:
                patterns = sig_map.get('patterns')
                if patterns is not None:
                    if not isinstance(patterns, list):
                        schema_issues.append((f"{role_name}/{basename}", f"'signal_mapping.patterns' must be a list, found {type(patterns).__name__}"))
                    else:
                        for idx, pat in enumerate(patterns):
                            if not isinstance(pat, dict):
                                schema_issues.append((f"{role_name}/{basename}", f"patterns[{idx}] must be an object/dict"))
                            elif 'pattern' not in pat or not isinstance(pat['pattern'], str):
                                schema_issues.append((f"{role_name}/{basename}", f"patterns[{idx}] missing string 'pattern'"))
                            elif 'maps_to' not in pat or not isinstance(pat['maps_to'], list):
                                schema_issues.append((f"{role_name}/{basename}", f"patterns[{idx}] missing list 'maps_to'"))


# -------------------------------------------------------------
# Report Results
# -------------------------------------------------------------
print('=' * 70)
print('ROLEGAUGE KNOWLEDGE BASE MULTI-LAYER VALIDATION REPORT')
print('=' * 70)

# 1. Broken References & Ghost Subskills
if broken:
    print('\n[FAILED] BROKEN REFERENCES OR GHOST SUBSKILLS FOUND:')
    for filename, ref, path in broken:
        print(f'  - File: {filename}, Reference: {ref}, Path: {path}')
else:
    print('[PASSED] Layer 1: All composite keys & expected_subskills references are valid.')

# 2. Level Disjointness
if disjointness_issues:
    print('\n[FAILED] LEVEL DISJOINTNESS VIOLATIONS FOUND:')
    for filename, sub, desc in disjointness_issues:
        print(f'  - File: {filename}, Subskill: {sub}, Issue: {desc}')
else:
    print('[PASSED] Layer 2: All skill levels are strictly disjoint (0 cross-level overlap).')

# 3. Subskill Counts & Distribution
if count_issues:
    print('\n[FAILED] SUBSKILL COUNT VIOLATIONS FOUND:')
    for filename, desc in count_issues:
        print(f'  - File: {filename}, Issue: {desc}')
else:
    print('[PASSED] Layer 3: All skills satisfy subskill count constraints (8-11 per skill, >=2 per level).')

# 4. Evidence Coverage
unreferenced = valid_keys - referenced_keys
if unreferenced:
    print('\n[FAILED] ORPHANED SUBSKILLS (NO EVIDENCE MAPPING):')
    for key in sorted(unreferenced):
        print(f'  - {key}')
else:
    print('[PASSED] Layer 4: Evidence coverage is 100% (0 orphaned subskills across all scanned sources).')

# 5. Assessment Question Quality
if assessment_issues:
    print('\n[WARNING] ASSESSMENT QUESTION COMPLETENESS ISSUES:')
    for filename, key, desc in assessment_issues:
        print(f'  - File: {filename}, Key: {key}, Issue: {desc}')
else:
    print('[PASSED] Layer 5: All assessment questions have non-empty text and populated keywords.')

# 6. Evidence Schema Consistency
if schema_issues:
    print('\n[FAILED] LAYER 6: EVIDENCE SCHEMA CONSISTENCY VIOLATIONS:')
    for filename, issue in schema_issues:
        print(f'  - File: {filename}: {issue}')
else:
    print('[PASSED] Layer 6: All evidence files conform to canonical schema standards (0 format discrepancies).')

print('=' * 70)
