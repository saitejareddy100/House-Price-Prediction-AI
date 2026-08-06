import streamlit as st
from utils import apply_theme

def about_page():

    apply_theme()

    st.markdown("""
    <div class='title'>
    ℹ️ About This Project
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='subtitle'>
    House Price Prediction using Machine Learning
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # -------------------------------------------------
    # Project Overview
    # -------------------------------------------------

    st.markdown("""
    <div class='card'>
    <h2>🏠 Project Overview</h2>

    This application predicts the estimated selling price of a house
    using a Machine Learning model trained on housing data.

    The application demonstrates the complete Machine Learning workflow:

    ✔ Data Collection

    ✔ Data Preprocessing

    ✔ Feature Engineering

    ✔ Model Training

    ✔ Model Evaluation

    ✔ Streamlit Deployment

    ✔ Interactive Dashboard

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # -------------------------------------------------
    # Technologies
    # -------------------------------------------------

    st.subheader("💻 Technologies Used")

    c1, c2, c3, c4 = st.columns(4)

    c1.success("Python")
    c2.success("Pandas")
    c3.success("Scikit-Learn")
    c4.success("Streamlit")

    c5, c6, c7, c8 = st.columns(4)

    c5.success("Plotly")
    c6.success("NumPy")
    c7.success("Joblib")
    c8.success("VS Code")

    st.divider()

    # -------------------------------------------------
    # ML Algorithm
    # -------------------------------------------------

    st.markdown("""
    <div class='card'>

    <h2>🤖 Machine Learning Model</h2>

    <b>Algorithm:</b> Linear Regression

    <br><br>

    The model predicts house prices based on:

    • Area

    • Bedrooms

    • Bathrooms

    • Stories

    • Parking

    • Main Road

    • Guest Room

    • Basement

    • Air Conditioning

    • Preferred Area

    • Furnishing Status

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # -------------------------------------------------
    # Features
    # -------------------------------------------------

    st.subheader("⭐ Key Features")

    feature1, feature2 = st.columns(2)

    with feature1:

        st.info("🏠 Real-time House Price Prediction")

        st.info("📊 Interactive Analytics Dashboard")

        st.info("📈 Plotly Charts")

        st.info("💾 Machine Learning Model")

    with feature2:

        st.info("🎨 Modern Glassmorphism UI")

        st.info("📋 Property Summary")

        st.info("📄 CSV Report Download")

        st.info("⚡ Fast Predictions")

    st.divider()

    # -------------------------------------------------
    # Dataset
    # -------------------------------------------------

    st.markdown("""
    <div class='card'>

    <h2>📁 Dataset</h2>

    Housing.csv

    Features include:

    ✔ Area

    ✔ Bedrooms

    ✔ Bathrooms

    ✔ Stories

    ✔ Parking

    ✔ Air Conditioning

    ✔ Furnishing Status

    ✔ House Price

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # -------------------------------------------------
    # Developer
    # -------------------------------------------------

    st.subheader("👨‍💻 Developer")

    st.markdown("""
    **Name:** Sai Teja Reddy

    **Role:** AI & Machine Learning Enthusiast

    **Projects:**

    • Iris Flower Classification

    • Spam Mail Detector

    • House Price Prediction

    • Upcoming: RAG Chatbot & AI Projects
    """)

    st.divider()

    # -------------------------------------------------
    # Future Scope
    # -------------------------------------------------

    st.subheader("🚀 Future Enhancements")

    st.markdown("""
    - Deep Learning Models

    - XGBoost & Random Forest Comparison

    - House Image Upload

    - Location-Based Price Prediction

    - Interactive Maps

    - AI Investment Suggestions

    - PDF Report Generation

    - User Login System

    - Cloud Deployment
    """)

    st.divider()

    st.success("✅ House Price Prediction Dashboard Version 1.0")

    st.caption(
        "© 2026 House Price Prediction AI | Developed using Python, Streamlit & Scikit-Learn"
    )