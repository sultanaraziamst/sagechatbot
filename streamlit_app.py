import streamlit as st
import replicate 
import os

#apptitle

st.set_page_config(page_title="Sage chat bot")


#Replicate credential
with st.sidebar:
    st.title('Sage chat bot')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        