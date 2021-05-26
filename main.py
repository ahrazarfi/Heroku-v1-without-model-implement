import requests
import streamlit as st


DISEASES = {
    "Diabetic Retinopathy (Upload your retinal fundus images)": "dia",
    "Malaria (Upload cell image)": "mal",
    "Heart Checkup (Upload Cardiac image)": "oct"
}


st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("DISEASE PREDICTOR")

disease = st.selectbox("Choose the disease", [i for i in DISEASES.keys()])

if(disease == "Diabetic Retinopathy (Upload your retinal fundus images)"):
    disease_URL = "dia"
elif(disease == "Malaria (Upload cell image)"):
    disease_URL = "mal"
else:
    disease_URL = "oct"

image = st.file_uploader("Choose an image")


def disease_prediction_Handler(result):
    rem_list = ['empty', 'type'] # source: "https://www.kite.com/python/answers/how-to-remove-multiple-keys-from-a-dictionary-in-python"
    if(disease_URL=="dia"):
        for key in rem_list:
            del result[key]
    elif(disease_URL=="dia"):
        for key in rem_list:
            del result[key]
    else:
        for key in rem_list:
            del result[key]
    return result

if st.button("Analyze"):
    if image is not None and disease_URL is not None:
        files = {"file": image.getvalue()}
        res = requests.post(f"http://139.59.4.61:5000/{disease_URL}", files=files)

        # result = res.text # this converts the response into plain text

        result = res.json() # returns the response from the API in JSON format, returns a dictionary

        # result = json.loads(result) # while using got error "the JSON object must be str, bytes or bytearray, not dict",  ref: "https://stackoverflow.com/questions/42354001/python-json-object-must-be-str-bytes-or-bytearray-not-dict"

        result = disease_prediction_Handler(result)

        pairs = result.items()
        for key, value in pairs:
            st.write(value)
        # result = result['pred_val']
        # st.write(result)


