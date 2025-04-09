from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model, scaler, label encoder
model = joblib.load("../results/xgb_pitch_predictor_model.pkl")
scaler = joblib.load("../results/scaler.pkl")
encoder = joblib.load("../results/group_label_encoder.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        input_order = [
            'stand', 'balls', 'strikes', 'inning', 'outs_when_up',
            'on_1b', 'on_2b', 'on_3b',
            'pitch_count', 'score_diff', 'is_home_team',
            'batter_id', 'pitcher_id'
        ]

        input_data = np.array([[data[feature] for feature in input_order]])
        input_scaled = scaler.transform(input_data)

        pred_class = model.predict(input_scaled)[0]
        pitch_group = encoder.inverse_transform([pred_class])[0]

        return jsonify({"predicted_pitch_type_group": pitch_group})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
