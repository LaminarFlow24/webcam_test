import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("OpenCV Filters on Video Stream")

filter = "none"

col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])

with col1:
    if st.button("None"):
        filter = "none"
with col2:
    if st.button("Blur"):
        filter = "blur"
with col3:
    if st.button("Grayscale"):
        filter = "grayscale"
with col4:
    if st.button("Sepia"):
        filter = "sepia"
with col5:
    if st.button("Canny"):
        filter = "canny"
with col6:
    if st.button("Invert"):
        filter = "invert"

webrtc_streamer(key="streamer", sendback_audio=False)
