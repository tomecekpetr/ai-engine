"""
Analyzer Module - Analyze data and generate insights
"""

import pandas as pd
import numpy as np
from .utils import log


class Analyzer:
    """Analyze data and provide statistics"""
    
    def __init__(self, df):
        """
        Initialize Analyzer
        
        Args:
            df (pd.DataFrame): Data to analyze
        """
        if df is None or df.empty:
            raise ValueError("DataFrame cannot be None or empty")
        
        self.df = df
        log(f"Analyzer initialized with {len(df)} rows")
    
    def get_statistics(self):
        """
        Get basic statistics
        
        Returns:
            pd.DataFrame: Statistics summary
        """
        return self.df.describe()
    
    def get_correlations(self):
        """
        Get correlation matrix
        
        Returns:
            pd.DataFrame: Correlation matrix
        """
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) == 0:
            log("⚠️  No numeric columns found for correlation")
            return None
        
        return self.df[numeric_cols].corr()
    
    def get_missing_data(self):
        """
        Get missing data report
        
        Returns:
            dict: Missing data information
        """
        missing = {
            "total": self.df.isnull().sum().to_dict(),
            "percentage": (self.df.isnull().sum() / len(self.df) * 100).to_dict()
        }
        return missing
    
    def get_column_info(self):
        """
        Get information about each column
        
        Returns:
            dict: Column information
        """
        info = {}
        for col in self.df.columns:
            info[col] = {
                "dtype": str(self.df[col].dtype),
                "unique_values": self.df[col].nunique(),
                "missing": self.df[col].isnull().sum()
            }
        return info
    
    def detect_anomalies(self, column=None, threshold=3):
        """
        Detect outliers using z-score
        
        Args:
            column (str): Column to check. If None, checks all numeric columns
            threshold (float): Z-score threshold (default: 3)
        
        Returns:
            dict: Anomalies found
        """
        from scipy import stats
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        anomalies = {}
        
        for col in numeric_cols:
            z_scores = np.abs(stats.zscore(self.df[col].dropna()))
            outlier_indices = np.where(z_scores > threshold)[0]
            
            if len(outlier_indices) > 0:
                anomalies[col] = {
                    "count": len(outlier_indices),
                    "percentage": len(outlier_indices) / len(self.df) * 100
                }
        
        return anomalies
