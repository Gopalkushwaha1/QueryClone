import streamlit as st
import helper
import pickle

# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Duplicate Question Checker", page_icon="🔍", layout="wide")

# Cache the model loading process to save memory
@st.cache_resource
def load_model():
    return pickle.load(open('model.pkl', 'rb'))

# Load the model
model = load_model()

# Add custom CSS for styling and responsiveness
st.markdown("""
    <style>
        /* Apply a gradient background to the entire page */
        body {
            background: linear-gradient(to right, #1a1a2e, #16213e, #0f3460);
            color: #ffffff;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
        }

        /* Header styling */
        .header {
            font-size: 3rem;
            color: #ffcc00; /* Gold */
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }

        /* Input fields styling */
        input {
            font-size: 1.2rem;
            color: #000000;
            background: #ffffff;
            padding: 10px;
            border: 2px solid #4CAF50;
            border-radius: 8px;
            margin-bottom: 20px;
            width: 100%;
            box-sizing: border-box; /* Ensure consistent box sizing */
        }

        /* Button styling */
        .stButton > button {
            font-size: 1.2rem;
            background: linear-gradient(to right, #00c6ff, #0072ff);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 10px 20px;
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
        }

        .stButton > button:hover {
            transform: scale(1.1);
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
        }

        /* Result styling */
        .result {
            font-size: 2rem;
            font-weight: bold;
            color: #32cd32; /* Lime green */
            text-align: center;
            margin-top: 20px;
        }

        .result.negative {
            color: #ff4500; /* Red-orange */
        }

        /* Footer styling with animated gradient */
        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .footer {
            background: linear-gradient(270deg, #1a1a2e, #0072ff, #00c6ff, #16213e);
            background-size: 400% 400%;
            animation: gradientAnimation 10s ease infinite;
            text-align: center;
            color: #cccccc;
            padding: 15px;
            margin-top: 50px;
            font-size: 1rem;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .header {
                font-size: 2.5rem; /* Adjust header for tablets */
            }
            input {
                font-size: 1rem;
                padding: 8px;
            }
            .stButton > button {
                font-size: 1rem;
                padding: 8px 15px;
            }
            .result {
                font-size: 1.5rem;
            }
            .footer {
                font-size: 0.9rem;
            }
        }

        @media (max-width: 480px) {
            .header {
                font-size: 2rem; /* Adjust header for mobile */
            }
            input {
                font-size: 0.9rem;
                padding: 6px;
            }
            .stButton > button {
                font-size: 0.9rem;
                padding: 6px 12px;
            }
            .result {
                font-size: 1.2rem;
            }
            .footer {
                font-size: 0.8rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Header with customized style
st.markdown('<h1 class="header">Duplicate Question Pair Detector</h1>', unsafe_allow_html=True)

# Input fields
q1 = st.text_input("Enter Question 1", placeholder="Type the first question here...")
q2 = st.text_input("Enter Question 2", placeholder="Type the second question here...")

# Prediction Button and Results
if st.button("Find"):
    if q1 and q2:
        query = helper.query_point_creator(q1, q2)

        try:
            result = model.predict(query)[0]
            if result:
                st.markdown('<div class="result">Duplicate</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="result negative">Not Duplicate</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter both questions.")

# Footer
st.markdown("""
    <div class="footer">
        Developed with 💚 by <b>Gopal Kushwaha</b>. <br>
        Powered by Streamlit 🚀
    </div>
""", unsafe_allow_html=True)
