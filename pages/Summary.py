from PIL import Image
import streamlit as st
import base64

st.set_page_config( layout="wide")

# ---------- TITLE ----------
st.markdown(
    '<h1 style="text-align: center;">Detailed Summary: AI Tools Usage Dataset (2025) </h1>',
    unsafe_allow_html=True
)

# ---------- BACK BUTTON ----------
if st.button("⬅ Back to Home", key="back_home_dash"):
    st.switch_page("Home.py")

st.markdown("<br>", unsafe_allow_html=True)

image_path = "Q1.jpg"

with open(image_path, "rb") as img_file:
    encoded_img = base64.b64encode(img_file.read()).decode()

st.markdown(
    f"""
    <style>
    .image-container {{
        position: relative;
        width: 110%;
        display: flex;
        justify-content: center;
    }}

    .image-container img {{
        width: 80%;
        border-radius: 12px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.4);
    }}

    /* Button styling */
    div.stButton > button {{
        background: rgba(0,0,0,0.75);
        color: white;
        padding: 12px 26px;
        border-radius: 14px;
        font-size: 15px;
        font-weight: 500;
        border: none;
        transition: all 0.3s ease;
    }}

    div.stButton > button:hover {{
        background: rgba(20,20,20,0.95);
        transform: translateY(-3px);
    }}
    </style>

    <div class="image-container">
        <img src="data:image/jpg;base64,{encoded_img}" alt="Dashboard Image">
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown("""
# AI Tools Usage Dataset Summary

This dataset provides a concise yet insightful overview of popular **Artificial Intelligence (AI) tools** used across different domains such as **Text, Image, Video, and Code**.  
It is designed to analyze tool popularity, user adoption, and emerging trends in the AI ecosystem.

---

## 🔢 Dataset Overview
- **Total Records:** 15 AI tools  
- **Total Columns:** 6  
- **Data Types:**
  - **Categorical (String):** 4 columns  
  - **Numerical (Integer):** 2 columns  

The dataset is clean, well-structured, and contains **no missing values**, making it ideal for visualization and dashboard development.

---

## 🧩 Column-wise Description

### 🔹 Tool Name
- Contains the names of widely used AI tools such as ChatGPT, MidJourney, GitHub Copilot, etc.  
- Each row represents a unique AI product.

### 🔹 Category
- Describes the primary functionality of the AI tool.  
- Categories include:
  - **Text**
  - **Image**
  - **Video**
  - **Code**  
- Useful for category-wise comparison and trend analysis.

### 🔹 Launch Date
- Indicates the month and year when the tool was launched.  
- Helps in understanding the relationship between launch time and popularity.

### 🔹 Free / Paid
- Shows the pricing model of each AI tool:
  - Free
  - Paid
  - Freemium  
- Useful for analyzing how pricing impacts user adoption.

### 🔹 Monthly Traffic
- Represents estimated monthly user visits.  
- Values range from millions to billions, indicating varying levels of market reach.

### 🔹 Popularity Score
- A numeric score (out of 100) representing the overall popularity of the tool.  
- Scores range approximately from **75 to 98**, with a high average popularity.

---

## 📈 Key Insights

- **Text-based AI tools** dominate in terms of monthly traffic and popularity.
- **Free and Freemium tools** generally attract more users than fully paid tools.
- Some newly launched tools show high popularity due to strong features and branding.
- Monthly traffic and popularity score are positively correlated, but usability and accessibility also matter.

---

## 🎯 Use Cases

- Interactive dashboards using **Streamlit**, **Plotly**, or **Power BI**
- AI market trend analysis (2023–2025)
- Data Analyst / Data Science portfolio projects
- Pricing model vs adoption analysis
- Category-wise AI tool performance comparison

---

📌 *Created by Surendra Oraon*
""")

