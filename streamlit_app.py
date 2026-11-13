import streamlit as st
import pandas as pd
import requests

st.title("Phishing URL Detection App")
st.write("Please enter the following website features to predict whether the website is phishing or legitimate:")

URLLength = st.number_input("URL Length", min_value=0, value=0)
DomainLength = st.number_input("Domain Length", min_value=0, value=0)
IsDomainIP = st.selectbox("Is Domain IP", [0, 1])
CharContinuationRate = st.number_input("Character Continuation Rate", min_value=0.0, value=0.0)
TLDLegitimateProb = st.number_input("TLD Legitimate Probability", min_value=0.0, value=0.0)
URLCharProb = st.number_input("URL Character Probability", min_value=0.0, value=0.0)
TLDLength = st.number_input("TLD Length", min_value=0, value=0)
NoOfSubDomain = st.number_input("Number of Subdomains", min_value=0, value=0)
HasObfuscation = st.selectbox("Has Obfuscation", [0, 1])
NoOfObfuscatedChar = st.number_input("Number of Obfuscated Characters", min_value=0, value=0)
ObfuscationRatio = st.number_input("Obfuscation Ratio", min_value=0.0, value=0.0)
NoOfLettersInURL = st.number_input("Number of Letters in URL", min_value=0, value=0)
LetterRatioInURL = st.number_input("Letter Ratio in URL", min_value=0.0, value=0.0)
NoOfDegitsInURL = st.number_input("Number of Digits in URL", min_value=0, value=0)
DegitRatioInURL = st.number_input("Digit Ratio in URL", min_value=0.0, value=0.0)
NoOfEqualsInURL = st.number_input("Number of Equals in URL", min_value=0, value=0)
NoOfQMarkInURL = st.number_input("Number of Question Marks", min_value=0, value=0)
NoOfAmpersandInURL = st.number_input("Number of Ampersands", min_value=0, value=0)
NoOfOtherSpecialCharsInURL = st.number_input("Number of Other Special Characters", min_value=0, value=0)
SpacialCharRatioInURL = st.number_input("Special Character Ratio", min_value=0.0, value=0.0)
IsHTTPS = st.selectbox("Is HTTPS", [0, 1])

LineOfCode = st.number_input("Line of Code", min_value=0, value=0)
LargestLineLength = st.number_input("Largest Line Length", min_value=0, value=0)
HasTitle = st.selectbox("Has Title", [0, 1])
DomainTitleMatchScore = st.number_input("Domain Title Match Score", min_value=0.0, value=0.0)
URLTitleMatchScore = st.number_input("URL Title Match Score", min_value=0.0, value=0.0)
HasFavicon = st.selectbox("Has Favicon", [0, 1])
Robots = st.selectbox("Robots", [0, 1])
IsResponsive = st.selectbox("Is Responsive", [0, 1])
NoOfURLRedirect = st.number_input("Number of URL Redirects", min_value=0, value=0)
NoOfSelfRedirect = st.number_input("Number of Self Redirects", min_value=0, value=0)
HasDescription = st.selectbox("Has Description", [0, 1])
NoOfPopup = st.number_input("Number of Popups", min_value=0, value=0)
NoOfiFrame = st.number_input("Number of iFrames", min_value=0, value=0)

HasExternalFormSubmit = st.selectbox("Has External Form Submit", [0, 1])
HasSocialNet = st.selectbox("Has Social Network", [0, 1])
HasSubmitButton = st.selectbox("Has Submit Button", [0, 1])
HasHiddenFields = st.selectbox("Has Hidden Fields", [0, 1])
HasPasswordField = st.selectbox("Has Password Field", [0, 1])
Bank = st.selectbox("Bank", [0, 1])
Pay = st.selectbox("Pay", [0, 1])
Crypto = st.selectbox("Crypto", [0, 1])
HasCopyrightInfo = st.selectbox("Has Copyright Information", [0, 1])

NoOfImage = st.number_input("Number of Images", min_value=0, value=0)
NoOfCSS = st.number_input("Number of CSS Files", min_value=0, value=0)
NoOfJS = st.number_input("Number of JavaScript Files", min_value=0, value=0)
NoOfSelfRef = st.number_input("Number of Self References", min_value=0, value=0)
NoOfEmptyRef = st.number_input("Number of Empty References", min_value=0, value=0)
NoOfExternalRef = st.number_input("Number of External References", min_value=0, value=0)


if st.button("Predict"):

    input_data = {
        "URLLength": URLLength,
        "DomainLength": DomainLength,
        "IsDomainIP": IsDomainIP,
        "CharContinuationRate": CharContinuationRate,
        "TLDLegitimateProb": TLDLegitimateProb,
        "URLCharProb": URLCharProb,
        "TLDLength": TLDLength,
        "NoOfSubDomain": NoOfSubDomain,
        "HasObfuscation": HasObfuscation,
        "NoOfObfuscatedChar": NoOfObfuscatedChar,
        "ObfuscationRatio": ObfuscationRatio,
        "NoOfLettersInURL": NoOfLettersInURL,
        "LetterRatioInURL": LetterRatioInURL,
        "NoOfDegitsInURL": NoOfDegitsInURL,
        "DegitRatioInURL": DegitRatioInURL,
        "NoOfEqualsInURL": NoOfEqualsInURL,
        "NoOfQMarkInURL": NoOfQMarkInURL,
        "NoOfAmpersandInURL": NoOfAmpersandInURL,
        "NoOfOtherSpecialCharsInURL": NoOfOtherSpecialCharsInURL,
        "SpacialCharRatioInURL": SpacialCharRatioInURL,
        "IsHTTPS": IsHTTPS,
        "LineOfCode": LineOfCode,
        "LargestLineLength": LargestLineLength,
        "HasTitle": HasTitle,
        "DomainTitleMatchScore": DomainTitleMatchScore,
        "URLTitleMatchScore": URLTitleMatchScore,
        "HasFavicon": HasFavicon,
        "Robots": Robots,
        "IsResponsive": IsResponsive,
        "NoOfURLRedirect": NoOfURLRedirect,
        "NoOfSelfRedirect": NoOfSelfRedirect,
        "HasDescription": HasDescription,
        "NoOfPopup": NoOfPopup,
        "NoOfiFrame": NoOfiFrame,
        "HasExternalFormSubmit": HasExternalFormSubmit,
        "HasSocialNet": HasSocialNet,
        "HasSubmitButton": HasSubmitButton,
        "HasHiddenFields": HasHiddenFields,
        "HasPasswordField": HasPasswordField,
        "Bank": Bank,
        "Pay": Pay,
        "Crypto": Crypto,
        "HasCopyrightInfo": HasCopyrightInfo,
        "NoOfImage": NoOfImage,
        "NoOfCSS": NoOfCSS,
        "NoOfJS": NoOfJS,
        "NoOfSelfRef": NoOfSelfRef,
        "NoOfEmptyRef": NoOfEmptyRef,
        "NoOfExternalRef": NoOfExternalRef
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=input_data
        )

        if response.status_code == 200:

            result = response.json()

            if result == "Phishing":
                st.warning("Prediction: Phishing Website")

            else:
                st.success("Prediction: Legitimate Website")

        else:
            st.error(f"Error occurred: {response.status_code} - {response.text}")

    except requests.RequestException as e:
        st.error(f"Error occurred while making the request: {e}")
