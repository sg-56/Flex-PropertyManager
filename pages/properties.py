import streamlit as st
st.set_page_config(page_title="Properties",layout="wide")
import streamlit_shadcn_ui as ui
from Utils import initialize_connection,redirect,DeleteProperty
from sqlalchemy import text
from streamlit_card import card
from Components import image_corousel

from time import sleep

if st.session_state["LoggedIn"]==False:
    st.stop()
    


def GetProperties(ownerid):
    conn = initialize_connection()
    sql = f"SELECT * FROM Properties WHERE owner_id = {ownerid}"
    df = conn.query(sql,ttl=0)
    return df

    
    



def AddProperty(property,ownerid):
    cur = initialize_connection().session
    values = list(property.values())
    values.append(ownerid)
    sql = f"INSERT INTO Properties(property_name,property_info,address,city,state,zip_code,property_type,square_footage,bedrooms,bathrooms,owner_id) VALUES {tuple(values)}; "
    cur.execute(text(sql))
    cur.commit()
    st.success("Added Property")
    

from menu import menu
menu() ##renders side bar
ownerid = st.session_state["Login_info"]["user_id"][0]


st.session_state["CurrentProp"] = GetProperties(ownerid=ownerid)


def renderprop():
        st.session_state["Properties"] = GetProperties(ownerid=ownerid)     
        properties = st.session_state["Properties"]
        if properties is None:
            st.write("U have not added Properties")
        else:
            colum = st.columns([1,4,1])
            with colum[1]:
                st.header("View Properties")
                #properties = GetProperties(ownerid=ownerid)
                props = properties["property_name"].values
                selected = st.selectbox("Select Your Property from the list: ",placeholder="",options=props,index=None)
                if selected:
                    filtered = properties.loc[properties["property_name"] == selected]
                    with st.container(border=True):
                        cols = st.columns([1,1])
                        with cols[0]:
                            st.header("Property Name : "+filtered.get("property_name").values[0])
                            for key in list(filtered.keys())[2:-1]:
                                 st.write(f"{key[0].upper()+key[1:]} : {filtered[key].values[0]}")

                        with cols[1]:
                            image_corousel(height=200)
                            with st.container(border=False):
                                edit = st.button(label="Edit Property")
                                delete = st.button(label="Delete Property")
                            
                                if edit:
                                    st.session_state["CurrentProperty"] = filtered
                                    st.session_state["Properties"] = None
                                    redirect(page="pages/editProperty.py")

                                if delete:
                                    DeleteProperty(propertyid = filtered.get("property_id").values[0])
                                    st.write("Property Deleted!")
                                    sleep(0.5)
                                    redirect(page="pages/properties.py")




with st.container():
    owner_tabs = ["View My properties","Add Property"]
    option = ui.tabs(options=owner_tabs,default_value=owner_tabs[0])
    if option == owner_tabs[0]:
         renderprop()


                                    


    if option == owner_tabs[1]:
        cols = st.columns([1,1])
        with cols[0]:
            with st.form(key="add_property",border=True,clear_on_submit=True):
                property = {}
                name = st.text_input(label="Property Name")
                info = st.text_area(label="Property Description")
                adress = st.text_area(label="Adress")
                city = st.text_input(label="City")
                state = st.text_input(label="state")
                zip = st.text_input(label="Zipcode",max_chars=6)
                type = st.selectbox(options=["Residential","Commercial"],label="Property Type")
                measure = st.text_input(label="Property Measure",placeholder="In Square Metres")
                beds = st.text_input(label="Bedrooms")
                bathrooms = st.text_input(label="Bathrooms")
                submit = st.form_submit_button(label="Submit")
        with cols[1]:
                st.image(image="images/property-bg.jpeg",clamp=True)
                if submit:
                    if beds == '' or bathrooms == '':
                        beds = 0
                        bathrooms = 0
                    
                    if name == '' or adress == '':
                        st.error("Please Enter the name and adress of the Property")
                        st.stop()

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
                    AddProperty(property=property,ownerid=ownerid)
                    sleep(0.5)
                    redirect("pages/properties.py")
