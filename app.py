from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Load the trained model
model = joblib.load("fraud_detection_model.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Ensure data is received in JSON format
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON format"}), 400

        # Validate required fields
        required_fields = ["type", "amount", "oldbalanceOrg", "newbalanceOrig", "oldbalanceDest", "newbalanceDest"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": f"Missing required fields. Required: {required_fields}"}), 400

        # Calculate engineered features
        balance_change = data["oldbalanceOrg"] - data["newbalanceOrig"]
        zero_balance_after = 1 if data["newbalanceOrig"] == 0 else 0

        # Extract transaction details with all 8 features (in same order as training)
        transaction_features = np.array([
            [
                data["type"], 
                data["amount"], 
                data["oldbalanceOrg"], 
                data["newbalanceOrig"], 
                data["oldbalanceDest"], 
                data["newbalanceDest"],
                balance_change,
                zero_balance_after
            ]
        ])

        # Make predictions
        prediction = model.predict(transaction_features)[0]
        probability = model.predict_proba(transaction_features)[0][1]

        return jsonify({
            "prediction": "Fraud" if prediction == 1 else "Legitimate",
            "fraud_probability": f"{probability * 100:.2f}%",
            "confidence": f"{max(probability, 1-probability) * 100:.2f}%"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
