from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from nlp import classifier_processus

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API OK"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def lire_fichier(file):

    if file.filename.endswith(".csv"):
        df = pd.read_csv(file.file)

    elif file.filename.endswith(".xlsx"):
        df = pd.read_excel(file.file)

    else:
        return {"erreur": "Format non supporté"}
    df["criticite"] = 0
    for index, row in df.iterrows():
        criticite = classifier_processus(row["processus"])
        df.at[index, "criticite"] = criticite


    return df.to_dict(orient="records")



@app.post("/upload/")
def upload_file(file: UploadFile = File(...)):
    return lire_fichier(file)