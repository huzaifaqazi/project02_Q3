import streamlit as st
import re

st.set_page_config(page_title="🔒Password strength meter" , layout="wide")

st.title("🔒 Password strength meter")
st.markdown("""
## Welcome to the password strength meter!
This tool will help you determine the strength of your password.
""")

password = st.text_input("Enter Your Password", type="password")
feedback = []

score = 0
if password:
    if len(password) <= 8:
        score +=1
    else:    
        feedback.append("password is too short🔑")    
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score +=1
    else:
        feedback.append("password should contain both uppercase and lowercase letters🔑")
    if re.search("[0-9]", password):
        score +=1
    else:
        feedback.append("password should contain numbers🔑")
    if re.search("[_@$]", password):
        score +=1
    else:
        feedback.append("password should contain special characters🔑")
    if score == 4:
        feedback.append("password is strong🔒")
    elif score == 3:
        feedback.append("password is medium🔒") 
    else:
        feedback.append("password is weak🔑 make it strong")

    if feedback:
        st.markdown("### Feedback")
        for i in feedback:
            st.write(i)
else:
    st.write("Enter your password to get feedback")            

