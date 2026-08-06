# 🏠 House Price Prediction AI

A modern Machine Learning web application that predicts house prices based on property features such as area, bedrooms, bathrooms, parking, furnishing status, and more.

Built using **Python**, **Scikit-Learn**, and **Streamlit**, this project provides an interactive dashboard with real-time predictions and analytics.

---

## 📌 Features

- 🏡 Predict house prices instantly
- 📊 Interactive analytics dashboard
- 📈 Data visualization using Plotly
- 🎨 Modern Streamlit UI
- 📱 Responsive dashboard
- ⚡ Fast prediction using Machine Learning
- 📋 User-friendly navigation
- 📂 Professional project structure

---

## 🖼️ Dashboard Preview

### Home Page

- Project Overview
- Technologies Used
- Features
- Model Information

### Prediction Page

- Enter property details
- Predict estimated house price
- Display prediction result

### Analytics Page

- Dataset overview
- Interactive graphs
- Correlation analysis
- Price distribution

### About Page

- Project information
- Technologies
- Dataset details
- Developer information

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Plotly
- Joblib
- Pillow

---

## 📂 Project Structure

```
House prediction/
│
├── app.py
├── utils.py
├── Train_model.py
├── house_price_model.pkl
├── README.md
├── requirements.txt
├── .gitignore
│
├── dataset/
│   └── Housing.csv
│
├── image/
│   └── image.png
│
├── my_pages/
│   ├── home.py
│   ├── prediction.py
│   ├── analytics.py
│   └── about.py
│
└── notebook/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/House-Price-Prediction-AI.git
```

### Navigate to Project

```bash
cd House-Price-Prediction-AI
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Train Model

Run

```bash
python Train_model.py
```

This creates

```
house_price_model.pkl
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open

```
http://localhost:8501
```

---

## 📊 Input Features

The model predicts price using:

- Area
- Bedrooms
- Bathrooms
- Stories
- Main Road
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Parking
- Preferred Area
- Furnishing Status

---

## 🤖 Machine Learning Model

Algorithm Used

```
Linear Regression
```

Workflow

```
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Train/Test Split
      │
      ▼
Linear Regression
      │
      ▼
Model Evaluation
      │
      ▼
Model Saved (.pkl)
      │
      ▼
Streamlit Dashboard
```

---

## 📈 Future Improvements

- Random Forest Regression
- XGBoost
- LightGBM
- Price Confidence Score
- PDF Report Generation
- Cloud Deployment
- User Authentication
- Database Integration

---

## 📸 Screenshots

Add screenshots here after uploading them.

Example

```
screenshots/
    home.png
    prediction.png
    analytics.png
```

---

## 👨‍💻 Author

**Sai Teja**

Machine Learning & Python Developer

GitHub:
https://github.com/saitejareddy100

---

## ⭐ Support

If you like this project,

⭐ Star this repository

Fork it

Contribute with improvements

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

- Streamlit
- Scikit-Learn
- Pandas
- Plotly
- NumPy