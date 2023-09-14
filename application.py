from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__, template_folder="templates")

# Load the trained model and scaler
model = joblib.load("models/best_xgboost_model.pkl")
scaler = joblib.load("models/data_scaler.pkl")

@app.route('/', methods=['GET', 'POST'])
def index():
    formatted_prediction = None
    if request.method == 'POST':
        # Get data from the form for all 13 features
        crim = float(request.form['crim'])
        zn = float(request.form['zn'])
        indus = float(request.form['indus'])
        chas = float(request.form['chas'])
        nox = float(request.form['nox'])
        rm = float(request.form['rm'])
        age = float(request.form['age'])
        dis = float(request.form['dis'])
        rad = float(request.form['rad'])
        tax = float(request.form['tax'])
        ptratio = float(request.form['ptratio'])
        b = float(request.form['b'])
        lstat = float(request.form['lstat'])

        # Create a 2D array from the input data
        data = np.array([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]])

        # Scale the data
        scaled_data = scaler.transform(data)

        # Make prediction
        prediction = model.predict(scaled_data)[0]

        # Format the prediction with thousands separators and two decimal places
        formatted_prediction = "${:,.2f} (in thousands of dollars)".format(prediction).replace(",", " ")

    return render_template('index.html', prediction=formatted_prediction)

if __name__ == "__main__":
    app.run(debug=True)



