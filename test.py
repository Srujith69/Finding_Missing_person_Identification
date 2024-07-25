import streamlit as st
from send_mail import SendMail
import uuid
sender_email = 'nakulchamariya373@gmail.com'
sender_password = 'gnhcjjvsjznxvodv'

def send_verification_code(receiver_email):
    try:
        code = str(uuid.uuid4())
        new_mail = SendMail([receiver_email], f'Verification code',
                            f"Your verififcation code is {code}", 
                            sender_email)
        new_mail.send(sender_password)
        return code,True
    except Exception as e:
        print(e)
        return code,False
        
email = st.text_input(label="Enter email address")
if st.button('Send'):
    code,status = send_verification_code(email)
    verification_code = st.text_input(label="Enter verification code")
    verify = False
    if st.button('Confirm'):
        if status:
            if code == verification_code:
                verify = True
                passw = st.text_input(label="Enter password")
                passw2 = st.text_input(label="Enter password again")
                if st.button('Signup'):
                    if passw == passw2:
                        st.markdown("> Signed up Succesfully. Please refresh and login with signed account.")
                    else:
                        st.markdown("> Password not matching.")
            else:
                st.markdown("> Verififcation code mismatch.")
        else:
            st.markdown("> Incorrect email. Please refresh and try again")
        
    if verify:
        st.header('Succesfully')
    
