import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image(r"C:\Users\bunny\Downloads\images\passportphoto.png")

with col2:
    st.title("Raja Alwala")
    content = """This is Rajashekar Reddy Alwala        
    """
    st.info(content)

content2 = """Below you can find Apps that I have buit"""
st.write(content2)

col3,empty_col, col4 = st. columns(3)

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code],({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
