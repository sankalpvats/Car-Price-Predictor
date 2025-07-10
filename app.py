from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("Clean Data.csv")  
model = joblib.load("LinearRegression.pkl")

@app.route('/')
def home():

    car_names = sorted(df['name'].unique())
    companies = sorted(df['company'].unique())
    years = sorted(df['year'].unique())

    return render_template(
        'index.html',
        car_names=car_names,
        companies=companies,
        years=years
    )

@app.route('/predict', methods=['POST'])
def predict():
    try:
        car_name = request.form['name']
        company = request.form['company']
        year = int(request.form['year'])
        kms_driven = int(request.form['kms_driven'])
        fuel_type = request.form['fuel_type']

        input_data = pd.DataFrame([[car_name, company, year, kms_driven, fuel_type]],
                                  columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

        prediction = model.predict(input_data)
        output = round(prediction[0], 2)

        return render_template('index.html',
                               prediction_text=f'Estimated Price: ₹{output:.2f}',
                               car_names=sorted(df['name'].unique()),
                               companies=sorted(df['company'].unique()),
                               years=sorted(df['year'].unique()))

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
