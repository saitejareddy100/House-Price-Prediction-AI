import streamlit as st
import base64
import joblib
from pathlib import Path
import pandas as pd

# -------------------------------------------------------
# Base Directory
# -------------------------------------------------------

BASE_DIR = Path(__file__).parent

# -------------------------------------------------------
# Load Model
# -------------------------------------------------------

@st.cache_resource
@st.cache_resource
def load_model():

    model_path = BASE_DIR / "house_price_model.pkl"

    if not model_path.exists():
        st.error("❌ house_price_model.pkl not found.")
        st.stop()

    return joblib.load(model_path)

# -------------------------------------------------------
# Background Image
# -------------------------------------------------------

def get_base64(file_path):

    try:
        with open(file_path, "rb") as image:
            return base64.b64encode(image.read()).decode()

    except FileNotFoundError:
        return ""

# -------------------------------------------------------
# Apply Custom Theme
# -------------------------------------------------------

def apply_theme():
    image_path = BASE_DIR / "images" / "background.png"

    if image_path.exists():
        img = get_base64(image_path)
        background_css = f"""
        background:
        linear-gradient(rgba(0,0,0,.72), rgba(0,0,0,.72)),
        url("data:image/png;base64,{img}");
        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;
        background-attachment:fixed;
        """
    else:
        background_css = "background:#0E1117;"

    st.markdown(
        f"""
<style>
.stApp{{
{background_css}
}}
section[data-testid="stSidebar"]{{
background:rgba(15,23,42,.95);
backdrop-filter:blur(10px);
}}
#MainMenu{{visibility:hidden;}}
footer{{visibility:hidden;}}
header{{visibility:hidden;}}
.title{{
font-size:50px;
font-weight:bold;
color:white;
}}
.subtitle{{
font-size:20px;
color:#E2E8F0;
}}
.card{{
background:rgba(255,255,255,.10);
padding:25px;
border-radius:20px;
backdrop-filter:blur(8px);
box-shadow:0px 8px 25px rgba(0,0,0,.30);
margin-bottom:20px;
color:white;
}}
.metric-card{{
background:rgba(255,255,255,.12);
padding:18px;
border-radius:15px;
text-align:center;
}}
.result-card{{
background:#16A34A;
padding:35px;
border-radius:20px;
text-align:center;
font-size:34px;
font-weight:bold;
color:white;
box-shadow:0px 10px 25px rgba(0,0,0,.30);
}}
.stButton>button{{
width:100%;
height:55px;
font-size:20px;
font-weight:bold;
background:#00C853;
color:white;
border-radius:15px;
border:none;
}}
.stButton>button:hover{{
background:#00E676;
color:black;
}}
div[data-testid="stDataFrame"]{{
border-radius:15px;
overflow:hidden;
}}
div[data-testid="metric-container"]{{
background:rgba(255,255,255,.12);
border-radius:15px;
padding:15px;
}}
</style>
""",
        unsafe_allow_html=True,
    )
# -------------------------------------------------------
# Prediction Input
# -------------------------------------------------------

def create_dataframe(
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
    furnishing,
):

    data = pd.DataFrame(
        {
            "area": [area],
            "bedrooms": [bedrooms],
            "bathrooms": [bathrooms],
            "stories": [stories],
            "mainroad": [1 if mainroad == "Yes" else 0],
            "guestroom": [1 if guestroom == "Yes" else 0],
            "basement": [1 if basement == "Yes" else 0],
            "hotwaterheating": [1 if hotwater == "Yes" else 0],
            "airconditioning": [1 if airconditioning == "Yes" else 0],
            "parking": [parking],
            "prefarea": [1 if prefarea == "Yes" else 0],
            "furnishingstatus_semi-furnished": [
                1 if furnishing == "semi-furnished" else 0
            ],
            "furnishingstatus_unfurnished": [
                1 if furnishing == "unfurnished" else 0
            ],
        }
    )

    return data

# -------------------------------------------------------
# Prediction
# -------------------------------------------------------

def predict_price(df):

    model = load_model()

    try:

        prediction = model.predict(df)

        return float(prediction[0])

    except Exception as e:

        st.error(f"Prediction Error: {e}")

        return None