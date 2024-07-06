function onClickedPrediction() {
  console.log("Prediction button clicked");
  var Pregnancies = document.getElementById("uipregnancies")
  var Glucose = document.getElementById("uiglucose")
  var BloodPressure = document.getElementById("uibloodpressure")
  var SkinThickness = document.getElementById("uiskinthickness")
  var Insulin = document.getElementById("uiinsulin")
  var BMI = document.getElementById("uibmi")
  var DiabetesPedigreeFunction = document.getElementById("uiDPF")
  var Age = document.getElementById("uiage")

  var estPrediction = document.getElementById("uiPrediction");

  var url = "http://127.0.0.1:5000/predict_diabetes";

  $.post(url, {
      t_Pregnancies: parseFloat(Pregnancies.value),
      t_Glucose: parseFloat(Glucose.value),
      t_BloodPressure: parseFloat(BloodPressure.value),
      t_SkinThickness: parseFloat(SkinThickness.value),
      t_Insulin: parseFloat(Insulin.value),
      t_BMI: parseFloat(BMI.value),
      t_DiabetesPedigreeFunction: parseFloat(DiabetesPedigreeFunction.value),
      t_Age: parseFloat(Age.value)
  },function(data, status) {
      console.log(data.est_prediction);
      var prediction = data.prediction;
      console.log(prediction)
      if (prediction == 1){
        estPrediction.innerHTML = "<h2>" + "Positive" + " :(</h2>";
      }
      else if (prediction == 0){
        estPrediction.innerHTML = "<h2>" + "Negative" + " :)</h2>";
      }
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "page loaded" );
}

window.onload = onPageLoad;
