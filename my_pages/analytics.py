import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from utils import apply_theme

BASE_DIR = Path(__file__).parent.parent


def analytics_page():

    apply_theme()

    st.markdown(
        """
        <div class='title'>
        📊 Housing Analytics Dashboard
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='subtitle'>
        Explore trends and insights from the housing dataset.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    try:
        df = pd.read_csv(BASE_DIR / "dataset" / "Housing.csv")

    except Exception as e:
        st.error(f"Dataset not found: {e}")
        return

    # ----------------------------
    # KPI Cards
    # ----------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🏠 Houses", len(df))
    c2.metric("📏 Avg Area", f"{int(df['area'].mean())} sq ft")
    c3.metric("🛏 Avg Bedrooms", round(df["bedrooms"].mean(), 1))
    c4.metric("💰 Avg Price", f"₹ {int(df['price'].mean()):,}")

    st.divider()

    # ----------------------------
    # Charts
    # ----------------------------

    left, right = st.columns(2)

    with left:

        fig = px.histogram(
            df,
            x="price",
            nbins=30,
            title="House Price Distribution",
            color_discrete_sequence=["#00C853"],
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        fig = px.scatter(
            df,
            x="area",
            y="price",
            color="bedrooms",
            size="bathrooms",
            title="Area vs Price",
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    left, right = st.columns(2)

    with left:

        fig = px.box(
            df,
            x="bedrooms",
            y="price",
            color="bedrooms",
            title="Bedrooms vs Price",
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        fig = px.bar(
            df.groupby("stories")["price"].mean().reset_index(),
            x="stories",
            y="price",
            title="Average Price by Stories",
            color="stories",
        )

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        df.head(15),
        use_container_width=True,
    )

    st.divider()

    st.subheader("📈 Dataset Statistics")

    st.dataframe(
        df.describe(),
        use_container_width=True,
    )

    st.divider()

    st.success("Analytics generated successfully.")