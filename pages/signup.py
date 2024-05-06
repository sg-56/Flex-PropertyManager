import streamlit as st
from menu import menu
import streamlit_shadcn_ui as ui
from Utils import check_password_strength,CheckUserNameExists,InsertNewUser


menu() # Render the dynamic menu!
cols = st.columns([1,1])
with cols[1]:
   st.image(image="images/login.jpeg")
with cols[0]:
    with st.form(key = "User_Signup"):
        st.markdown("##### Select User Type: ")
        user_type = ui.tabs(options=["Owner","Manager","Tenant"],default_value="Owner",key = "user_role")
        username = st.text_input(label="Username",placeholder="Username is Unique to every user",key="username")
        f_name = st.text_input(label="Enter Your First Name",key = "firstname")
        l_name  = st.text_input(label="Enter Your Last Name",key = "lastname")
        email  = st.text_input(label="Enter Your Email",key = "email")
        password = st.text_input(label="Enter Your Password",type="password")
        phone = st.text_input(label="Enter your Contact Number",key = "phone",max_chars=10)
        adress = st.text_area(label="Enter Your Current Adress",key="adress")
        submit_button = st.form_submit_button(label="Submit",use_container_width=False)
        if submit_button:
            if('@' not in email):
                st.error("Enter a valid Email Adress")
                st.stop() 

            if (check_password_strength(password=password)): ##Checking Password
                if CheckUserNameExists(username=username):
                   if (InsertNewUser(username=username,
                                  first_name=f_name,
                                  last_name=l_name,
                                  email=email,
                                  password=password,
                                  phone=phone,
                                  adress=adress,
                                  usertype=user_type)):
                    st.toast("User Successfully Created!!")
                    st.switch_page("app.py")
