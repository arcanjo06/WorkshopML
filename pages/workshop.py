import streamlit as st
st.write("manuzinha gameplays 2004")

input=st.text_input("Nome:", key="mingi")       

st.write(input)
st.button("Click me")
st.feedback("thumbs")
st.page_link("app.py", label="Home")
st.checkbox("I agree")
st.toggle("Enable")
st.radio("Pick one", ["cats", "dogs"])
st.selectbox("Pick one", ["gays", "lesbianas", "bi"])
st.multiselect("Pick one", ["gays", "lesbianas", "bi"])
st.camera_input("faz a pose,olha o flash, que eu to gravando")
