import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title("My Mid Term Project Dashboard")

# File uploader
#uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

#if uploaded_file is not None:
    #df = pd.read_csv(uploaded_file)
    #st.write("### Preview of the dataset:")
    #st.dataframe(df)

# Load dataset (make sure the file is in the same directory or provide full path)
df = pd.read_csv("encounters.csv")
st.subheader("Immigration Encounters Dataset")
st.dataframe(df)

st.subheader('Filter Data')
columns = df.columns.tolist()
selected_column = st.selectbox("Select column to filter by", columns)
unique_values = df[selected_column].unique()
selected_value = st.selectbox("Select value", unique_values)

filtered_df = df[df[selected_column] == selected_value]
st.write(filtered_df)

st.subheader("📊 Descriptive Statistics")
st.dataframe(df.describe())

#st.subheader("📍 Encounters Count per State")
#encounter_counts = df['State'].value_counts().reset_index()
#encounter_counts.columns = ['State', 'Encounters Count']
#st.dataframe(encounter_counts)

st.subheader("📅 Encounters Count by State, Fiscal Year, and Month")
encounter_counts = df.groupby(['State', 'Fiscal Year', 'Month (abbv)']).size().reset_index(name='Encounters Count')
encounter_counts = encounter_counts.sort_values(by=['State', 'Fiscal Year', 'Month'])
st.dataframe(encounter_counts)

# Plot bar chart
st.subheader("📊 Bar Chart of Encounters per State")
fig = px.bar(encounter_counts, x='State', y='Encounters Count', color='Encounters Count',
             color_continuous_scale='Blues', title='Number of Encounters by State')
st.plotly_chart(fig)

# Random Plot
st.subheader("Plot Data")
x_column = st.selectbox("Select x-axis column", columns)
y_column = st.selectbox("Select y-axis column", columns)

if st.button("Generate Plot"):
    st.line_chart(filtered_df.set_index(x_column)[y_column])

st.subheader("Bar Chart")
#st.dataframe(df)

# Let user select columns for bar chart
x_axis = st.selectbox("Select X-axis (categorical):", df.columns)
y_axis = st.selectbox("Select Y-axis (numerical):", df.columns)

# Plot the bar chart
st.bar_chart(df.set_index(x_axis)[y_axis])




