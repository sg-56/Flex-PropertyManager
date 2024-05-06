from menu import menu
menu()
import streamlit as st

import streamlit_shadcn_ui as ui

from datetime import date

from Utils import initialize_connection,AddLease,redirect,GetProperties


def GetTenants():
    conn = initialize_connection()
    sql = "SELECT * from Users WHERE user_type = 'tenant' ;"
    df = conn.query(sql)
    return df

tenants = GetTenants()
ownerid = st.session_state["Login_info"]["user_id"].values[0]
properties = GetProperties(ownerid=ownerid)
PropsList = properties["property_name"].values

tenantlist = (tenants["first_name"] +" "+ tenants["last_name"]+" | "+ "Tenant ID : "+tenants["user_id"].astype('str')).values

user_option = ui.tabs(options=["View Leases","Create New Lease"],default_value="Create New Lease")
if user_option == "View Leases":
    redirect("pages/leases.py")
else:
    cols = st.columns([1,2,1])
    with cols[1]:  
        st.title("Add a lease")
        with st.form("AddLease",clear_on_submit=True):
            property = st.selectbox(label="Property Name",options=PropsList)
            propertyid = properties[properties["property_name"] == property]["property_id"].values[0]
            tenant = st.selectbox(label="Select Tenant",options=tenantlist,placeholder="Select a tenant from the list",index=None)
            description = st.text_area(label="Enter Lease Description")
            formc = st.columns([1,1])
            with formc[0]:
                start_date = st.date_input(label="Start Date",key="start_date",format="YYYY/MM/DD")
            with formc[1]:
                end_date = st.date_input(label="End Date",key="end_date",min_value=date.today(),format="YYYY/MM/DD")
            monthly_rent = st.text_input(label="Enter Monthly Rent",placeholder="In Rupees")  
            submit = st.form_submit_button(label="Submit")

            if submit:
                if tenant is not None and tenant != '':
                    tenant_id = tenant.split(" ")[-1]
                AddLease(property_id=propertyid,tenant_id=tenant_id,start_date=start_date,end_date = end_date,monthly_rent=monthly_rent,lease_description=description)
                st.write("Lease has been added Successfully!!")
                redirect("pages/viewCurrentlease.py")