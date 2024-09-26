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
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input ('Enter the Replicate API token:' , type='password')
    if not (replicate_api.startswith('r8_') and len (replicate_api)==40):
        st.warning('Please enter your credentials!', icon='⚠️')
    else:
        st.success('Proceed tp entering your prompt message!', icon= '👉')
os.environ['REPLICATE_API_TOKEN'] = replicate_api


st.subheader('Model and parameters')
selected_model = st.sidebar.selectbox ('Choose a Sage Model', ['Sage-1B', 'Sage-2B'], key= 'selected_model')

if selected_model == 'Sage-2B':
    ss 

    
        