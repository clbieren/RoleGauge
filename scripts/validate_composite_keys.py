import json
import glob
import os

valid_keys = set()
valid_skill_ids = set()
skills_dir = r'd:\Repos\RoleGauge\knowledge-base\skills\**\*.json'
evidence_dir = r'd:\Repos\RoleGauge\knowledge-base\evidence\**\*.json'

broken = []
referenced_keys = set()

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
                
        # Validating expected_subskills against defined subskills
        levels = data.get('levels', {})
        for level_name, level_data in levels.items():
            expected = level_data.get('expected_subskills', [])
            for exp in expected:
                if exp not in local_subskills:
                    broken.append((os.path.basename(f), exp, f'levels.{level_name}.expected_subskills'))


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

if broken:
    print('BROKEN REFERENCES FOUND:')
    for filename, ref, path in broken:
        print(f'File: {filename}, Reference: {ref}, Path: {path}')
else:
    print('All maps_to and dict-key composite references are valid! No ghost subskills in expected_subskills either!')

unreferenced = valid_keys - referenced_keys
if unreferenced:
    print('\nWARNING - ORPHANED SUBSKILLS (NO EVIDENCE MAPPING):')
    for key in sorted(unreferenced):
        print(f'- {key}')
else:
    print('\nAll subskills have at least one evidence mapping! Coverage is 100%.')
