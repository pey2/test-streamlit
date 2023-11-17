import streamlit as st

st.subheader("This is a subtitle")
st.text("This is some text")

text = "Hello world!"
st.text(text)

organization_options = {"ASCII", "TPG", "Infobits", "CCIS-SC"}

if st.button("Click"):
    st.write("Button Clicked!")

st.radio('Gender', ["Male", "Female"])
st.number_input('Enter your GPA here')
st.multiselect('Organizations', organization_options)