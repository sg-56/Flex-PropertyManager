import streamlit as st
import numpy as np
from PIL import Image
import pandas as pd
import re
from sqlalchemy import text
import base64
import hashlib

# Initialize connection.

def initialize_connection():
    conn = st.connection('mysql', type='sql')
    return conn


def check_password(hash,user):
    hashed = hash_password(user)
    print("Hashed : ",hashed)
    if(hashed == hash):
        return True
    else:
        return False


def GetUserDetails(username:str,email:str,password:str,user_type:str,conn = initialize_connection):
    query_data = f"SELECT * from Users WHERE username = '{username}' AND email = '{email}' AND user_type = '{user_type}';"
    print(query_data)
    df = conn.query(query_data,ttl = 600)
    return df

def Authenticate(df):
    UserDetails = df.to_dict()
    print(UserDetails)
    if(UserDetails["username"] == {} or UserDetails["email"] == {}):
        st.error("User Not Found/Please Sign Up")
    elif(df["password"][0] != st.session_state.password):
            st.error("You Have entered Wrong Password")
    else:
        Login(df["user_type"][0])
        st.switch_page(page="pages/user.py")



    

def set_role(user_type:str):
    # Callback function to save the role selection to Session State
    st.session_state.role = user_type.lower()


def Login(role:str):
    set_role(role)
    st.session_state["LoggedIn"] = True

def LogOut():
    st.session_state.role = None
    st.switch_page("app.py")



def GetImage(Login_info):
    img_file_buffer = Login_info["profile_picture"][0]
    if img_file_buffer is not None:
        image = Image.open(img_file_buffer)
        return image
    
def redirect(page:str):
    st.switch_page(page=page)


