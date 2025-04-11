from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS
import json

with open("avg_velocity_lookup.json", "r") as f:
    velocity_data = json.load(f)

# Build a quick lookup dictionary
velocity_lookup = {
    (entry["pitcher_id"], entry["pitch_type_group"]): round(entry["avg_velocity"], 1)
    for entry in velocity_data
}

app = Flask(__name__)
CORS(app)  # ✅ This will allow all domains (safe for development)

# Load model, scaler, label encoder
model = joblib.load("xgb_pitch_predictor_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("group_label_encoder.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        input_order = [
            'stand', 'balls', 'strikes', 'inning', 'outs_when_up',
            'on_1b', 'on_2b', 'on_3b', 'score_diff', 
            'pitcher_id'
        ]

        input_data = np.array([[data[feature] for feature in input_order]])
        input_scaled = scaler.transform(input_data)

        pred_class = model.predict(input_scaled)[0]
        pitch_group = encoder.inverse_transform([pred_class])[0]
        # Look up average velocity
        pitcher_id = data['pitcher_id']
        velocity = velocity_lookup.get((pitcher_id, pitch_group), "N/A")

        return jsonify({
            "predicted_pitch_type_group": pitch_group,
            "avg_velocity": velocity
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
