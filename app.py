from flask import Flask, render_template, request, jsonify
#from keras.models import load_model
import numpy as np
import joblib

# Load the RandomForestRegressor model from the joblib file
loaded_model = joblib.load('rf_model.joblib')

# Now you can use the loaded_model for predictions
predict()
#predictions = loaded_model.predict(scale_input)

app = Flask(__name__)

# Load your trained model
#model = load_model('flood_prediction_model.h5')

# Your scaling function if you used StandardScaler
def scale_input(input_data):
    # Implement your scaling logic here
    return input_data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the UI form
        input_data = [float(request.form['feature1']),
                      float(request.form['feature2']),
                      float(request.form['feature3'])]

        # Scale the input data
        scaled_input = scale_input(np.array([input_data]))

        # Make a prediction using the loaded model
        prediction = loaded_model.predict(scaled_input)[0][0]

        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
