# Import necessary libraries
from flask import Flask, render_template, request
import joblib

# Load the machine learning model
model = joblib.load('rf_model.joblib')

# Create Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('results2.html')

# Define a route for handling predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    date = request.form['date']
    month = request.form['month']
    year = request.form['year']
    flow = float(request.form['flow'])
    rainfall = float(request.form['rainfall'])

    # Make a prediction using the loaded model
    input_data = [[date, month, year, flow, rainfall]]
    prediction = model.predict(input_data)

    # Render the result on a new page
    return render_template('results.html', prediction=prediction)

if __name__ == '__main__':
    # Run the app on localhost:5000
    app.run(debug=True)
