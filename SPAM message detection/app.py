import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Set the page configuration
st.set_page_config(page_title="Message Predictor", page_icon="📧")

# Custom CSS styles
css = """
<style>
body {
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
    padding: 20px;
}
.title {
    text-align: center;
    color: white;
    margin-bottom: 20px;
    font-size: 36px;
}
.description {
    text-align: center;
    color: #666;
    margin-bottom: 30px;
    font-size: 18px;
}
.message-input {
    width: 80%;
    padding: 8px;
    font-size: 16px;
    margin-bottom: 20px;
}
.predict-button {
    width: 100%;
    padding: 10px;
    font-size: 18px;
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
}
.result {
    text-align: center;
    margin-top: 20px;
    padding: 10px;
    font-size: 24px;
    border-radius: 5px;
    color: white;
}
.error-message {
    text-align: center;
    color: #FF5733;
    margin-top: 10px;
    font-size: 20px;
}
.warning-message {
    text-align: center;
    color: #FFA500;
    margin-top: 10px;
    font-size: 20px;
}
</style>
"""

# Display custom CSS
st.markdown(css, unsafe_allow_html=True)

# Page Title and Description
st.markdown('<h1 class="title">📧 Message Predictor</h1>', unsafe_allow_html=True)
st.markdown("""
         <p class="description">This app predicts whether a given message is <strong>spam</strong> or <strong>legit</strong>. 
         Please enter your message below and click the <strong>Predict</strong> button.</p>
         """, unsafe_allow_html=True)

# Input field for the message
message = st.text_input('Enter a Message', value='', max_chars=None, key=None, type='default')

# Predict button
submit = st.button('Predict', key=None, help=None)

# Function to predict message category
def predict_message(message):
    prediction = model.predict([message])
    return prediction[0]

# When the Predict button is clicked
if submit:
    if message:  # Check if the input is not empty
        # Predict the category of the message
        result = predict_message(message)
        
        # Display the result
        if result == 'spam':
            st.markdown('<p class="warning-message">🚫 THIS MESSAGE IS SPAM</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="result">✅ THIS MESSAGE IS LEGIT</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="error-message">Please enter a message to predict.</p>', unsafe_allow_html=True)