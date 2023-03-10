import streamlit as st
import pickle
pickle_model=open('model.pkl',"rb")
load_model=pickle.load(pickle_model)
st.title("Social Media Bullying Classification")
st.write("1.Not Cyber_bullying")
st.write("2.Cyber Bullying")
st.write("3.Gender")
st.write("4.Age")
st.write("5.Ethnicity")
st.write("6.Religion")
inputs=st.text_input("Give any tweet !!!")
if st.button("Predict"):
    result=load_model.predict([inputs])
    st.success(result)

