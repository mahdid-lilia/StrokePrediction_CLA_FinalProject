from flask import Flask, render_template, redirect, request, url_for
import joblib
import pandas as pd

app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def welcome():
    return render_template('form.html')  # render a template


@app.route('/prediction/<prob>')
def success(prob):
    return render_template('Response.html',proba=prob)
 
 
@app.route('/prediction', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        
        age = request.form['age']
        gender = request.form['gender']
        hypertension = request.form['hypertension']
        hypertension = 1 if hypertension == "yes" else 0
        
        heartdisease = request.form['heartdisease']
        heartdisease = 1 if heartdisease == "yes" else 0
        
        avg_gl = request.form["glucose"]
        
        bmi = request.form["bmi"]
        
        smoke = request.form["smoke"]
        smoke = "Unknown" if smoke == "choose not to reveal" else smoke
        
        married = request.form["married"]
        
        job_types = {"Government job":"Govt_job" ,
                     "Never worked":"Never_worked",
                     "Children":"children",
                     "Self-employed":"Self-employed",
                     "Private job":"Private"}
        job = request.form["job"]
        
        residence = request.form["residence"]
        
        # load the model from disk
        loaded_model = joblib.load('./models/random_forest_clf.sav')
        # Load the standard scaler
        loaded_std = joblib.load("./models/std_scaler.bin")
        # Load the encoder
        loaded_enc = joblib.load("./models/label_enc.bin")
        
        entry = [[gender, age, hypertension, heartdisease,
                  married, job, 
                  residence, avg_gl, bmi,
                  smoke]]
        
        col = ["gender","age","hypertension","heart_disease",
               "ever_married","work_type",
               "Residence_type","avg_glucose_level","bmi",
               "smoking_status"]
         	 	 	 	 	 	 	
        entry = pd.DataFrame(columns=col, data=entry)
        
        gender=loaded_enc.fit_transform(entry['gender'])
        smoking_status=loaded_enc.fit_transform(entry['smoking_status'])
        work_type=loaded_enc.fit_transform(entry['work_type'])
        Residence_type=loaded_enc.fit_transform(entry['Residence_type'])
        ever_married=loaded_enc.fit_transform(entry['ever_married'])

        entry['work_type']=work_type
        entry['ever_married']=ever_married
        entry['Residence_type']=Residence_type
        entry['smoking_status']=smoking_status
        entry['gender']=gender
        
        test = loaded_std.transform(entry)
        
        #prediction = loaded_model.predict(test)
        proba = loaded_model.predict_proba(test)[0][1]*100 # probability of being in danger of a stroke
        
        return redirect(url_for('success', prob=proba))
    else:
        #user = request.args.get('nm')
        return redirect(url_for('success', name=49))






# start the server with the 'run()' method
if __name__ == '__main__':
    app.debug = True
    app.run()

