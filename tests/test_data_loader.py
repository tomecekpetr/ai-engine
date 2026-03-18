"""
Unit tests for DataLoader module
"""

import pytest
import pandas as pd
import os
from src.data_loader import DataLoader


class TestDataLoader:
    """Test DataLoader class"""
    
    def test_initialization(self):
        """Test DataLoader initialization"""
        loader = DataLoader("data/sample.xlsx")
        assert loader.filepath == "data/sample.xlsx"
        assert loader.df is None
    
    def test_load_missing_file(self):
        """Test loading non-existent file"""
        loader = DataLoader("data/nonexistent.xlsx")
        with pytest.raises(FileNotFoundError):
            loader.load()
    
    def test_get_info(self):
        """Test getting file info"""
        # This test assumes sample.xlsx exists
        if os.path.exists("data/sample.xlsx"):
            loader = DataLoader("data/sample.xlsx")
            df = loader.load()
            info = loader.get_info()
            
            assert "rows" in info
            assert "columns" in info
            assert info["rows"] > 0
    
    def test_validate_loaded_data(self):
        """Test data validation"""
        if os.path.exists("data/sample.xlsx"):
            loader = DataLoader("data/sample.xlsx")
            df = loader.load()
            
            is_valid = loader.validate()
            assert is_valid is True


if __name__ == "__main__":
    pytest.main([__file__])
