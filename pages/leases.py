import streamlit as st
st.set_page_config(page_title="Leases",layout="wide")
import streamlit_shadcn_ui as ui
from Utils import card,redirect
from PIL import Image

from Utils import GetProperties,GetLeases

from streamlit_extras import dataframe_explorer

from menu import menu
menu()

def DisplayLeases(CurrentProperty):
    with st.container():
        cols = st.columns([2,3,1])
        with cols[0]:
            with st.container():
                image = Image.open('images/Home-icon.png')
                new_image = image.resize((250, 250))
                st.image(new_image)
                #st.image(image="images/Home-icon.png",use_column_width=True,width=100,)
             
        with cols[1]:
             card(propertyname=CurrentProperty["property_name"],property_info=CurrentProperty["property_info"],city=CurrentProperty["city"],state=CurrentProperty["state"],adress=CurrentProperty["address"])
        with cols[2]:
             con1 = st.container(height=110,border=False)
             viewbutton = st.button("View",type="primary",key=CurrentProperty["property_name"])
             if viewbutton:
                st.session_state["CurrentLease"] = CurrentProperty
                redirect(page="pages/viewCurrentlease.py")

ownerid = st.session_state["Login_info"]["user_id"][0]



properties = GetProperties(ownerid=ownerid)
props = properties["property_name"].values
leases = GetLeases(ownerid=ownerid)

user_option = ui.tabs(options=["View Leases","Create New Lease"],default_value="View Leases")
if user_option == "View Leases":
    cols = st.columns([1,2,1])
    with cols[1]:
        selected = st.multiselect("Select Your Property from the list: ",placeholder="",options=props)
    if selected:
            st.markdown("# View My Leases")
            filtered = properties[properties["property_name"] == selected[0]]
            props = properties.to_dict(orient='index')
            if len(selected) > 1:
                props = properties.to_dict(orient='index')
                for i in range(properties.shape[0]):
                    with st.container(border=True):
                        DisplayLeases(CurrentProperty=props[i])
            elif len(selected) == 1:
                for i in props:
                    if selected[0] in props[i].values():
                        DisplayLeases(props[i])
                      
if user_option =="Create New Lease":
   redirect(page="pages/createlease.py")
        
            