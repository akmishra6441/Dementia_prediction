import joblib
import pandas as pd

def load_model_1():
    return joblib.load(r'models\gb_model2.pkl')

def load_model_2():
    return joblib.load(r'models\rf_model2.pkl')

def predict(model, visit, mr_delay, mf, age, educ, ses, mmse, cdr, etiv, nwbv, asf):
    data = pd.DataFrame({
        'Visit': [visit],
        'MR Delay': [mr_delay],
        'M/F': [mf],
        'Age': [age],
        'EDUC': [educ],
        'SES': [ses],
        'MMSE': [mmse],
        'CDR': [cdr],
        'eTIV': [etiv],
        'nWBV': [nwbv],
        'ASF': [asf]
    })
    return model.predict(data)[0]