import streamlit as st
from menu import menu_with_redirect
import pandas as pd


# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()
import streamlit_shadcn_ui as ui
from PIL import Image
from Utils import redirect,update_password,check_password_strength
import io


def render_user():
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
                "Photo":userdb["profile_picture"][0]

    }   
    st.session_state["Current user"] = userdata        
    #st.write(userdata)
    cols = st.columns([1,0.5,3])
    with cols[0]:
        if userdata["Photo"] is None:
            st.image(image="images/user.png",width=200,use_column_width=True)

        imgupload = st.button(label="Change Profile Picture",use_container_width=True)
        prof = st.button(label="Change Password",use_container_width=True)

        if prof:
                redirect("pages/changepassword.py")
        if imgupload:
             redirect("pages/imageupload.py")   


    with cols[2]:
        for key in userdata:
            if key not in ["Password","User ID","Photo"]:
                st.write(f"{key} : {userdata[key]}")
        upd_prof = st.button(label="Update Profile")
        if upd_prof:
             redirect("pages/updateprofile.py")
                    

render_user()


