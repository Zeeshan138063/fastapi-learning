from fastapi import FastAPI
import seaborn as sns

import pandas as pd

app = FastAPI()

# load the titanic dataset
df = sns.load_dataset("titanic")

# perform a simple data transformation
survival_rate = df.groupby("class")["survived"].mean().reset_index()

 
@app.get("/")
async def root():
    return {"Hello": "Welcome to the titanic API we are learning with Zeeshan"}

@app.get("/survival_rate")
async def get_survival_rate():
    return survival_rate.to_dict(orient="records")
 

