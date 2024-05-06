import streamlit as st
st.set_page_config(page_title = "Flex",layout="wide")


from menu import menu
from streamlit_option_menu import option_menu
import streamlit_shadcn_ui as ui
menu_selected = ''
from streamlit_extras.switch_page_button import switch_page
from Utils import initialize_connection
from Utils import GetUserDetails
from Utils import Authenticate,redirect

st.session_state["database"] = initialize_connection()




#pages_list = about,admin,login,menu
#login()

with st.sidebar:
    selected = option_menu("Flex", ["Home",'Login/Signup','About'], 
        icons=['house', 'gear','book','bell'], menu_icon="cast", default_index=0,key=menu_selected)
    
if selected == "Home":
    st.markdown("<h1 style='text-align: left; color: grey;'>Welcome to Flex</h1>", unsafe_allow_html=True)  
    st.markdown("## Your streamlined property management solution for landlords.")
    


    row1 = st.columns([1,1,1],)
    st.image("images/home.jpeg")
    with row1[0]:
        ui.metric_card(title="Centralized Dashboard", content="""Manage all your properties from one convenient platform. Get a comprehensive overview of your portfolio instantly.""", key="card1")
        
    with row1[1]:
        ui.metric_card(title="Security and Privacy", content="""Your data is safe with us. We employ advanced encryption technologies to protect your sensitive information.""", key="card2")
        
    with row1[2]:
       ui.metric_card(title="Automated Rent Collection", content="Say goodbye to chasing down payments. Our app automates rent collection, depositing payments directly to your bank account.", key="card3")

    row2 = st.columns(3)
    st.image("images/dashboard-homepage.jpeg")
    with row2[0]:
        ui.metric_card(title="Reminders and Notifications", content="""Never miss a deadline again. Receive reminders for lease renewals, maintenance tasks, and other important dates.""", key="card4")
    with row2[1]:
        ui.metric_card(title="Financial Tools", content=" Easily track rental income and generate reports for tax purposes. Simplify your financial management with our built-in tools.", key="card5")
    with row2[2]:
        ui.metric_card(title="Security and Privacy", content="Your data is safe with us. We employ advanced encryption technologies to protect your sensitive information.", key="card6")
    

    with st.container():
        image_col, text_col = st.columns((0.4,0.6))
    with image_col:
        st.image("images/home-square.jpeg")

    with text_col:
        st.subheader("There is no better place than Home!!")
        st.markdown(""" ##### Homeownership holds cultural significance in India, symbolizing stability, security, and social status. It is often seen as a milestone in one's life and a source of pride for families.
            """)

    with st.container():
        image_col, text_col = st.columns((0.4,0.6))
    with image_col:
        st.image("images/graph-square.jpeg",use_column_width=False,width=400)

    with text_col:
        st.subheader("Growth and Rise of Real Estate")
        st.write(""" The rising middle class in India has led to a surge in demand for affordable housing. 
                 This segment of the population is actively seeking homeownership opportunities, driving growth in the real estate market.
                 """)

if selected == "Login/Signup":
    cols = st.columns([1,1])
    with cols[0]:
        st.image(image="images/login.jpeg",use_column_width=True)

    with cols[1]:
        with st.container():
            with st.form("signup",clear_on_submit=True):
                st.markdown("# Login")
                st.markdown("#### Select user type")
                usertype = ui.tabs(options=['Tenant', 'Manager', 'Owner'], default_value='Owner',key = "_role")
                username = st.text_input(label="Username",key = "username")
                email = st.text_input(label="Email",key = "email")
                password = st.text_input(label="Password",type="password",key="password")

                buttons = st.columns([0.7,0.2])
                with buttons[0]:
                    submitted = st.form_submit_button("Submit") 
                    st.page_link(page="pages/resetpassword.py",label="Forgot Password?")
                with buttons[1]:
                        signup = st.form_submit_button(label="Signup")
                if signup:
                    st.switch_page("pages/signup.py")
                if submitted:
                    if (username != '' and  email != '' and password != ''):
                        st.session_state["Login_info"] = GetUserDetails(username=st.session_state.username,
                                                user_type=usertype.lower(),
                                                email=st.session_state.email,
                                                password=st.session_state.password,
                                                conn=st.session_state["database"]
                                                )
                        Authenticate(st.session_state["Login_info"])
                    else:
                        st.error("Please Enter all the details")
                


if selected == "About":
    st.write("To be implemented")

        








