"""
Data Loader Module - Load and validate Excel files
"""

import pandas as pd
import os
from config import DATA_DIR, ALLOWED_EXTENSIONS, MAX_FILE_SIZE
from .utils import log


class DataLoader:
    """Load data from Excel files"""
    
    def __init__(self, filepath):
        """
        Initialize DataLoader
        
        Args:
            filepath (str): Path to Excel file
        """
        self.filepath = filepath
        self.df = None
    
    def load(self):
        """
        Load Excel file into DataFrame
        
        Returns:
            pd.DataFrame: Loaded data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is invalid
        """
        
        # Check if file exists
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File not found: {self.filepath}")
        
        # Check file size
        file_size = os.path.getsize(self.filepath)
        if file_size > MAX_FILE_SIZE:
            raise ValueError(f"File too large: {file_size / 1024 / 1024:.2f} MB")
        
        # Check extension
        _, ext = os.path.splitext(self.filepath)
        if ext.lower().lstrip('.') not in ALLOWED_EXTENSIONS:
            raise ValueError(f"Invalid file format: {ext}")
        
        # Load file
        try:
            # Auto-detect file format
            if self.filepath.endswith('.xlsx') or self.filepath.endswith('.xls'):
                self.df = pd.read_excel(self.filepath)
            else:  # CSV
                self.df = pd.read_csv(self.filepath)
            log(f"Loaded file: {self.filepath}")
            return self.df
        except Exception as e:
            raise ValueError(f"Error reading file: {str(e)}")
    
    def validate(self):
        """
        Validate loaded data
        
        Returns:
            bool: True if valid
            
        Raises:
            ValueError: If data is invalid
        """
        
        if self.df is None:
            raise ValueError("No data loaded. Call load() first.")
        
        if self.df.empty:
            raise ValueError("DataFrame is empty")
        
        log("✅ Data validation passed")
        return True
    
    def get_info(self):
        """Get DataFrame info"""
        if self.df is None:
            raise ValueError("No data loaded")
        
        return {
            "rows": len(self.df),
            "columns": len(self.df.columns),
            "column_names": list(self.df.columns),
            "dtypes": self.df.dtypes.to_dict()
        }
