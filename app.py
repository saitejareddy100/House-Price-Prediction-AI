import streamlit as st
from streamlit_option_menu import option_menu


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="House Price Prediction AI",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Import Pages
# -----------------------------
from my_pages.home import home_page
from my_pages.prediction import prediction_page
from my_pages.analytics import analytics_page
from my_pages.about import about_page

# -----------------------------
# Sidebar Navigation
# -----------------------------
with st.sidebar:

    st.image("image/image.png", use_container_width=True)

    st.markdown("## 🏠 House Price AI")

    selected = option_menu(
        menu_title="Navigation",
        options=[
            "Home",
            "Prediction",
            "Analytics",
            "About"
        ],
        icons=[
            "house-fill",
            "graph-up-arrow",
            "bar-chart-fill",
            "info-circle-fill"
        ],
        menu_icon="cpu-fill",
        default_index=0,
        styles={
            "container": {
                "padding": "5px",
                "background-color": "#0E1117",
            },
            "icon": {
                "color": "#00E676",
                "font-size": "20px",
            },
            "nav-link": {
                "font-size": "17px",
                "text-align": "left",
                "margin": "5px",
                "--hover-color": "#1E293B",
            },
            "nav-link-selected": {
                "background-color": "#00C853",
            },
        },
    )

# -----------------------------
# Load Selected Page
# -----------------------------

if selected == "Home":
    home_page()

elif selected == "Prediction":
    prediction_page()

elif selected == "Analytics":
    analytics_page()

elif selected == "About":
    about_page()