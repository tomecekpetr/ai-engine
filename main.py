#!/usr/bin/env python3
"""
AI Engine - Main application entry point
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import DATA_DIR, DEBUG
from src.data_loader import DataLoader
from src.analyzer import Analyzer
from src.predictor import Predictor
from src.utils import log


def main():
    """Main execution function"""
    
    log("=" * 50)
    log("🚀 AI Engine Started")
    log("=" * 50)
    
    try:
        # Step 1: Load data
        log("\n1️⃣  Loading data from CSV...")
        loader = DataLoader(f"{DATA_DIR}sample.csv")
        df = loader.load()
        log(f"✅ Loaded {len(df)} rows, {len(df.columns)} columns")
        
        # Step 2: Analyze data
        log("\n2️⃣  Analyzing data...")
        analyzer = Analyzer(df)
        stats = analyzer.get_statistics()
        log(f"✅ Analysis complete")
        print("\nBasic Statistics:")
        print(stats)
        
        # Step 3: Train model and make predictions
        log("\n3️⃣  Training model and making predictions...")
        predictor = Predictor()
        
        # Prepare data for training
        X = df[['Sales']].values  # Features (input)
        y = df['Profit'].values   # Target (output)
        
        # Train model
        score = predictor.train(X, y)
        log(f"✅ Model trained with score: {score:.4f}")
        
        # Make predictions
        predictions = predictor.predict(X)
        log(f"✅ Generated {len(predictions)} predictions")
        print("\nSample Predictions:")
        print(predictions[:5])
        
        log("\n" + "=" * 50)
        log("✅ AI Engine completed successfully!")
        log("=" * 50)
        
    except Exception as e:
        log(f"❌ Error: {str(e)}")
        if DEBUG:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
