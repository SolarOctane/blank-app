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
df = pd.read_csv("encounters_aor_df.csv")
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

#Streamlit Title
st.subheader("Total Encounters by Fiscal Year")
#st.dataframe(encounter_counts)
encounters_by_year = df.groupby('Fiscal Year')['Encounter Count'].sum().sort_index()
# Create bar chart
fig, ax = plt.subplots(figsize=(10, 6))
x = encounters_by_year.index.astype(str)  # Ensure labels are strings
y = encounters_by_year.values
bars = ax.bar(x, y)
# Add labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:,.0f}', ha='center', va='bottom', fontsize=10)
# Chart styling
ax.set_title('Total Encounter Count by Fiscal Year')
ax.set_xlabel('Fiscal Year')
ax.set_ylabel('Encounter Count')
ax.tick_params(axis='x', rotation=45)
ax.grid(axis='y')
plt.tight_layout()
# Show the plot in Streamlit
st.pyplot(fig)

st.subheader("Total Encounters by Continent")
encounters_by_continent = df.groupby('Continent')['Encounter Count'].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10, 6))
x = encounters_by_continent.index.astype(str)  # Ensure labels are strings
y = encounters_by_continent.values
bars = ax.bar(x, y)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:,.0f}', ha='center', va='bottom', fontsize=10)
    
plt.title('Total Encounter Count by Continent')
plt.xlabel('Continents')
plt.ylabel('Encounter Count')
plt.tick_params(axis='y', rotation=45)
plt.tight_layout()
plt.grid(axis='y')
st.pyplot(fig)