def check_password_strength(password):
    # Minimum length requirement
    if len(password) < 8:
        return st.error("Weak: Password should be at least 8 characters long.")

    # Check for uppercase, lowercase, digits, and special characters
    if not re.search(r"[A-Z]", password):
        return st.error("Weak: Password should contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        return "Weak: Password should contain at least one lowercase letter."
    if not re.search(r"\d", password):
        return st.error("Weak: Password should contain at least one digit.")
    if not re.search(r"[ !@#$%^&*()_+{}\[\]:;<>,.?/\\~`|\"\-']", password):
        return st.error("Weak: Password should contain at least one special character.")
    return True


def CheckUserNameExists(username:str):
    conn = initialize_connection()
    query_text = f"SELECT username FROM Users WHERE username = '{username}';"
    query = conn.query(query_text,ttl=0)
    try:
        if(query["username"][0]):
            st.error("User Name Already Exists ! Please reset your password")
        else:
            return True
    except KeyError:
        return True
        
    


def hash_password(password):
    # Encode the password as bytes
    password_bytes = password.encode('utf-8')
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    # Update the hash object with the password bytes
    sha256_hash.update(password_bytes)
    # Get the hexadecimal representation of the hash
    hashed_password = sha256_hash.hexdigest()
    return hashed_password



def InsertNewUser(username:str,first_name:str,last_name,email:str,password:str,phone:str,adress:str,usertype:str):
    #password = hash_password(password=password) will be implemented later
    query = f"""INSERT INTO Users(username,first_name,last_name,email,password,phonenumber,Adress,user_type)
                VALUES('{username}','{first_name}','{last_name}','{email}','{password}','{phone}','{adress}','{usertype.lower()}');
            """
    db = initialize_connection().session
    if (db.execute(text(query))):
        db.commit()
        db.close()
        st.write("User Singup Successfull")
        return True
    else:
        st.error("Unknown Error Occured")
        return False
    
def update_password(id:str,new_password:str):
        db = initialize_connection().session
        sql = f"UPDATE Users SET password = '{new_password}' WHERE user_id = {id};"
        print(sql)
        db.execute(text(sql))
        db.commit()
        st.error("Password Updated Sucessfuly")


def render_image(filepath: str):
   """
   filepath: path to the image. Must have a valid file extension.
   """
   mime_type = filepath.split('.')[-1:][0].lower()
   with open(filepath, "rb") as f:
        content_bytes = f.read()
        content_b64encoded = base64.b64encode(content_bytes).decode()
        image_string = f'data:image/{mime_type};base64,{content_b64encoded}'
        st.image(image_string)



def UpdateProfileImage(image,userid):
    parms = ({"profile_picture":image,"id":userid})
    cur = initialize_connection().session
    sql = f"UPDATE Users SET profile_picture = '{str(image)}' WHERE user_id = {userid}"
    print(text(sql))
    cur.execute(text(sql))
    print(f"Image Updated Sucessfully for User ID = {userid}")
    cur.commit()
    cur.close()


def GetProperties(ownerid):
    conn = initialize_connection()
    sql = f"SELECT * FROM Properties WHERE owner_id = {ownerid}"
    df = conn.query(sql,ttl=0)
    return df


def GetLeases(ownerid):
    conn = initialize_connection()

    sql = f"SELECT l.* FROM Leases l JOIN Properties p ON l.property_id = p.property_id WHERE p.owner_id = {ownerid} ;"
    df = conn.query(sql,ttl=0)
    return df


def UpdateUser(first_name:str,last_name,email:str,phone:str,adress:str,user_id:int):
    #password = hash_password(password=password) will be implemented later
    query = f"""UPDATE Users SET first_name = '{first_name}',last_name = '{last_name}',email = '{email}',phonenumber = '{phone}',Adress = '{adress}' WHERE user_id = {user_id} ;
            """
    print(query)
    db = initialize_connection().session
    if (db.execute(text(query))):
        #db.commit()
        db.close()
        st.write("User Singup Successfull")
        return True
    else:
        st.error("Unknown Error Occured")
        return False



def card(propertyname:str,property_info:str,city:str,state:str,adress:str):
    st.markdown("""
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <div class="card mb-3" style="max-width: 600px;border: 0px;">
        <div class="row g-0">
        <div class="col-md-8">
        <div class="card-body">
        <h2 class="card-title"><b>{}</b></h2>
        <p class="card-text">{}</p>
        <p class="card-text">{}</p>
        <p class="card-text"><small class="text-muted" style="margin: 0px">{}</small></p>
        <p class="card-text"><small class="text-muted">{}</small></p>
            </div>
         </div>
        </div>
        </div>
        """.format(propertyname,property_info,adress,city,state),unsafe_allow_html=True)
    




def AddLease(property_id,tenant_id,start_date,end_date,monthly_rent,lease_description):
    db = initialize_connection().session
    sql = f"""INSERT INTO Leases(property_id,tenant_id,start_date,end_date,monthly_rent,lease_description)
            VALUES ({property_id},{tenant_id},'{start_date}','{end_date}',{monthly_rent},'{lease_description}');
        """
    print(sql)
    db.execute(text(sql))
    db.commit()
    print("Lease Added Sucessfully!!")
    db.close()




def UpdateProperty(property):
    db = initialize_connection().session
    query = f"""UPDATE Properties SET property_name = '{property["property_name"]}',
            property_info = '{property["property_info"]}',
            address = '{property["adress"]}',
            city = '{property["city"]}',
            state = '{property["state"]}',
            zip_code = {property["zip_code"]},
            square_footage = {property["square_footage"]},
            bedrooms = {property["bedrooms"]},
            bathrooms = {property["bathrooms"]}
            WHERE owner_id = {property["owner_id"]} AND property_id = {property["property_id"]};
            """
    print(query)
    db.execute(text(query))
    db.commit()
    db.close()
    print("Property Details Updated Sucessfully")


def DeleteProperty(propertyid):
    db = initialize_connection().session
    query = f"DELETE FROM Properties WHERE property_id = {propertyid};"
    print(query)
    db.execute(text(query))
    db.commit()
    db.close()


def GetmyHome(tenantid):
    db = initialize_connection()
    query = f"SELECT p.* FROM Properties p JOIN Leases l WHERE p.property_id = l.property_id AND l.tenant_id = {tenantid};"
    df = db.query(query,ttl=0)
    return df[df.index==0]


def GetmyLease(tenantid):
    db = initialize_connection()
    query = f"SELECT l.* FROM Properties p JOIN Leases l WHERE p.property_id = l.property_id AND l.tenant_id = {tenantid};"
    df = db.query(query,ttl=0)
    return df[df.index==0]


def GetOwnerDetails(propertyid):
    db = initialize_connection()
    query = f"Select u.first_name,u.last_name,u.phonenumber,u.email from Users u JOIN Properties P on u.user_id = P.owner_id AND P.property_id = {propertyid};"
    df = db.query(query,ttl=0)
    return df

def GettenantPayments(leaseid):
    db = initialize_connection()
    sql = f"SELECT payment_date,payment_amount,payment_method FROM Payments WHERE lease_id = {leaseid};"
    df = db.query(sql=sql)
    return df


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



def GetMyRequests(tenantid,propertyid):
    db = initialize_connection()
    query_text = f"SELECT * FROM Maintenance_Requests WHERE tenant_id = {tenantid} AND property_id = {propertyid};"
    df = db.query(query_text,ttl = 0)
    return df


def SubmitUserQuery(propertyid,tenantid,description,date,status):
    db = initialize_connection().session
    query = f"INSERT INTO Maintenance_Requests(property_id,tenant_id,description,submitted_date,status) VALUES ({propertyid},{tenantid},'{description}','{date}','{status}');"
    db.execute(text(query))
    db.commit()
    db.close()


def GetMaintenanceRequests(ownerid):
    db = initialize_connection()
    props = GetProperties(ownerid=ownerid)["property_id"].values
    df = None
    for prop in props:
        query = f"SELECT * FROM Maintenance_Requests WHERE property_id = {prop};"
        data = db.query(query,ttl=0)
        if df is not None:
            df = pd.concat([df,data],ignore_index=True)
        else:
            df = data
    return df




def GetPropertyName(property_id):
    db = initialize_connection()
    query = f"SELECT property_name from Properties WHERE property_id = {property_id};"
    df = db.query(query,ttl=0)
    return df["property_name"].values[0]


def GetTenantName(tenant_id):
    db = initialize_connection()
    query = f"SELECT first_name,last_name from Users WHERE user_id = {tenant_id};"
    df = db.query(query,ttl=0)
    return (df["first_name"]+" "+df["last_name"]).values[0]