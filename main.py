from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field,field_validator
from fastapi.responses import JSONResponse
from typing import Annotated,List,Literal
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from xgboost import XGBRegressor
import pandas as pd
import numpy as np
import joblib

MODEL_FLOW='25.0.9.2025'
app=FastAPI(title="ENERGY CONSUMPTION MODEL",version=MODEL_FLOW,description="THIS API HELPS US TO SHOW HOW MUCH ENERGY WILL BE CONSUMED BASED ON INPUTS")

class Features(BaseModel):
    building_type:Literal['Residential', 'Commercial', 'Industrial']
    Square_Footage:Annotated[int,Field(description="SQUARE AREA",example=14000)]
    Number_of_Occupants:Annotated[int,Field(description="Number of occupants",example=3)]
    use:Annotated[int,Field(description="appliances used",example=2)]
    Temperature:Annotated[float,Field(description="avg temperature",example=34.5)]
    dayofweek:Literal['Weekday', 'Weekend']
    @field_validator('building_type')
    @classmethod
    def type(cls,value):
        value = value.capitalize()
        if value not in ['Residential', 'Commercial', 'Industrial']:
            raise ValueError("Invalid building_type")
        return value
class Output(BaseModel):
    power:float=Field(description="POWER CONSUMED BY USING THOSE FEATURES")




@app.get("/",tags=['About'])
def about():
    try:
        return "ENERGY CONSUMPTION MODEL RUNNING"
    except:
        return HTTPException(status_code=400,detail="INVALID DATA REQUEST")

@app.get("/health",tags=['Health'])
def health_check():
    return{"status":"RUNNING","version":MODEL_FLOW,"MODEL": True if model  else False}




model=joblib.load("Model/energy_consumption.pkl")

@app.post("/predict",tags=['Prediction'],response_model=Output)
def predict(data:Features):
    value = pd.DataFrame([[
        data.building_type,
        data.Square_Footage,
        data.Number_of_Occupants,
        data.use,
        data.Temperature,
        data.dayofweek
    ]], columns=model.feature_names_in_)
    try:
        value=model.predict(value).tolist()
        # conf = model.predict_proba(value)[0].max() if hasattr(model, "predict_proba") else None ONly work for classification models
        return JSONResponse(status_code=200,content={"power_consumption": value[0]})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
