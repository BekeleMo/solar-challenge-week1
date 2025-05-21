import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def load_data():
    """Load or simulate solar data from local CSVs or defaults."""
    try:
        benin = pd.read_csv("data/benin_clean.csv")
        sierra_leone = pd.read_csv("data/sierra_leone_clean.csv")
        togo = pd.read_csv("data/togo_clean.csv")
    except FileNotFoundError:
        np.random.seed(42)
        benin = pd.DataFrame({
            "GHI": np.random.normal(282.66, 269.58, 525600).clip(-12, 1424),
            "DNI": np.random.normal(167.11, 206.21, 525600).clip(0, 1004.5),
            "DHI": np.random.normal(220.60, 148.53, 525600).clip(0, 805.7),
            "Country": "Benin"
        })
        sierra_leone = pd.DataFrame({
            "GHI": np.random.normal(241.73, 241.43, 525600).clip(-19.5, 1499),
            "DNI": np.random.normal(155.52, 167.82, 525600).clip(-7.8, 946),
            "DHI": np.random.normal(131.63, 131.63, 525600).clip(-17.9, 892),
            "Country": "Sierra Leone"
        })
        togo = pd.DataFrame({
            "GHI": np.random.normal(272.54, 261.75, 525600).clip(-12.7, 1424),
            "DNI": np.random.normal(193.60, 194.15, 525600).clip(0, 1004.5),
            "DHI": np.random.normal(137.21, 126.62, 525600).clip(0, 805.7),
            "Country": "Togo"
        })
        return pd.concat([benin, sierra_leone, togo], ignore_index=True)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

def plot_ghi_boxplot(data):
    """Generate and return a GHI boxplot."""
    fig, ax = plt.subplots()
    sns.boxplot(x="Country", y="GHI", data=data, ax=ax)
    return fig

def get_top_regions(data):
    """Return a table of top regions by average GHI."""
    avg_ghi = data.groupby("Country")["GHI"].mean().reset_index()
    avg_ghi.columns = ["Country", "Average GHI (W/m²)"]
    return avg_ghi.sort_values(by="Average GHI (W/m²)", ascending=False)