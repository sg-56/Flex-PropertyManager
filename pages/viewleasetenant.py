import streamlit as st
from menu import menu
st.set_page_config(page_title="View My Lease",layout="wide")

menu()

from Utils import GetmyLease,GetOwnerDetails

def DisplayDataframe(df):
    cols = st.columns([1,0.3,2])
    with cols[0]:
        for i in df.columns:
            st.write(i.replace("_"," ").upper())
    with cols[1]:
        for i in df.columns:
            st.write(":")
    with cols[2]:
        for row in df.columns:
            st.write(str(df[row].values[0]))


tenantid = st.session_state["Login_info"]["user_id"].values[0]

lease = GetmyLease(tenantid=tenantid)
owner_info = GetOwnerDetails(lease["property_id"].values[0])
cols = st.columns([2,2])
with cols[0]:
    with st.container(border=True):
        st.header("Owner Info")
        #st.markdown("---")
        DisplayDataframe(owner_info)
with cols[1]:
    with st.container(border=True):
        st.header("Lease Info")
        DisplayDataframe(lease[lease.columns[3:]])