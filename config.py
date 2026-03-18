"""
Configuration file for AI Engine
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ==================== PATHS ====================
DATA_DIR = "data/"
MODELS_DIR = "models/"
OUTPUT_DIR = "output/"

# ==================== API KEYS ====================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# ==================== SETTINGS ====================
DEBUG = os.getenv("DEBUG", "True") == "True"
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB
ALLOWED_EXTENSIONS = ["xlsx", "xls", "csv"]

# ==================== ML SETTINGS ====================
MODEL_VERSION = "v1"
TRAIN_TEST_SPLIT = 0.8
RANDOM_STATE = 42

# ==================== LOGGING ====================
LOG_FILE = "ai_engine.log"
LOG_LEVEL = "INFO"
