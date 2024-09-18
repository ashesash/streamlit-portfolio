import streamlit as st
from sitewide.main_sidebar import sidebar
import uuid

st.set_page_config(layout="wide")

col1 = st.sidebar

col1, col2 = st.columns(2)

with col1:
    st.title("Ash")
    st.title("Software Engineer")
    content = """
    I'm a software engineer who was once a Mechanical engineer. I love all things web dev and data.
    """
    st.info(content)

with col2:
    st.title("Python developer")
    content = """
    Who are you?
    """
    st.info(content)
