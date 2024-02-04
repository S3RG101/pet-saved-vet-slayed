import streamlit as st

st.title('Patient Summary')

col1, col2= st.columns(2)

with col1:
  st.subheader("Name")
  cont1 = st.container(border=True)
  cont1.write("Esteban")
  
  st.subheader("Breed")
  cont1 = st.container(border=True)
  cont1.write("Shiba Inu")
  
  st.subheader("Active Concerns")
  cont1 = st.container(border=True)
  cont1.write("Spay 01-Aug-2019")
  cont1 = st.container(border=True)
  cont1.write("Otitis externa 28-Oct-2018")
  cont1 = st.container(border=True)
  cont1.write("Wellness/Preventive care 31-Aug-2017")

  

with col2:
  st.subheader("Age")
  cont1 = st.container(border=True)
  cont1.write("2 years, 11 months")

  st.subheader("Sex")
  cont1 = st.container(border=True)
  cont1.write("Female/Spayed")

  st.subheader("Weight")
  cont1 = st.container(border=True)
  cont1.write("19.1 lb")
  
  st.subheader("Medications")
  cont1 = st.container(border=True)
  cont1.write("Sentinel 11-25lb/5-11kg Green 6pk")
  cont1 = st.container(border=True)
  cont1.write("Rovera (Carprofen) 75mg Cw Tab")
