import streamlit as st
from xai_sdk import Client
from xai_sdk.chat import system, user
from dotenv import load_dotenv
import os

# Load environment variables (local) or secrets (cloud)
load_dotenv()  # For local .env
api_key = os.getenv("XAI_API_KEY") or os.getenv("GROK_API_KEY")  # Local fallback
if "XAI_API_KEY" in st.secrets:  # Use Streamlit secrets for cloud
    api_key = st.secrets["XAI_API_KEY"]
if not api_key:
    st.write("Debug: API Key:", api_key)
    st.error("API key not found. Ensure secrets are configured in Streamlit Cloud or .env locally.")
    st.stop()

# Initialize client
client = Client(api_key=api_key)

# App layout
st.title("AdvocateAI - Insurance Appeal Assistant")
st.write("This tool helps you draft appeal letters for insurance denials. Enter 'denial' to start.")

# User input
user_input = st.text_input("What do you need help with?", key="user_input")
if st.button("Submit") or user_input.lower() == "denial":
    if "denial" in user_input.lower():
        with st.form(key="appeal_form_v1"):
            st.write("Provide details to draft your appeal letter.")
            name = st.text_input("Your Full Name")
            street = st.text_input("Street Address")
            city_state_zip = st.text_input("City, State, ZIP Code")
            email = st.text_input("Your Email Address")
            phone = st.text_input("Your Phone Number")
            date = st.date_input("Date")
            insurance = st.text_input("Insurance Company")
            denied = st.text_input("What was denied? (e.g., MS medication)")
            policy = st.text_input("Policy Number (optional)")
            ins_address = st.text_input("Insurance Address (from denial letter, optional)")
            medical_need = st.text_area("Why is this needed? (optional)", "Essential for my health.")
            submit_button = st.form_submit_button("Generate Appeal")

            if submit_button:
                # Check for required fields
                required_fields = [name, street, city_state_zip, email, phone, date, insurance, denied]
                if not all(required_fields):
                    st.error("Please fill all required fields.")
                else:
                    chat = client.chat.create(model="grok-4-0709", temperature=0)
                    chat.append(system("You are an expert in healthcare advocacy, drafting clear, concise, and formal appeal letters for insurance denials. Include a subject line, brief medical necessity, a request for a 30-day response, and use line breaks for addresses."))
                    chat.append(user(f"Generate a concise appeal letter with Name: {name}, Address: '{street}\\n{city_state_zip}', Email: {email}, Phone: {phone}, Date: {date.strftime('%Y-%m-%d')}, Insurance Company: {insurance}, Insurance Address: '{ins_address if ins_address else '[Insert address from denial letter]'}', What was denied: {denied}, Policy Number: {policy if policy else 'N/A'}, Medical Necessity: {medical_need if medical_need else 'Essential for my health.'}."))
                    response = chat.sample()
                    letter = response.content
                    st.write("### Your Appeal Letter")
                    st.write(letter)
    else:
        st.write("Enter 'denial' to start an insurance appeal.")

# Basic accessibility
st.markdown("""
    <style>
    .stTextInput > div > input { font-size: 16px; }
    .stButton > button { height: 48px; font-size: 16px; }
    body { color: #000000; background-color: #FFFFFF; }
    .stError { font-size: 16px; }
    </style>
""", unsafe_allow_html=True)
