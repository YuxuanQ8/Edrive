import streamlit as st
import mysql.connector

# run stramlit
# python -m streamlit run your_script.py
# python -m streamlit run 'c:\Users\YXQia\OneDrive\Documents\IIT assignments\Fourth Year (First)\IPRO 497\demo.py'

# connect database (db)
mydb = mysql.connector.connect(
    host = 'edrive.cpm4gce8a2jo.us-east-2.rds.amazonaws.com',
    user = 'admin',
    password = 'iitDelta'
)

cur = mydb.cursor()

cur.execute('select user_emails from edrive.user_info ui;')

# get emails exist in db 
existEmails = [elem for tup in cur.fetchall() for elem in tup]



# avawilson@gmail.com
# email
email = st.text_input("Email")
if email in existEmails:
    st.write("This email has already registered")

# user name
userName = st.text_input('Username')

# password
psw = st.text_input('Password')

# retype password
repsw = st.text_input('Confirm password')

if repsw == '' and psw != '':
    pass
elif repsw != psw:
    st.write("Confirm password doesn't match")


press = st.button("Sign Up")



if press is True and email == '':
    st.write("Email can't be empty")
elif press is True and userName == '':
    st.write("Username can't be empty")
elif press is True and psw == '':
    st.write("Password can't be empty")
elif press is True and repsw == '':
    st.write("Confirm password can't be empty")
elif press is True and psw != repsw:
    st.write("Confirm password doesn't match")
elif press is True and email != '' and userName != '' and psw != '' and repsw != '':
    cur.execute("insert into edrive.user_info (user_emails, user_names, pswd, driving_hour) \
                 values (%s, %s, %s, '0');", (email, userName, repsw))
    mydb.commit()
    st.write("Successfully register")


# close database
cur.close()
mydb.close()