function onClickedPrediction() {
  console.log("Prediction button clicked");
  var age = document.getElementById("uiage")
  var no_sex_partners = document.getElementById("uino_sex_partners")
  var first_sex_intercourse = document.getElementById("uifirst_sex_intercourse")
  var no_pregnancies = document.getElementById("uino_pregnancies")
  var smokes = document.getElementById("uismokes")
  var smokes_year = document.getElementById("uismokes_year")

  var estPrediction = document.getElementById("uiPrediction");

  var url = "http://127.0.0.1:5000/predict_cervical_cancer";

  $.post(url, {
      t_age : parseFloat(age.value),
      t_no_sex_partners : parseFloat(no_sex_partners.value),
      t_first_sex_intercourse : parseFloat(first_sex_intercourse.value),
      t_no_pregnancies : parseFloat(no_pregnancies.value),
      t_smokes : parseFloat(smokes.value),
      t_smokes_year : parseFloat(smokes_year.value)
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

/*
age
no_sex_partners
first_sex_intercourse
no_pregnancies
smokes
smokes_year
*/