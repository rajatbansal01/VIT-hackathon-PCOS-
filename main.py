import uvicorn ##ASGI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pcos import PCOS
import numpy as np
import pickle
import pandas as pd
from pydantic import BaseModel
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # to solve the CORS problem
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# get request
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To the Project Femow': f'{name}'}
 # post a json file to predict results.
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


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# to run the app locally use
#uvicorn main:app --reload

