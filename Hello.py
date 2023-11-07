
import streamlit as st
import pandas as pd

# Display dependencies with exact versions required
st.write("Dependencies:")
st.write("- pandas==1.2.4")
st.write("- streamlit==0.82.0")

# Title and explanation
st.title("Pandas Demo")
st.write("This app demonstrates some popular pandas operations.")

# Load a sample dataset
@st.cache
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    return data

data = load_data()

st.header("Dataset Overview")
st.write("The loaded dataset contains information about passengers of the Titanic.")

# Display a subset of the dataset
subset = st.checkbox("Display dataset subset")
if subset:
    subset_size = st.slider("Number of rows", 1, len(data))
    st.write(data.head(subset_size))

st.header("Operations")

# Describe the dataset
if st.button("Describe Dataset"):
    st.write(data.describe())

# Group by a column and aggregate
if st.button("Group By"):
    group_by_col = st.selectbox("Column to group by", data.columns)
    aggregate_col = st.selectbox("Column to aggregate", data.columns)
    aggregation = st.selectbox("Aggregation function", ['sum', 'mean', 'count', 'min', 'max'])
    group_by_result = data[[group_by_col, aggregate_col]].groupby(group_by_col).agg(aggregation)
    st.write(group_by_result)

# Perform data filtering
st.header("Filtering")
filter_col = st.selectbox("Column to filter", data.columns)
filter_value = st.text_input("Filter value")
filtered_data = data[data[filter_col] == filter_value]
st.write(filtered_data)

# Draw a bar chart
st.header("Visualization")
if st.button("Bar Chart"):
    chart_col = st.selectbox("Column to visualize", data.columns)
    chart_data = data[chart_col].value_counts()
    st.bar_chart(chart_data)

# Display the dataset as a table
st.header("Full Dataset")
st.write(data)
