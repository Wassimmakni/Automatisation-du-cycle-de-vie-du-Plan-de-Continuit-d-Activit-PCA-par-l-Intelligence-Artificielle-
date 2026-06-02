from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()
@app.get("/")
def home():
    return {"message": "API OK"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # autorise React
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

    return df.to_dict(orient="records")

@app.post("/upload/")
def upload_file(file: UploadFile = File(...)):
    return lire_fichier(file)
