"""
Predictor Module - ML models and predictions
"""

import pickle
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from config import MODELS_DIR
from .utils import log


class Predictor:
    """Machine Learning predictions"""
    
    def __init__(self, model_name="model_v1"):
        """
        Initialize Predictor
        
        Args:
            model_name (str): Name of model file (without .pkl)
        """
        self.model_name = model_name
        self.model = None
        self.scaler = None
        self.is_trained = False
        
        # Try to load existing model
        self._load_model()
    
    def _load_model(self):
        """Load model from file if exists"""
        model_path = f"{MODELS_DIR}{self.model_name}.pkl"
        
        if os.path.exists(model_path):
            try:
                with open(model_path, 'rb') as f:
                    self.model = pickle.load(f)
                self.is_trained = True
                log(f"✅ Loaded model: {model_path}")
            except Exception as e:
                log(f"⚠️  Could not load model: {str(e)}")
        else:
            # Create new model if doesn't exist
            self.model = LinearRegression()
            log(f"Created new model: {self.model_name}")
    
    def _save_model(self):
        """Save model to file"""
        os.makedirs(MODELS_DIR, exist_ok=True)
        model_path = f"{MODELS_DIR}{self.model_name}.pkl"
        
        try:
            with open(model_path, 'wb') as f:
                pickle.dump(self.model, f)
            log(f"✅ Saved model: {model_path}")
        except Exception as e:
            log(f"❌ Error saving model: {str(e)}")
    
    def predict(self, X):
        """
        Make predictions
        
        Args:
            X (pd.DataFrame or np.array): Features for prediction
        
        Returns:
            np.array: Predictions
        """
        
        if self.model is None:
            raise ValueError("Model not initialized")
        
        # Convert DataFrame to numpy if needed
        if isinstance(X, pd.DataFrame):
            X = X.select_dtypes(include=[np.number]).values
        
        try:
            predictions = self.model.predict(X)
            log(f"✅ Generated {len(predictions)} predictions")
            return predictions
        except Exception as e:
            log(f"❌ Prediction error: {str(e)}")
            raise
    
    def train(self, X, y):
        """
        Train the model
        
        Args:
            X (pd.DataFrame or np.array): Training features
            y (pd.Series or np.array): Training labels
        
        Returns:
            float: Model score (R² for regression)
        """
        
        # Convert to numpy if needed
        if isinstance(X, pd.DataFrame):
            X = X.select_dtypes(include=[np.number]).values
        
        if isinstance(y, pd.Series):
            y = y.values
        
        try:
            # Train model
            self.model.fit(X, y)
            self.is_trained = True
            
            # Calculate score
            score = self.model.score(X, y)
            log(f"✅ Model trained. Score: {score:.4f}")
            
            # Save model
            self._save_model()
            
            return score
        except Exception as e:
            log(f"❌ Training error: {str(e)}")
            raise
    
    def get_model_info(self):
        """Get model information"""
        return {
            "name": self.model_name,
            "type": type(self.model).__name__,
            "trained": self.is_trained,
            "parameters": self.model.get_params() if hasattr(self.model, 'get_params') else {}
        }
