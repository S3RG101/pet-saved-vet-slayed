import streamlit as st

st.title('Patient Summary')

col1, col2= st.columns(2)

with col1:
  st.subheader("Name")
  cont1 = st.container(border=True)
  cont1.write("Stephana")
  
  st.subheader("Breed")
  cont1 = st.container(border=True)
  cont1.write("French Bulldog")
  
  st.subheader("Active Concerns")
  cont1 = st.container(border=True)
  cont1.write("Wellness Exam")
  cont1 = st.container(border=True)
  cont1.write("Rabies Vaccine Due")
  cont1 = st.container(border=True)
  cont1.write("Heartworm Testing")

  

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

  st.subheader("Behavior Concerns")
  cont1 = st.container(border=True)
  cont1.write("Noise Sensitive **go slow**")
  
  st.subheader("Current Medications")
  cont1 = st.container(border=True)
  cont1.write("**Sentinel** 11-25lb/5-11kg Green 6pk")
