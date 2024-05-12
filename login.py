
import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
import analyzer  # Import the module containing the analyzer page

# Path to your Firebase project credentials
cred_path = 'logindemo1-e3c8e-55453e37a9ba.json'

def initialize_firebase():
    try:
        firebase_admin.get_app()
    except ValueError:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)

initialize_firebase()

def send_password_reset(email):
    try:
        auth.send_password_reset_email(email)
        st.success("Password reset link sent. Check your email.")
    except Exception as e:
        st.error("Failed to send password reset email!!")

def app():
    st.title('WhatsApp Chat Analyzer!!!')

    # Initialize the session state for authentication if it's not already set
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    # Check the authentication status
    if not st.session_state['authenticated']:
        # Display the login and signup options if not authenticated
        choice = st.selectbox('Login/Sign Up', ['Login', 'Sign Up','Forget Password'])

        if choice == 'Login':
            email = st.text_input('Email Address')
            password = st.text_input("Password", type='password')
            if st.button('Login'):
                try:
                    #user = auth.create_user_with_email_and_password(email,password)
                    user = auth.get_user_by_email(email)
                    st.session_state['authenticated'] = True
                    st.success("Login successful!")
                    # Immediately render the analyzer page upon successful login
                    st. rerun()
                    #st.experimental_rerun()
                except Exception as e:
                    st.warning("Login Failed. Check your credentials.")

        elif choice == 'Sign Up':
            email = st.text_input('Email Address', key='email_signup')
            password = st.text_input("Password", type='password', key='password_signup')
            if st.button('Sign Up'):
                try:
                    user = auth.create_user(email=email, password=password)
                    st.success("Account created successfully!! Please Login using your email and password!!")
                except Exception as e:
                    st.error("Email is already existing!!")

        elif choice == 'Forget Password':
            email = st.text_input("Enter your email to reset your password")
            if st.button('Send Reset Link'):
                send_password_reset(email)




    if st.session_state['authenticated']:
        # If the user is authenticated, run the analyzer page
        # st.title("Welcome to Whatsapp Chat Analyzer")
        analyzer.run_analyzer()

if __name__ == "__main__":
    app()









# import streamlit as st
# import firebase_admin
# from firebase_admin import credentials, auth
# # Import the module containing the analyzer page
# import analyzer
#
# # Path to your Firebase project credentials
# cred_path = 'logindemo1-e3c8e-55453e37a9ba.json'
#
# def initialize_firebase():
#     try:
#         firebase_admin.get_app()
#     except ValueError:
#         cred = credentials.Certificate(cred_path)
#         firebase_admin.initialize_app(cred)
#
# initialize_firebase()
#
# def app():
#     st.title('WhatsApp Chat Analyzer')
#
#     if 'authenticated' not in st.session_state:
#         st.session_state['authenticated'] = False
#
#     choice = st.selectbox('Login/Sign Up', ['Login', 'Sign Up'])
#
#     if choice == 'Login':
#         email = st.text_input('Email Address')
#         password = st.text_input("Password", type='password')
#         if st.button('Login'):
#             try:
#                 user = auth.get_user_by_email(email)
#                 st.session_state['authenticated'] = True
#                 st.success('Login Successful!!')
#
#
#             except:
#                 st.warning("Login Failed")
#
#     elif choice == 'Sign Up':
#         email = st.text_input('Email Address', key='email_signup')
#         password = st.text_input("Password", type='password', key='password_signup')
#         if st.button('Sign Up'):
#             try:
#                 user = auth.create_user(email=email, password=password)
#                 st.success("Account created successfully!! Please Login using your email and password!!")
#             except Exception as e:
#                 st.error(f"Failed to create user: {e}")
#
#     if st.session_state['authenticated']:
#         # If the user is authenticated, run the analyzer page
#         st.title("Welcome to Whatsapp Chat Analyzer")
#         analyzer.run_analyzer()
#
#
# if __name__ == "__main__":
#     app()
#
#
