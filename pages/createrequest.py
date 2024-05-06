import streamlit as st
import streamlit_shadcn_ui as ui
from Utils import GetmyHome,GetMyRequests,SubmitUserQuery

from menu import menu
menu()


def Requestform():
    cols = st.columns([1,2,1])
    with cols[1]:
        with st.form(key="Requestform",clear_on_submit=True):
            Description = st.text_area(label="Describe Your Request")
            date = st.date_input(label="Enter the Date of the issue",value="today",format="DD/MM/YYYY")
            submit = st.form_submit_button(label="Submit",type="primary")
            status = "pending"
            if submit:
                SubmitUserQuery(propertyid=propertyid,tenantid=tenantid,description=Description,date=date,status=status)
                st.success("Your Request has been submitted")

tenantid = st.session_state["Login_info"]["user_id"].values[0]
propertyid = GetmyHome(tenantid=tenantid)["property_id"].values[0]

ops = ["View My Requests","Make a request"]

selected = ui.tabs(options=ops,default_value=ops[0])

if selected == ops[0]:
    st.title("Displaying my requests")
    st.divider()
    requests = GetMyRequests(tenantid=tenantid,propertyid=propertyid)
    if (requests.shape[0] == 0):
        cols = st.columns([1,2,1])
        with cols[1]:
            st.image(image="images/No_data_found.jpg",width=500)
            st.header("You have raised no requests....")
    else:
        st.table(requests[["request_id","description","submitted_date","status"]])

if selected == ops[1]:
    st.title("Create a Request")
    st.divider()
    Requestform()




