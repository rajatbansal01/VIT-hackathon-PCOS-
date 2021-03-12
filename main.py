import uvicorn ##ASGI
from fastapi import FastAPI
from pcos import PCOS
import numpy as np
import pickle
import pandas as pd
from pydantic import BaseModel
# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)
# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

@app.post('/predict')
def predict_pcos(data:PCOS):
    data = data.dict()
    age=data["Age"]
    weight=data["Weight"]
    height=data["Height"]
    cycle=data["Cycle"]
    cyclelength=data["Cyclelength"]
    fsh=data["Fsh"]
    lh=data["Lh"]
    frl=data["Frl"]
    tsh=data["Tsh"]
    amh=data["Amh"]
    rbs=data["Rbs"]
    weightgain=data["Weightgain"]
    hairgrowth=data["Hairgrowth"]
    skindarkening=data["Skindarkening"]
    hairloss=data["Hairloss"]
    pimples=data["Pimples"]
    fastfood=data["Fastfood"]
    regexercise=data["Regexercise"]
    follicleR=data["FollicleR"]
    folliclL=data["FolliclL"]
    prediction = classifier.predict([[age,weight,height,cycle,cyclelength,fsh,lh,frl,tsh,amh,rbs,
    weightgain,hairgrowth,skindarkening,hairloss,pimples,fastfood,regexercise,follicleR,folliclL]])
    if(prediction[0]>0.5):
        pred="Yes"
    else:
        pred="No"
    return {
        'prediction': pred ,
        'probablity': float(prediction[0])
    }


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload

