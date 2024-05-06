import streamlit as st
from menu import menu_with_redirect
from Utils import GetmyHome
from Components import image_corousel,property_info
st.set_page_config(page_title="Tenant",layout="wide")
# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

cols = st.columns([1,1,1,1,1])
with cols[2]:
    st.title("My Home")

tenantid = st.session_state["Login_info"]["user_id"].values[0]
myhome = GetmyHome(tenantid=tenantid)
#st.dataframe(myhome,hide_index=True)
image_corousel(height=600)
property_info(property_name=myhome["property_name"].values[0],adress=myhome["address"].values[0],state=myhome["state"].values[0],city=myhome["city"].values[0])
