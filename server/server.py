from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/predict_cervical_cancer', methods=['GET', 'POST'])
def predict_home_price():
    age = float(request.form['t_age'])
    no_sex_partners = float(request.form['t_no_sex_partners'])
    first_sex_intercourse = float(request.form['t_first_sex_intercourse'])
    no_pregnancies = float(request.form['t_no_pregnancies'])
    smokes = float(request.form['t_smokes'])
    smokes_year = float(request.form['t_smokes_year'])

    response = jsonify({
        'prediction': int(util.get_est_prediction(age,no_sex_partners,first_sex_intercourse,no_pregnancies,smokes,smokes_year)[0])
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Cervical Cancer Pediction...")
    util.load_saved_artifacts()
    app.run()