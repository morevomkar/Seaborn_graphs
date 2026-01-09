import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_option_menu import option_menu

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Taxi Data Visualization Dashboard",
    page_icon="🚕",
    layout="wide"
)

# ---------------- Load Data ----------------
@st.cache_data
def load_data():
    return sns.load_dataset('taxis')

data = load_data()

# ---------------- Sidebar ----------------
with st.sidebar:
    st.title("🚕 Taxi Analytics")
    menu = option_menu(
        "Navigation",
        ["Overview", "Distribution", "Relationships", "Categorical Analysis", "Interactive Charts"],
        icons=["bar-chart", "pie-chart", "graph-up", "grid", "cursor"],
        default_index=0
    )

# ---------------- Main Title ----------------
st.markdown("## 📊 Taxi Dataset – Data Visualization with Matplotlib, Seaborn & Plotly")
st.markdown("Explore trends, patterns, and insights using beautiful and interactive charts.")

# ---------------- Overview ----------------
if menu == "Overview":
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Dataset Preview")
        st.dataframe(data.head())
    with col2:
        st.subheader("Dataset Info")
        st.write(data.describe())

# ---------------- Distribution ----------------
elif menu == "Distribution":
    st.subheader("📈 Distribution Analysis")

    fig, ax = plt.subplots()
    sns.histplot(data['total'], kde=True, ax=ax)
    ax.set_title("Distribution of Total Fare")
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.boxplot(y=data['tip'], ax=ax)
    ax.set_title("Tip Distribution (Box Plot)")
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.violinplot(y=data['tip'], ax=ax)
    ax.set_title("Tip Distribution (Violin Plot)")
    st.pyplot(fig)

# ---------------- Relationships ----------------
elif menu == "Relationships":
    st.subheader("🔗 Relationship Analysis")

    fig, ax = plt.subplots()
    sns.scatterplot(x='total', y='tip', data=data, ax=ax)
    ax.set_title("Total Fare vs Tip")
    st.pyplot(fig)

    fig = sns.pairplot(data[['total', 'tip', 'distance']])
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.lmplot(x='total', y='tip', data=data, hue='color')
    st.pyplot(plt.gcf())

# ---------------- Categorical Analysis ----------------
elif menu == "Categorical Analysis":
    st.subheader("📊 Categorical Insights")

    fig, ax = plt.subplots()
    sns.countplot(x='passengers', data=data, ax=ax)
    ax.set_title("Passenger Count Distribution")
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.barplot(x='color', y='tip', data=data, ax=ax)
    ax.set_title("Average Tip by Taxi Color")
    st.pyplot(fig)

# ---------------- Interactive Charts ----------------
elif menu == "Interactive Charts":
    st.subheader("✨ Interactive Plotly Visualizations")

    fig = px.scatter(
        data,
        x='total',
        y='tip',
        color='color',
        size='distance',
        title='Total Fare vs Tip (Interactive)'
    )
    st.plotly_chart(fig, use_container_width=True)

    fig = px.histogram(
        data,
        x='total',
        nbins=40,
        title='Total Fare Distribution'
    )
    st.plotly_chart(fig, use_container_width=True)

    fig = px.box(
        data,
        x='color',
        y='tip',
        title='Tip Distribution by Taxi Color'
    )
    st.plotly_chart(fig, use_container_width=True)

# ---------------- Footer ----------------
st.markdown("---")
st.markdown("💡 **Built with Streamlit | Matplotlib | Seaborn | Plotly**")
