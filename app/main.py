import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append("C:/Users/bekel/Desktop/Channel/10 Academy/solar-challenge-week1/app")  # Add app directory to path
from utils import load_data, plot_ghi_boxplot, get_top_regions

# Debug: Check data loading
data = load_data()
st.write("Data loaded:", data.head())  # Add this line to inspect the first few rows

# Title and description
st.title("Solar Irradiance Dashboard")
st.write("Interactive visualization of solar data for Benin, Sierra Leone, and Togo.")

# Sidebar for country selection
st.sidebar.header("Filters")
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)

# Load data (again, in case of filtering)
data = load_data()
filtered_data = data[data["Country"].isin(selected_countries)]

# Display GHI Boxplot
st.header("GHI Boxplot")
fig = plot_ghi_boxplot(filtered_data)
st.pyplot(fig)

# Display Top Regions Table
st.header("Top Regions by Average GHI")
top_regions = get_top_regions(filtered_data)
st.table(top_regions)

# Add interactivity note
st.write("Use the sidebar to filter countries and explore the data interactively.")