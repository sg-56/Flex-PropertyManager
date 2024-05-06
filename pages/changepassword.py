import streamlit as st
from Utils import check_password_strength,update_password
from menu import menu
menu()

cols = st.columns([1,2])
with cols[0]:
    newpass = st.text_input(label="New Password")
    confirmpass = st.text_input(label="Confirm Password")
    update = st.button(label="Update")
    id = st.session_state.Login_info["user_id"][0]
    if update:
        if(newpass != confirmpass):
            st.error("Password Does Not Match")
            check_password_strength(newpass)
        else:
            update_password(id = id,new_password=newpass)

        
