import os
import sys

# Ensure backend directory is in sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Set test environment variables
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///:memory:"
os.environ["KB_PATH"] = os.path.join(os.path.dirname(BASE_DIR), "knowledge-base")
os.environ["AI_PROVIDER"] = "none"
