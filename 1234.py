# app.py

import streamlit as st

# Set the title for the application
st.title("👋 Simple Streamlit Greeting App")
st.markdown("---")

# --- User Input Widgets ---

# 1. Text Input Widget
name = st.text_input(
    "Enter your name:", 
    "Data Scientist" # Default value
)

# 2. Slider Widget
number = st.slider(
    "Select a favorite number:", 
    min_value=1, 
    max_value=100, 
    value=42 # Default value
)

# 3. Button Widget
# The button returns 'True' only when it is clicked
if st.button("Generate Output"):
    
    # --- Output Display ---
    
    st.header(f"Hello, {name}!")
    
    # Check if the number is even or odd
    if number % 2 == 0:
        message = f"Your chosen number, **{number}**, is an **even** number."
    else:
        message = f"Your chosen number, **{number}**, is an **odd** number."
        
    # Display the result using st.success for a nice visual
    st.success(message)
    
    # Display a congratulatory message with a fun element
    st.balloons() 

else:
    st.info("💡 Enter your details and click the button to see the result!")
