"""
Utilities Module - Helper functions
"""

import os
from datetime import datetime
from config import LOG_FILE, LOG_LEVEL


def log(message, level="INFO"):
    """
    Log message to console and file
    
    Args:
        message (str): Message to log
        level (str): Log level (INFO, WARNING, ERROR)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] [{level}] {message}"
    
    print(log_message)
    
    # Optionally write to file
    try:
        os.makedirs("logs", exist_ok=True)
        with open(f"logs/{LOG_FILE}", "a") as f:
            f.write(log_message + "\n")
    except:
        pass


def save_dataframe(df, filepath):
    """
    Save DataFrame to CSV
    
    Args:
        df (pd.DataFrame): DataFrame to save
        filepath (str): Output file path
    """
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False)
        log(f"✅ Saved: {filepath}")
    except Exception as e:
        log(f"❌ Error saving file: {str(e)}", "ERROR")
        raise


def load_model(filepath):
    """
    Load pickled model
    
    Args:
        filepath (str): Path to model file
    
    Returns:
        Model object
    """
    import pickle
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Model not found: {filepath}")
    
    try:
        with open(filepath, 'rb') as f:
            model = pickle.load(f)
        log(f"✅ Loaded model: {filepath}")
        return model
    except Exception as e:
        log(f"❌ Error loading model: {str(e)}", "ERROR")
        raise


def format_number(number, decimals=2):
    """
    Format number with decimals
    
    Args:
        number (float): Number to format
        decimals (int): Number of decimal places
    
    Returns:
        str: Formatted number
    """
    return f"{number:.{decimals}f}"
