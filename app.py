# import streamlit as st
# import helper
# import pickle

# model = pickle.load(open('model.pkl','rb'))

# st.header('Duplicate Question Pairs')

# q1 = st.text_input('Enter question 1')
# q2 = st.text_input('Enter question 2')

# if st.button('Find'):
#     query = helper.query_point_creator(q1,q2)
#     result = model.predict(query)[0]

#     if result:
#         st.header('Duplicate')
#     else:
#         st.header('Not Duplicate')

import streamlit as st
import helper
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Set page title and background
st.set_page_config(page_title="Duplicate Question Checker", page_icon="🔍", layout="wide")

# Add a custom CSS for better styling
st.markdown("""
    <style>
        .header {
            font-size: 40px;
            color: #ff6347;
            font-weight: bold;
        }
        .input {
            font-size: 20px;
            color: #4b0082;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .result {
            font-size: 30px;
            font-weight: bold;
            color: #008080;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            color: #888888;
            font-size: 18px;
        }
        .background {
            background-image: url('https://www.w3schools.com/w3images/forestbridge.jpg');
            background-size: cover;
            background-position: center;
            padding: 20px;
            color: white;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Add background color
st.markdown('<div class="background">', unsafe_allow_html=True)

# Header with customized style
st.markdown('<h1 class="header">Duplicate Question Pair Detector</h1>', unsafe_allow_html=True)

# Add input fields with styling
q1 = st.text_input('Enter Question 1', key='q1', help="Input the first question here.", placeholder="Type question 1...")
q2 = st.text_input('Enter Question 2', key='q2', help="Input the second question here.", placeholder="Type question 2...")

# Create a button for triggering the model
if st.button('Find', key="find", help="Click to check if the questions are duplicate", use_container_width=True):
    if q1 and q2:  # Check if both questions are entered
        query = helper.query_point_creator(q1, q2)
        result = model.predict(query)[0]

        if result:
            st.markdown('<p class="result">Duplicate</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="result">Not Duplicate</p>', unsafe_allow_html=True)
    else:
        st.warning("Please enter both questions.")

# Footer section
st.markdown('<div class="footer">Developed with ❤️ by Gopal Kushwaha</div>', unsafe_allow_html=True)

# Close the background div
st.markdown('</div>', unsafe_allow_html=True)


         

