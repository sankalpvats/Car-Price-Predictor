🚗 Car Price Prediction Model
This project is a machine learning-based web application that predicts the price of a used car based on factors like car brand, model, fuel type, age, and kilometers driven. The model is built using XGBoost Regressor, and the web interface is powered by Flask.

📌 Features
✅ Predicts car prices based on input parameters
✅ Uses XGBoost Regressor for high accuracy
✅ Web-based UI using Flask & HTML/CSS
✅ Interactive dropdowns for car brand & model
✅ Deployed locally or on cloud platforms

📊 Dataset
The dataset used contains the following features:

Name (Car Model)
Company (Brand)
Year (Car Age)
Kms Driven
Fuel Type
Price (Target Variable)
Data was cleaned, preprocessed, and encoded before training the model.

🛠 Technologies Used
🔹 Python (Pandas, NumPy, Scikit-Learn, XGBoost)
🔹 Flask (For Web App)
🔹 HTML / CSS (For Frontend)
🔹 Matplotlib / Seaborn (For Data Visualization)
🔹 GitHub (Version Control)

🚀 How to Run Locally
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Flask App
bash
Copy
Edit
python app.py
🌐 Open http://127.0.0.1:5000/ in your browser.

📌 Model Performance
R² Score: 0.919
Algorithm Used: XGBoost Regressor
Hyperparameter Tuning: Yes (GridSearchCV)
