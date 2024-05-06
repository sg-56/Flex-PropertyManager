import streamlit as st
from menu import menu_with_redirect
st.set_page_config("Maintenance",layout="wide")
from Utils import GetMaintenanceRequests,GetPropertyName,GetTenantName

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verify the user's role
if st.session_state.role not in ["owner"]:
    st.warning("You do not have permission to view this page.")
    st.stop()



def RenderRequests(df):
    cols = st.columns([1,1,1,2,1,1])
    for i in range(len(df.columns)):
        with cols[i]:
            with st.container(border=True):
                st.write(df.columns[i].replace("_"," ").upper())
    st.divider()
    for idx,row in df.iterrows():
        with cols[0]:
            st.write(row["request_id"])
        with cols[1]:
            st.write(GetPropertyName(row["property_id"]))
        with cols[2]:
            st.write(GetTenantName(row["tenant_id"]))
        with cols[3]:
            st.write(row["description"])
        with cols[4]:
            st.write(str(row["submitted_date"]))
        with cols[5]:
            button = st.button(label=row["status"],key=row["request_id"])



owner_id = st.session_state["Properties"]["owner_id"].values[0]

requests = GetMaintenanceRequests(ownerid=owner_id)
st.write(requests)

RenderRequests(requests)





    



