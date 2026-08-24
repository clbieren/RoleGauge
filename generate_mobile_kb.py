import os
import json

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'knowledge-base'))

# Ensure directories exist
for platform in ['android', 'ios']:
    os.makedirs(os.path.join(base_dir, 'skills', platform), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'roles', platform), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'evidence', platform), exist_ok=True)

print("Directories prepared successfully.")
