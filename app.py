import streamlit as st

# Backend URL (Update this if you deploy the Flask app on Heroku)
BACKEND_URL = "https://floating-crag-45056-9ea530251d89.herokuapp.com/"

# Streamlit app
st.title("Webcam Stream Viewer")
st.text("The webcam feed is streamed from the Flask backend.")

# Display video feed
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{BACKEND_URL}" style="width: 640px; height: 480px; border: 1px solid #ddd;">
    </div>
    """,
    unsafe_allow_html=True,
)
