# Fraud Detection System (Python)

## Overview

A Python-based machine learning system for detecting fraudulent financial transactions using a Decision Tree classifier.

## Features

- **Python ML Pipeline**: Uses scikit-learn for model training
- **Flask API**: REST endpoint for real-time predictions
- **Jupyter Notebook**: Complete EDA and model training workflow
- **High Accuracy**: 99.97% test accuracy on transaction data

## Tech Stack

```plaintext
Python 3.8+
Flask 2.0
scikit-learn
pandas
numpy
Jupyter Notebook
```

## Installation

1. Clone repo:
```bash
git clone https://github.com/yourusername/fraud-detection.git
cd fraud-detection
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

Start Flask server:
```bash
python app.py
```

Example API request:
```python
import requests

data = {
    "type": 4,  # TRANSFER
    "amount": 1000.0,
    "oldbalanceOrg": 5000.0,
    "newbalanceOrig": 4000.0
}

response = requests.post("http://localhost:5000/predict", json=data)
print(response.json())
```

## Project Structure

```plaintext
fraud-detection/git remote set-url origin https://github.com/tejaswiputluri-gif/Fraud-Detection-System.git
git push -u origin main --force

├── model/                   # Serialized .pkl model
│   └── fraud_model.pkl
├── notebooks/               # Jupyter notebooks
│   └── fraud_detection.ipynb
├── app.py                   # Flask application
├── requirements.txt         # Python dependencies
└── README.md
```

## Development

To retrain the model:
1. Run all cells in `notebooks/fraud_detection.ipynb`
2. The notebook will save the trained model to `model/fraud_model.pkl`



##Key improvements:
1. Removed all R-specific terminology
2. Added proper Python version requirements
3. Included Python-specific installation commands
4. Added Python API usage example
5. Organized files in standard Python project structure
6. Simplified tech stack section to focus on Python tools
7. Added clear model retraining instructions using Jupyter
