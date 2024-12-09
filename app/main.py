import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from app.utils import load_data, clean_data

# Title
st.title("Solar Energy Dashboard")
st.sidebar.header("Navigation")

# Navigation
options = st.sidebar.radio("Select a Page:", ["Overview", "Analysis", "Raw Data"])

# Load and clean data
datasets = load_data()
cleaned_data = {name: clean_data(df) for name, df in datasets.items()}

if options == "Overview":
    st.header("Project Overview")
    st.write("""
    This dashboard visualizes solar radiation and environmental data from Benin, Sierra Leone, and Togo.
    Use the navigation menu to explore different insights.
    """)

elif options == "Analysis":
    st.header("Data Analysis")
    selected_dataset = st.selectbox("Select a Dataset", list(cleaned_data.keys()))
    df = cleaned_data[selected_dataset]

    # Summary Statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Interactive Histogram
    selected_column = st.selectbox("Select a Column for Histogram", df.select_dtypes("number").columns)
    bins = st.slider("Number of Bins", 5, 50, 20)
    fig, ax = plt.subplots()
    df[selected_column].hist(bins=bins, ax=ax, color="skyblue", edgecolor="black")
    st.pyplot(fig)

    # Correlation Heatmap

    st.subheader("Correlation Heatmap")
# Select only numeric columns
    numeric_df = df.select_dtypes(include=["float", "int"])
    if numeric_df.empty:
        st.warning("No numeric columns available for correlation.")
    else:
    
        correlation = numeric_df.corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)


#
elif options == "Raw Data":
    st.header("Raw Data")
    selected_dataset = st.selectbox("Select a Dataset to View", list(cleaned_data.keys()))
    st.dataframe(cleaned_data[selected_dataset])
