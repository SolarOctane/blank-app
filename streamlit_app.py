import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🎈 My Mid Term Project App")
st.write(
    "This is an immigration encounters app."
)

st.title("Upload and Display Dataset")

# File uploader
#uploaded_file = st.file_uploader("encounters", type="csv")

#if uploaded_file is not None:
    #df = pd.read_csv(uploaded_file)
    #st.write("### Preview of the dataset:")
    #st.dataframe(df)


st.title("Load Local Dataset")

# Load dataset (make sure the file is in the same directory or provide full path)
df = pd.read_csv("encounters.csv")

st.write("### Preview of the dataset:")
st.dataframe(df)

x = st.slider('x')
st.write(x, 'squared is', x * x)
