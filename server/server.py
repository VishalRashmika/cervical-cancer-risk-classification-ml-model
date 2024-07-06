from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/predict_diabetes', methods=['GET', 'POST'])
def predict_home_price():
    Pregnancies = float(request.form['t_Pregnancies'])
    Glucose = float(request.form['t_Glucose'])
    BloodPressure = float(request.form['t_BloodPressure'])
    SkinThickness = float(request.form['t_SkinThickness'])
    Insulin = float(request.form['t_Insulin'])
    BMI = float(request.form['t_BMI'])
    DiabetesPedigreeFunction = float(request.form['t_DiabetesPedigreeFunction'])
    Age = float(request.form['t_Age'])

    response = jsonify({
        'prediction': int(util.get_est_prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)[0])
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Diabetes Pediction...")
    util.load_saved_artifacts()
    app.run()