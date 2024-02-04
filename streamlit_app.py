import streamlit as st
from streamlit_apexjs import st_apexcharts

st.set_page_config(page_title='Pet Saved, Vet Slayed®')

if "STATE" not in st.session_state:
    st.session_state.STATE = 0

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

def page1():
  st.title('Patient Summary')

  col1, col2= st.columns(2)

  with col1:
    st.subheader("Active Concerns")
    cont1 = st.container(border=True)
    cont1.write("Spay 01-Aug-2019")
    cont1 = st.container(border=True)
    cont1.write("Otitis externa 28-Oct-2018")
    cont1 = st.container(border=True)
    cont1.write("Wellness/Preventive care 31-Aug-2017")

  with col2:
    st.subheader("Medications")
    cont1 = st.container(border=True)
    cont1.write("Sentinel 11-25lb/5-11kg Green 6pk")
    cont1 = st.container(border=True)
    cont1.write("Rovera (Carprofen) 75mg Cw Tab")


def page2():
  st.title('Red flags')
  st.header("Vaccine Reactions")
  st.text("Covid 19 Vaccine Reaction: On page 17, the dog showed negative ")

  st.header("Drug Reactions")

  st.header("Antimicrobial Resistance")


def page3():
  st.title('Hospital Stats')
  st.header('1 Month Antimicrobial Resistance')

  options2 = {
      "chart": {
          "id": "lol2",
          "toolbar": {
              "show": False
          }
      },

      "xaxis": {
          "categories":
              ['MRSA', 'Campylobacter spp.', 'Salmonella spp.', 'Staphylococcus spp.']
      }
      ,
      "legend": {
          "show": True,
          "position": "bottom",
      }
  }

  series2 = [{
  "name": 'example',
  "data": [15, 17, 23, 44]
  }]

  st_apexcharts(options2, series2, 'bar', '200%')

if st.session_state.STATE == 0:
    mainpage()
elif st.session_state.STATE == 1:
    page1()
elif st.session_state.STATE == 2:
    page2()
elif st.session_state.STATE == 3:
    page3()
