# create flask api + streamlit for API Response Tester Dashboard application

import streamlit as st
import requests
import json

st.set_page_config(page_title="API Tester", layout="wide")

st.title("🚀 API Response Tester")

# INPUTS
url = st.text_input("Enter API URL")

method = st.selectbox("Method", ["GET", "POST"])

headers_input = st.text_area(
    "Headers (JSON format)",
    value='{\n  "Content-Type": "application/json"\n}'
)

payload_input = st.text_area(
    "POST Payload (JSON format)",
    value='{\n}'
)

if st.button("Send Request"):

    if not url:
        st.error("Please enter a URL")
        st.stop()

    try:
        headers = json.loads(headers_input)
        payload = json.loads(payload_input)
    except:
        st.error("Headers or Payload must be valid JSON")
        st.stop()

    with st.spinner("Sending request..."):

        response = requests.post(
            "http://127.0.0.1:5000/test-api",
            json={
                "url": url,
                "method": method,
                "headers": headers,
                "payload": payload
            }
        )

    if response.status_code != 200:
        st.error("Error from API")
        st.json(response.json())
    else:
        data = response.json()

        st.success("Request Completed")

        col1, col2 = st.columns(2)

        col1.metric("Status Code", data["status_code"])
        col2.metric("Response Time (ms)", data["response_time_ms"])

        st.subheader("Response Body")
        st.json(data["body"])

        st.subheader("Response Headers")
        st.json(data["headers"])