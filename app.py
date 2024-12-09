import streamlit as st
import helper
import pickle

# Cache the model loading process to save memory and avoid reloading it repeatedly
@st.cache_resource
def load_model():
    return pickle.load(open('model.pkl', 'rb'))

# Load the model
model = load_model()

# Set page title and layout
st.set_page_config(page_title="Duplicate Question Checker", page_icon="🔍", layout="wide")

# Add custom CSS for better styling
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

# Add a background section
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

        try:
            result = model.predict(query)[0]

            if result:
                st.markdown('<p class="result">Duplicate</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="result">Not Duplicate</p>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both questions.")

# Footer section
st.markdown('<div class="footer">Developed with ❤️ by Gopal Kushwaha</div>', unsafe_allow_html=True)

# Close the background div
st.markdown('</div>', unsafe_allow_html=True)
