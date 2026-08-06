import streamlit as st
from utils import apply_theme

def home_page():

    apply_theme()

    st.markdown(
        """
        <div class='title'>
        🏠 House Price Prediction AI
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='subtitle'>
        Predict property prices instantly using Machine Learning.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown(
            """
            <div class='card'>
            <h2>🚀 Project Overview</h2>

            This application predicts the estimated selling price of a
            house using a Machine Learning Linear Regression model.

            <br><br>

            ✔ Area

            ✔ Bedrooms

            ✔ Bathrooms

            ✔ Stories

            ✔ Parking

            ✔ Air Conditioning

            ✔ Preferred Area

            ✔ Furnishing Status

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.metric(
            "Model",
            "Linear Regression"
        )

        st.metric(
            "Prediction",
            "House Price"
        )

        st.metric(
            "Framework",
            "Streamlit"
        )

    st.write("")
    st.write("")

    st.markdown("## 📊 Features")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """
            <div class='card'>

            <h3>🏡 Smart Prediction</h3>

            Predict house prices in seconds using Machine Learning.

            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            """
            <div class='card'>

            <h3>📈 Analytics</h3>

            Visualize property information and predictions.

            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            """
            <div class='card'>

            <h3>⚡ Fast & Accurate</h3>

            Quick predictions powered by Scikit-Learn.

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    st.markdown("## 💻 Technologies Used")

    tech1, tech2, tech3, tech4 = st.columns(4)

    tech1.success("Python")

    tech2.success("Streamlit")

    tech3.success("Scikit-Learn")

    tech4.success("Pandas")

    st.write("")
    st.write("")

    st.markdown(
        """
        <div class='card'>

        <h2>🎯 How to Use</h2>

        <ol>

        <li>Open the <b>Prediction</b> page.</li>

        <li>Enter the house details.</li>

        <li>Click <b>Predict Price</b>.</li>

        <li>View the estimated property price.</li>

        </ol>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.info(
        "👈 Use the sidebar to navigate to the Prediction Dashboard."
    )

    st.divider()

    st.caption(
        "© 2026 House Price Prediction AI | Built with ❤️ using Streamlit"
    )