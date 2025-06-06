import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go

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
#st.dataframe(df)

st.markdown("---")

st.subheader('Filter Data')
columns = df.columns.tolist()
selected_column = st.selectbox("Select column to filter by", columns)
unique_values = df[selected_column].unique()
selected_value = st.selectbox("Select value", unique_values)

filtered_df = df[df[selected_column] == selected_value]
st.write(filtered_df)

st.markdown("---")

st.subheader('Total Encounters by Fiscal Year')
encounters_by_fiscal_year = df.groupby('Fiscal Year')['Encounter Count'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=encounters_by_fiscal_year, x='Fiscal Year', y='Encounter Count', palette='viridis', ax=ax)
ax.set_title('Total Encounters by Fiscal Year')
ax.set_xlabel('Fiscal Year')
ax.set_ylabel('Total Encounters')

for index, row in encounters_by_fiscal_year.iterrows():
    ax.text(index, row['Encounter Count'], f"{row['Encounter Count']:,}", color='black',
            ha='center', va='bottom', fontsize=10)
    
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)
            
st.markdown("---")

st.subheader("Total Encounters by Fiscal Year and Month")
encounters_by_year_month = df.groupby(['Fiscal Year', 'Month'])['Encounter Count'].sum().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(14, 7))
encounters_by_year_month.T.plot(kind='bar', ax=ax)
ax.set_title('Total Encounters by Fiscal Year and Month')
ax.set_xlabel('Month')
ax.set_ylabel('Encounter Count')
ax.legend(title='Fiscal Year')
ax.grid(axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

st.write(encounters_by_year_month)

st.markdown("---")

st.subheader("Total Encounter by Citizenship")
encounters_by_citizenship = df.groupby('Citizenship')['Encounter Count'].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(20, 8))
sns.barplot(x=encounters_by_citizenship.index, y=encounters_by_citizenship.values, palette='viridis', ax=ax)
ax.set_title('Total Encounters by Citizenship')
ax.set_xlabel('Citizenship')
ax.set_ylabel('Total Encounters')
ax.set_xticklabels(encounters_by_citizenship.index, rotation=45)

for index, value in enumerate(encounters_by_citizenship.values):
    ax.text(index, value + 50, f'{value:,}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
st.pyplot(fig)

st.write(encounters_by_citizenship)

st.markdown("---")

st.subheader("Total Encounters by Continent")
encounters_by_continent = df.groupby('Continent')['Encounter Count'].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=encounters_by_continent.index, y=encounters_by_continent.values, palette='viridis', ax=ax)
ax.set_title('Total Encounters by Continent')
ax.set_xlabel('Continent')
ax.set_ylabel('Total Encounters')
ax.set_xticklabels(encounters_by_continent.index, rotation=45)
for index, value in enumerate(encounters_by_continent.values):
    ax.text(index, value + 50, f'{value:,}', ha='center', va='bottom', fontsize=10)
plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

st.subheader("Total Encounters by Fiscal Year with Mean and Median")

# Calculate the mean and median of the Sum of Encounter Count by Fiscal Year. Add interactive table with plotly. Add meand and median results to the table.
encounters_by_fiscal_year_stats = encounters_by_fiscal_year.copy()
encounters_by_fiscal_year_stats['Mean'] = encounters_by_fiscal_year_stats['Encounter Count'].mean()
encounters_by_fiscal_year_stats['Median'] = encounters_by_fiscal_year_stats['Encounter Count'].median()
import plotly.express as px
fig = px.bar(encounters_by_fiscal_year_stats, x='Fiscal Year', y='Encounter Count',
             title='Total Encounters by Fiscal Year with Mean and Median',
             labels={'Encounter Count': 'Total Encounters'},
             text='Encounter Count')
fig.add_scatter(x=encounters_by_fiscal_year_stats['Fiscal Year'], y=encounters_by_fiscal_year_stats['Mean'],
                mode='lines+markers', name='Mean', line=dict(color='red', dash='dash'))
fig.add_scatter(x=encounters_by_fiscal_year_stats['Fiscal Year'], y=encounters_by_fiscal_year_stats['Median'],
                mode='lines+markers', name='Median', line=dict(color='blue', dash='dash'))
fig.update_layout(yaxis_title='Total Encounters', xaxis_title='Fiscal Year')
fig.show()
st.plotly_chart(fig, use_container_width=True)

st.write(encounters_by_fiscal_year_stats)

st.markdown("---")
















