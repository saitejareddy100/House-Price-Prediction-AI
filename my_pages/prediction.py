import streamlit as st
import pandas as pd

from utils import (
    apply_theme,
    create_dataframe,
    predict_price
)

def prediction_page():

    apply_theme()

    st.markdown(
        """
        <div class='title'>
        🏠 House Price Prediction
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='subtitle'>
        Enter the property details below.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    left, right = st.columns([1,1])

    with left:

        area = st.number_input(
            "Area (sq ft)",
            min_value=500,
            max_value=10000,
            value=2000
        )

        bedrooms = st.slider(
            "Bedrooms",
            1,
            10,
            3
        )

        bathrooms = st.slider(
            "Bathrooms",
            1,
            10,
            2
        )

        stories = st.slider(
            "Stories",
            1,
            4,
            2
        )

        parking = st.slider(
            "Parking",
            0,
            5,
            1
        )

    with right:

        mainroad = st.selectbox(
            "Main Road",
            ["Yes","No"]
        )

        guestroom = st.selectbox(
            "Guest Room",
            ["Yes","No"]
        )

        basement = st.selectbox(
            "Basement",
            ["Yes","No"]
        )

        hotwater = st.selectbox(
            "Hot Water Heating",
            ["Yes","No"]
        )

        airconditioning = st.selectbox(
            "Air Conditioning",
            ["Yes","No"]
        )

        prefarea = st.selectbox(
            "Preferred Area",
            ["Yes","No"]
        )

        furnishing = st.selectbox(
            "Furnishing Status",
            [
                "furnished",
                "semi-furnished",
                "unfurnished"
            ]
        )

    st.write("")

    if st.button("🔍 Predict House Price"):

        data = create_dataframe(
            area,
            bedrooms,
            bathrooms,
            stories,
            mainroad,
            guestroom,
            basement,
            hotwater,
            airconditioning,
            parking,
            prefarea,
            furnishing
        )

        price = predict_price(data)

        st.markdown(
            f"""
            <div class='result-card'>

            💰 Estimated Price

            <br><br>

            ₹ {price:,.2f}

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.success("Prediction completed successfully.")

        st.write("")

        st.subheader("📋 Property Summary")

        summary = pd.DataFrame({
            "Feature":[
                "Area",
                "Bedrooms",
                "Bathrooms",
                "Stories",
                "Parking",
                "Main Road",
                "Guest Room",
                "Basement",
                "Hot Water",
                "Air Conditioning",
                "Preferred Area",
                "Furnishing"
            ],

            "Value":[
                area,
                bedrooms,
                bathrooms,
                stories,
                parking,
                mainroad,
                guestroom,
                basement,
                hotwater,
                airconditioning,
                prefarea,
                furnishing
            ]
        })

        st.dataframe(
            summary,
            use_container_width=True
        )

        st.write("")

        c1,c2,c3 = st.columns(3)

        c1.metric(
            "Area",
            f"{area} sq ft"
        )

        c2.metric(
            "Bedrooms",
            bedrooms
        )

        c3.metric(
            "Bathrooms",
            bathrooms
        )

        st.write("")

        csv = summary.to_csv(index=False)

        st.download_button(
            "📄 Download Report",
            csv,
            file_name="prediction_report.csv",
            mime="text/csv"
        )