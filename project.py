from flask import Flask, render_template, request,redirect
import pandas as pd
import joblib
from predict import load_model_1, load_model_2, predict
app = Flask(__name__)



@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
      print('submitted')
      user_name = request.form.get('user_Name')
      visit_date = request.form.get('Visit')
      mr_delay = request.form.get('MR Delay')
      mf = request.form.get('Male/Female')
      hand = request.form.get('Right/Left')
      age = request.form.get('Age')
      educ = request.form.get('educ') 
      ses = request.form.get('SES')
      mmse = request.form.get('MMSE') 
      cdr = request.form.get('CDR')
      etiv = request.form.get('eTIV')
      nwbv = request.form.get('nWBV')
      asf = request.form.get('ASF')
      data = [user_name,visit_date,mr_delay,mf,
              hand,age,educ,ses,mmse,cdr,etiv,nwbv,asf]
      prediction = predict(load_model_1(), visit_date, mr_delay, mf, age, educ, ses, mmse, cdr, etiv, nwbv, asf)
      if prediction == 0:
        prediction = 'Converted'
      elif prediction == 1:
        prediction = 'Dementia'
      else:
        prediction = 'Normal'
      return render_template('result.html', prediction=prediction, data=data)
    return render_template('form.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('Form.html')
@app.route('/about' )
def About():
    return render_template('About.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
