# Models Directory

## Purpose
This directory contains trained machine learning models.

## Model Versioning

### model_v1.pkl
- **Type**: Linear Regression
- **Created**: -
- **Accuracy**: -
- **Description**: Baseline linear model for initial predictions

### model_v2.pkl
- **Type**: Random Forest
- **Created**: -
- **Accuracy**: -
- **Description**: Improved model with better accuracy

## Model Files

Models are serialized using Python's pickle format (.pkl).

## Usage
```python
from src.predictor import Predictor

# Load existing model
predictor = Predictor("model_v1")
predictions = predictor.predict(data)

# Or train new model
predictor = Predictor("model_v2")
predictor.train(X_train, y_train)
predictions = predictor.predict(X_test)
```

## Model Training

To train a new model:
```python
from src.predictor import Predictor
from src.data_loader import DataLoader

# Load data
loader = DataLoader("data/training_data.xlsx")
df = loader.load()

# Prepare features and labels
X = df[['feature1', 'feature2', ...]]
y = df['target']

# Train
predictor = Predictor("model_v3")
score = predictor.train(X, y)
print(f"Model score: {score}")
```

## Notes
- Models should be retrained periodically
- Keep version history
- Document model parameters
- Test before production use
