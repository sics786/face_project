from PIL import Image
import streamlit as st
st.title('Face Recognition')
c = st.container()
Username = c.text_input("User name")
Userid = c.text_input("User ID")
Password = c.text_input("Password")
Emailid = c.text_input("Email Id")
Designation = c.selectbox("Designation", ["content Writer", "Team Lead", "Developer"])
Teamname = c.selectbox("Team Name", ["Developing", "Testing", "Training", "Marketing", "HR"])
Reporting = c.selectbox("Reporting Person", ["Monisha H Chandran", "Athulya", "Vishnu Prasad"])
Userimage = c.camera_input("Take a image for user")
DateofHire = c.date_input("Date of Hire")
Employeestatus = c.selectbox("Employee Status", ["Active", "Inactive"])
Employeetype = c.selectbox("Employee Type", ["Work From Home", "Work From Office"])
Employeecategory = c.radio("Employee Category", ["Permanent", "Probation", "Trainee", "Contract"])
Dateofjoining = c.date_input("Date of Joining")
submit = c.button("Submit")
img = st.sidebar.image("FACE.jpg", width = 500)


