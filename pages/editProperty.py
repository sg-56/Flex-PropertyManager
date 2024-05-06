import streamlit as st

from menu import menu
menu()

from time import sleep

from Utils import UpdateProperty,redirect
from streamlit_js_eval import streamlit_js_eval

def getType(type):
    if type == "residential":
         return 0
    else:
         return 1

Currprop = st.session_state["CurrentProperty"]

cols = st.columns([1,2,1])
with cols[1]: 
    st.header("Edit Property")
    with st.form(key="EditProperty",clear_on_submit=True):
                property = {}
                name = st.text_input(label="Property Name",value=Currprop["property_name"].values[0])
                info = st.text_area(label="Property Desciption",value=Currprop["property_info"].values[0])
                adress = st.text_area(label="Adress",value=Currprop["address"].values[0])
                city = st.text_input(label="City",value=Currprop["city"].values[0])
                state = st.text_input(label="state",value=Currprop["state"].values[0])
                zip = st.text_input(label="Zipcode",max_chars=6,value=Currprop["zip_code"].values[0])
                type = st.selectbox(options=["Residential","Commercial"],label="Property Type",disabled=True,index=getType(Currprop["property_type"].values[0]))
                measure = st.text_input(label="Property Measure",placeholder="In Square Metres",value=Currprop["square_footage"].values[0])
                beds = st.text_input(label="Bedrooms",value=Currprop["bedrooms"].values[0])
                bathrooms = st.text_input(label="Bathrooms",value=Currprop["bathrooms"].values[0])
                submit = st.form_submit_button(label="Submit")
                if submit:
                    if beds == '' or bathrooms == '':
                        beds = 0
                        bathrooms = 0
                    
                    if name == '' or adress == '':
                        st.error("Please Enter the name and adress of the Property")
                        st.stop()

                    property["property_id"] = Currprop["property_id"].values[0]
                    property["property_name"] = name
                    property["property_info"] = info
                    property["adress"] = adress
                    property["city"] = city
                    property["state"] = state
                    property["zip_code"] = zip
                    property["property_type"] = type.lower()
                    property["square_footage"] = measure
                    property["bedrooms"] = int(beds)
                    property["bathrooms"] = int(bathrooms)
                    property["owner_id"] = Currprop["owner_id"].values[0]
                    UpdateProperty(property)
                    st.success("Property Details Updated Sucessfully")
                    sleep(1.5)
                    redirect(page = "pages/properties.py")
                    
