import streamlit as st
from menu import menu
import streamlit_shadcn_ui as ui
from Utils import GettenantPayments,GetmyLease,DisplayDataframe
st.set_page_config(page_title="Payments",layout="wide")
menu()

tenantid = st.session_state["Login_info"]["user_id"].values[0]
leaseid = GetmyLease(tenantid=tenantid)["lease_id"].values[0]

payments = GettenantPayments(leaseid=leaseid)

ops = ["View My payments","Make a payment"]
options = ui.tabs(options=ops,default_value=ops[0])

if options == ops[0]:
    st.header("My Payments")
    st.dataframe(payments,hide_index=True)

if options == ops[1]:
    st.write("Yet to be implemented")
 