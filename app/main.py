import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from app.utils import load_data, clean_data
from scipy.stats import zscore

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
    numeric_df = df.select_dtypes(include=["float", "int"])
    if numeric_df.empty:
        st.warning("No numeric columns available for correlation.")
    else:
        correlation = numeric_df.corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # Box Plot (for outlier detection)
    st.subheader(f"Boxplot for {selected_dataset}")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=df[["GHI", "DNI", "DHI"]], ax=ax)
    st.pyplot(fig)

    # Time Series Plot for GHI
  # Time Series Plot for GHI
    st.subheader(f"Time Series Plot of GHI for {selected_dataset}")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df.set_index("Timestamp", inplace=True)

# Create figure and axis explicitly
    fig, ax = plt.subplots(figsize=(12, 6))
    df[["GHI"]].plot(ax=ax)  # Plot the data on the ax

    plt.title("Time Series of GHI")
    st.pyplot(fig)  # Pass the figure to st.pyplot()


    # Scatter Plot (GHI vs. Tamb)
    st.subheader(f"Scatter Plot of GHI vs. Tamb for {selected_dataset}")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x=df["GHI"], y=df["Tamb"], ax=ax)
    st.pyplot(fig)

    # Z-Score Analysis (to detect anomalies)
    st.subheader(f"Z-Score Analysis for {selected_dataset}")
    df["z_ghi"] = zscore(df["GHI"].dropna())
    anomalies = df[df["z_ghi"] > 3]
    st.write(f"Anomalies in GHI for {selected_dataset}:", anomalies)

elif options == "Raw Data":
    st.header("Raw Data")
    selected_dataset = st.selectbox("Select a Dataset to View", list(cleaned_data.keys()))
    st.dataframe(cleaned_data[selected_dataset])
