import streamlit as st
from streamlit_apexjs import st_apexcharts

st.set_page_config(page_title='Vet Aid Pet Saved®')

st.sidebar.image("petsave.png", use_column_width=True)

st.title('Vet Aid Pet Saved®')

click = None

if click is None:
  file = st.file_uploader("Choose Medical History in PDF", type='pdf', key='file_uploader')

if not file is None:
  click = st.button('Proceed')
  if click:
