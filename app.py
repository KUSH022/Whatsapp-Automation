import pandas as pd
import pywhatkit
import streamlit as st

def read_excel(file_path):
    data = pd.read_excel(file_path, dtype={'Phone Number': str})
    return data

def send_whatsapp_message(name, phone_number, message, country_code='+91'):
    if not phone_number.startswith('+'):
        phone_number = country_code + phone_number
    
    personalized_message = message.replace("{name}", name)
    pywhatkit.sendwhatmsg_instantly(phone_number, personalized_message, wait_time=15, tab_close=True)

def main():
    st.title("WhatsApp Message Automation")
    
    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])
    message = st.text_area("Enter your message (use {name} as a placeholder for the recipient's name)")
    
    if uploaded_file is not None and message:
        data = read_excel(uploaded_file)
        st.write(data)
        
        if st.button("Send Messages"):
            for index, row in data.iterrows():
                send_whatsapp_message(row['Name'], row['Phone Number'], message)
            st.success("Messages sent successfully!")
        
if __name__ == "__main__":
    main()
