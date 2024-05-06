import streamlit as st

from menu import menu
menu()
from sqlalchemy import text
from Utils import redirect

from Components import image_corousel
from Utils import initialize_connection

import streamlit_shadcn_ui as ui

st.title("Viewing Lease")
property_info = st.session_state["CurrentLease"]



def GetLease(propertyid):
    conn = initialize_connection()
    sql = f"SELECT * FROM Leases WHERE property_id = {propertyid} ;"
    df = conn.query(sql,ttl=0)
    return df

Leaseinfo = GetLease(propertyid=property_info.get("property_id"))

def GetUser(userid):
    conn = initialize_connection()
    sql = f"SELECT first_name,last_name,phonenumber,email,Adress FROM Users WHERE user_id = {userid};"
    df = conn.query(sql)
    return df


with st.container(border=True):
    cols = st.columns([1,1])
    with cols[0]:
        st.header("Property Name : "+property_info.get("property_name"))
        for key in list(property_info.keys())[2:-1]:
            st.write(f"{key.upper()} : {property_info[key]}")

    with cols[1]:
        image_corousel(height=390)

Leaseinfo = GetLease(propertyid=property_info.get("property_id"))


if Leaseinfo.shape[0] == 0:
    with st.container():
        cols = st.columns([1,2,1])
        with cols[1]:
            st.subheader("No Leases have been created for this property")      

    with cols[2]:
        createlease = st.button(label="Create a Lease")

    if createlease:
        redirect("pages/createlease.py")

else:
        st.header("Displaying Lease Agreement")
        with st.container(border=True):
            st.subheader("Tenant Details")
            tenant_info = GetUser(Leaseinfo["tenant_id"].values[0])
            st.dataframe(tenant_info,hide_index=True)

        with st.container(border=True):
            lescols = st.columns([1,0.3,2])
            for key in list(Leaseinfo.keys())[3:]:
                with lescols[0]:
                    st.markdown(key.replace("_"," ").upper())
                with lescols[1]:
                    st.write(":")
                with lescols[2]:
                        st.write(str(Leaseinfo[key].values[0]))

        buttoncols = st.columns([1,0.1,2])
        with buttoncols[0]:
            edit = st.button("Edit Lease")
        with buttoncols[2]:
            delete = st.button("Delete Lease")