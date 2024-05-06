import streamlit as st
import mysql.connector
from mysql.connector import Error
from PIL import Image
import base64
from io import BytesIO
from menu import menu
menu()

# Function to connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='property_management',
            user='root',
            password='8310728618'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error connecting to MySQL database: {e}")
        return None




# Function to insert or update profile picture for a user
def update_profile_picture(connection, userid, profile_picture):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE user_id = %s", (userid,))
        existing_user = cursor.fetchone()
        profile_picture = str(profile_picture)
        #st.write(existing_user)
        if existing_user:
            # Update profile picture if user already exists
            cursor.execute("UPDATE Users SET profile_picture = %s WHERE user_id = %s", (profile_picture, userid))
            st.success("Profile picture updated successfully!")
        else:
            # Insert new user with profile picture
            cursor.execute("INSERT INTO Users (username, profile_picture) VALUES (%s, %s)", (userid, profile_picture))
            st.success("Profile picture uploaded successfully!")

        #connection.commit()
    except Error as e:
        st.error(f"Error updating profile picture: {e}")

# Main function
def main():
    st.title("Upload Your Profile Photo")

    # Connect to MySQL database
    connection = connect_to_database()
    if connection is not None:
        userid = int(st.session_state.Login_info["user_id"][0])

        # File uploader
        uploaded_file = st.file_uploader("Choose a profile picture...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Display the uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Profile Picture", use_column_width=True)
            # Button to update profile picture
            if st.button("Update Profile Picture"):
                update_profile_picture(connection,userid,uploaded_file.getvalue())

# Run the main function
if __name__ == "__main__":
    main()