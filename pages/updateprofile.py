from menu import menu
menu()

import streamlit as st
from Utils import UpdateUser,LogOut

st.header("Update Profile")

userdb = st.session_state["Login_info"] 
userdata = {"User ID":userdb["user_id"][0],
                "First Name":userdb["first_name"][0],
                "Last Name":userdb["last_name"][0],
                "User Name":userdb["username"][0],
                "Email":userdb["email"][0],
                "Password" : userdb["password"][0],
                "Adress":userdb["Adress"][0],
                "Type":userdb["user_type"][0],
                "Phone Number":str(round(userdb["phonenumber"][0],0))[0:-2],
                "Photo":userdb["profile_picture"][0]}


with st.form(key = "User_Signup"):
        f_name = st.text_input(label="Enter Your First Name",key = "firstname",value=userdata["First Name"])
        l_name  = st.text_input(label="Enter Your Last Name",key = "lastname",value=userdata["Last Name"])
        email  = st.text_input(label="Enter Your Email",key = "email",value=userdata["Email"])
        phone = st.text_input(label="Enter your Contact Number",key = "phone",max_chars=10,value=userdata["Phone Number"])
        adress = st.text_area(label="Enter Your Current Adress",key="adress",value=userdata["Adress"])
        submit_button = st.form_submit_button(label="Submit",use_container_width=False)
        if submit_button:
            if('@' not in email):
                st.error("Enter a valid Email Adress")
                st.stop() 
            UpdateUser(first_name=f_name,
                       last_name=l_name,
                       email=email,
                       phone=phone,
                       adress=adress,user_id=userdata["User ID"])
            st.success("Profile Sucessfully Updated!!")
            LogOut()