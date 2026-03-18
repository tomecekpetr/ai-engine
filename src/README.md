# Data Directory

## Purpose
This directory contains Excel files with data for analysis and training.

## Expected Format

### Excel File Structure
- **First row**: Column headers (names)
- **Data types**: datetime, numeric, string
- **Max size**: 50 MB per file

### Example Structure
Date  Product  Sales  Profit
2024-01-01  A  1000  200  

## Files

### sample.xlsx
- Sample file for testing
- Contains synthetic data
- Use for development and testing

### Your Data Files
- Add your own Excel files here
- Follow the expected format
- Update this README with descriptions

## Usage
```python
from src.data_loader import DataLoader

loader = DataLoader("data/your_file.xlsx")
df = loader.load()
```

## Notes
- Data files should not be committed (usually in .gitignore)
- Large files should be stored separately
- Ensure data quality before analysis
