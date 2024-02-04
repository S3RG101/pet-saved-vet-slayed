import streamlit as st
from streamlit_apexjs import st_apexcharts

st.set_page_config(page_title='Pet Saved, Vet Slayed®')

def mainpage():
  st.title('Pet Saved, Vet Slayed®')

  click = None

  if click is None:
    file = st.file_uploader("Choose Medical History in PDF", type='pdf', key='file_uploader')

  if not file is None:
    click = st.button('Proceed')
    if click:

      with st.sidebar:
        pat_sum = st.button('Patient Summary')
        if pat_sum:
          st.session_state.STATE = 1
          st.experimental_rerun()
        red_flag = st.button('Red Flags')
        if red_flag:
          st.session_state.STATE = 2
          st.experimental_rerun()
        hos_stats = st.button('Hospital Stats')
        if hos_stats:
          st.session_state.STATE = 3
          st.experimental_rerun()
