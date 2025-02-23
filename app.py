from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("LinearRegression.pkl")

# Define route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        car_name = request.form['name']
        company = request.form['company']
        year = int(request.form['year'])
        kms_driven = int(request.form['kms_driven'])
        fuel_type = request.form['fuel_type']

        # Create DataFrame for prediction
        input_data = pd.DataFrame([[car_name, company, year, kms_driven, fuel_type]], 
                                  columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

        # Make prediction
        prediction = model.predict(input_data)

        # Convert to integer price
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f'Estimated Price: ₹{output}')

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
