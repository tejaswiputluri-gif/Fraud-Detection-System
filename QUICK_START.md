# 🚀 Quick Start Guide - Fraud Detection System

## Project Overview
Production-ready fraud detection system with **99.73% accuracy** and **99.09% fraud detection rate**.

---

## ⚡ Quick Setup (5 minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start Flask Server
```bash
python app.py
```
✅ Server running at `http://localhost:5000`

### Step 3: Make Predictions
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "type": 4,
    "amount": 1000,
    "oldbalanceOrg": 5000,
    "newbalanceOrig": 4000,
    "oldbalanceDest": 1000,
    "newbalanceDest": 2000
  }'
```

---

## 📝 API Request Format

**Endpoint**: `POST /predict`

### Required Fields (All Mandatory)
```json
{
  "type": 1-5,                    // 1=CASH_OUT, 2=PAYMENT, 3=CASH_IN, 4=TRANSFER, 5=DEBIT
  "amount": 0.01-1000000.00,     // Transaction amount (positive number)
  "oldbalanceOrg": 0.00+,        // Sender's balance BEFORE transaction
  "newbalanceOrig": 0.00+,       // Sender's balance AFTER transaction
  "oldbalanceDest": 0.00+,       // Recipient's balance BEFORE transaction
  "newbalanceDest": 0.00+        // Recipient's balance AFTER transaction
}
```

### Response Format
```json
{
  "prediction": "Fraud" or "Legitimate",
  "fraud_probability": "X.XX%",
  "confidence": "X.XX%"
}
```

---

## 📊 Example Requests

### ✅ Legitimate Transaction
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "type": 2,
    "amount": 5000,
    "oldbalanceOrg": 50000,
    "newbalanceOrig": 45000,
    "oldbalanceDest": 5000,
    "newbalanceDest": 10000
  }'
```
**Response**: `"prediction": "Legitimate", "fraud_probability": "1.05%"`

### 🚨 Suspicious Transaction
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "type": 4,
    "amount": 181,
    "oldbalanceOrg": 181,
    "newbalanceOrig": 0,
    "oldbalanceDest": 0,
    "newbalanceDest": 0
  }'
```
**Response**: `"prediction": "Fraud", "fraud_probability": "100.00%"`

---

## 🎯 Understanding Predictions

### High Fraud Probability (> 50%)
- **Action**: Block or verify transaction
- **Example**: Account balance completely emptied
- **Typical Cause**: Unusual balance changes

### Low Fraud Probability (< 20%)
- **Action**: Allow transaction
- **Confidence**: Very high legitimate probability
- **Typical Cause**: Normal transaction patterns

### Medium Risk (20-50%)
- **Action**: Review and potentially challenge user
- **Confidence**: Moderate uncertainty
- **Typical Cause**: Edge cases or uncommon patterns

---

## 🔍 Model Details

### Features Used (8 Total)
1. **type** - Transaction type (1-5)
2. **amount** - Transaction amount
3. **oldbalanceOrg** - Sender's initial balance
4. **newbalanceOrig** - Sender's final balance
5. **oldbalanceDest** - Recipient's initial balance
6. **newbalanceDest** - Recipient's final balance
7. **balance_change** - Auto-calculated: oldbalanceOrg - newbalanceOrig
8. **zero_balance_after** - Auto-calculated: 1 if newbalanceOrig == 0, else 0

### Most Important Features (by importance)
| Rank | Feature | Importance |
|------|---------|------------|
| 1 | balance_change | 28.5% |
| 2 | oldbalanceOrg | 21.7% |
| 3 | amount | 15.3% |
| 4 | newbalanceOrig | 10.7% |
| 5 | type | 9.2% |

### Algorithm
- **Type**: Random Forest Classifier
- **Trees**: 100 decision trees
- **Training**: SMOTE-balanced data (50% fraud synthetic samples)
- **Test Accuracy**: 99.73%

---

## 📊 Performance Metrics

| Metric | Value | What It Means |
|--------|-------|---------------|
| **Sensitivity** | 99.09% | Catches 99 out of 100 fraud cases ✅ |
| **Specificity** | 99.73% | Only 0.27% legitimate users blocked ✅ |
| **Precision** | 32.49% | 1 in 3 flagged cases is actual fraud |
| **ROC-AUC** | 99.95% | Excellent discrimination ability ✅ |
| **Test Accuracy** | 99.73% | Overall correctness rate |

---

## ⚙️ Retrain Model

### Run Full Pipeline
```bash
# Open Jupyter notebook
jupyter notebook homwwork.ipynb

# Run all cells in order:
# 1. Data Loading
# 2. Data Cleaning & Feature Engineering
# 3. Train-Test Split + SMOTE
# 4. Model Training
# 5. Model Evaluation
# 6. Prediction Examples
# 7. Save Model

# Time needed: ~15-20 minutes
```

---

## 🐛 Troubleshooting

### Error: "No such file or directory: fraud_detection_model.pkl"
**Solution**: Run notebook cells to train and save the model first

### Error: "ModuleNotFoundError: No module named 'imbalanced_learn'"
**Solution**: `pip install imbalanced-learn`

### Error: "scikit-learn version mismatch"
**Info**: Warning only, model still works. Optional: upgrade scikit-learn
```bash
pip install --upgrade scikit-learn
```

### Predictions seem random
**Check**: Ensure all 6 required input fields are provided with numeric values

---

## 📁 Project Files

```
fraud-detection/
├── app.py                          # Flask REST API server
├── homwwork.ipynb                  # ML pipeline notebook
├── index.html                      # Web UI (optional)
├── requirements.txt                # Python dependencies
├── fraud_detection_model.pkl       # Trained model ⭐
├── model_metadata.json             # Model stats
├── FINAL_REPORT.md                 # Detailed report
├── QUICK_START.md                  # This file
└── PS_20174392719_1491204439457_log.csv  # Training data
```

---

## 🔐 Security Recommendations

1. **API Key**: Add authentication before production
2. **Rate Limiting**: Limit requests to prevent abuse
3. **HTTPS**: Use SSL/TLS in production
4. **Logging**: Log all predictions for audit trail
5. **Monitoring**: Alert on model performance degradation

---

## 🎓 Key Insights

### Why Model Works Well
✅ **SMOTE Balancing**: Synthetic fraud samples improved detection from 50% → 99%
✅ **Feature Engineering**: balance_change captures fraud patterns
✅ **Stratified Splitting**: Preserved fraud ratio in train/test
✅ **RandomForest**: Handles non-linear patterns well

### What to Monitor
⚠️ **False Positive Rate**: Currently 0.27% (acceptable)
⚠️ **False Negative Rate**: Currently 0.91% (very low)
⚠️ **Data Drift**: Monitor if transaction patterns change
⚠️ **Model Accuracy**: Retrain monthly with new data

---

## 📞 Support & Questions

**Check**: `FINAL_REPORT.md` for detailed documentation
**Issues**: Verify all 6 input fields are provided
**Performance**: See metrics in Quick Start section

---

**Last Updated**: May 22, 2026
**Status**: ✅ Production Ready
