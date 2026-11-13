from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
model = joblib.load("phishing_url_rand_svc.pkl")
app = FastAPI(title="Phishing URL Detection API", description="API for detecting phishing URLs using a pre-trained model.", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class input_data(BaseModel):
    URLLength: float
    DomainLength: float
    IsDomainIP: float
    CharContinuationRate: float
    TLDLegitimateProb: float
    URLCharProb: float
    TLDLength: float
    NoOfSubDomain: float
    HasObfuscation: float
    NoOfObfuscatedChar: float
    ObfuscationRatio: float
    NoOfLettersInURL: float
    LetterRatioInURL: float
    NoOfDegitsInURL: float
    DegitRatioInURL: float
    NoOfEqualsInURL: float
    NoOfQMarkInURL: float
    NoOfAmpersandInURL: float
    NoOfOtherSpecialCharsInURL: float
    SpacialCharRatioInURL: float
    IsHTTPS: float
    LineOfCode: float
    LargestLineLength: float
    HasTitle: float
    DomainTitleMatchScore: float
    URLTitleMatchScore: float
    HasFavicon: float
    Robots: float
    IsResponsive: float
    NoOfURLRedirect: float
    NoOfSelfRedirect: float
    HasDescription: float
    NoOfPopup: float
    NoOfiFrame: float
    HasExternalFormSubmit: float
    HasSocialNet: float
    HasSubmitButton: float
    HasHiddenFields: float
    HasPasswordField: float
    Bank: float
    Pay: float
    Crypto: float
    HasCopyrightInfo: float
    NoOfImage: float
    NoOfCSS: float
    NoOfJS: float
    NoOfSelfRef: float
    NoOfEmptyRef: float
    NoOfExternalRef: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Phishing URL Detection API"}
@app.post("/predict")
def predict(data: input_data):
    input_df = pd.DataFrame([data.model_dump()])
    prediction = model.predict(input_df)


    return "Phishing" if prediction[0] == 0 else "Legitimate"