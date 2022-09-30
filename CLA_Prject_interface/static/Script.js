const form = document.querySelector("form"),
  sumbitBtn = form.querySelector(".sumbit"),
  allInput = form.querySelectorAll(".form input");
allselectedvalues = form.querySelectorAll(".form select");

sumbitBtn.addEventListener("click", () => {
  let list = [];
  allInput.forEach((input) => {
    if (input.value != "") {
      list.push(input.value);
    }
  });
  allselectedvalues.forEach((selected) => {
    if (selected.value != "") {
      list.push(selected.value);
    }
    console.log(list);
    //all the data from the form is stocked in the list array
    //order is : age / bmi / Average Glucose level / gender / How often does the patient smoke? /
    //Does the patient have hypertension/Has the patient ever been married/
    //Does the patient have heart disease/What type of work does the patient do/
    //In what type of residance does the patient live
  });
});
//get the accuracy

function getprobability(proba) {
  //use the variable list to get the accuracy
  let d = proba; //lets assume this is the accuracy
  if (d < 50) {
    document.getElementById("dynamic").innerHTML =
      "<span class='green'>less</span>";
    document.getElementById("cercle").innerHTML =
      "<div class='cercle greencercle'><span class='prediction'>" +
      d +
      "%</span></div>";
  } else {
    document.getElementById("dynamic").innerHTML =
      "<span class='red'>more</span>";
    document.getElementById("cercle").innerHTML =
      "<div class='cercle redcercle'> <span class='prediction'>" +
      d +
      "%</span></div>";
  }
}
