from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("rainfall_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_features = []

        # Default values (realistic weather values)
        defaults = [60, 1010, 65, 0, 7, 1012, 20, 28, 18, 32]

        # Loop through inputs f1 to f10
        for i in range(1, 11):
            value = request.form.get(f"f{i}")

            if value is None or value.strip() == "":
                input_features.append(defaults[i-1])
            else:
                input_features.append(float(value))

        final_features = np.array([input_features])

        prediction = model.predict(final_features)

        result = "🌧️ Rainfall Expected" if prediction[0] == 1 else "☀️ No Rainfall"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)