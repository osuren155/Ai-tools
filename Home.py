# py -m streamlit run home.py

import streamlit as st
import base64
import os

# ---------- PAGE CONFIG (MUST BE FIRST) ----------
st.set_page_config(
    page_title="AI Tools Project",
    layout="wide"
)

# ---------- TITLE ----------
st.markdown(
    '<h1 style="text-align: center;">Detailed Summary: AI Tools Usage Dataset (2025)</h1>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- IMAGE ----------
image_path = r"D:\Ai tools\Q3.jpg"

if os.path.exists(image_path):
    with open(image_path, "rb") as img_file:
        encoded_img = base64.b64encode(img_file.read()).decode()

st.markdown(
    f"""
    <style>

    /* ---------- IMAGE CONTAINER ---------- */
    .image-container {{
        width: 110%;
        display: flex;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 40px;
    }}

    .image-container img {{
        width: 80%;
        max-width: 1100px;
        border-radius: 16px;
        box-shadow: 0px 20px 45px rgba(0, 0, 0, 0.35);
    }}

    /* ---------- BUTTON STYLE (SAFE) ---------- */
    div.stButton > button {{
        width: 100%;
        padding: 10px 30px;
        border-radius: 18px;
        font-size: 17px;
        font-weight: 600;
        letter-spacing: 0.5px;

        background: linear-gradient(135deg, #667eea, #764ba2);
        color: #ffffff;

        border: none;
        cursor: pointer;

        box-shadow: 0px 10px 25px rgba(102, 126, 234, 0.45);
        transition: all 0.35s ease;
    }}

    div.stButton > button:hover {{
        transform: translateY(-4px) scale(1.03);
        box-shadow: 0px 18px 35px rgba(118, 75, 162, 0.6);
        background: linear-gradient(135deg, #764ba2, #667eea);
    }}

    div.stButton > button:active {{
        transform: scale(0.98);
        box-shadow: 0px 8px 18px rgba(0, 0, 0, 0.35);
    }}

    </style>

    <div class="image-container">
        <img src="data:image/jpg;base64,{encoded_img}">
    </div>
    """,
    unsafe_allow_html=True
)



st.markdown("<br>", unsafe_allow_html=True)

# ---------- CENTERED BUTTONS ----------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    btn_col1, btn_col2 = st.columns(2)

    with btn_col1:
        if st.button("Dashboard", use_container_width=True):
            st.switch_page("pages/Dashboard.py")

    with btn_col2:
        if st.button(" Summary", use_container_width=True):
            st.switch_page("pages/Summary.py")
            
            

st.markdown("""
## 📊 AI Tools Usage Dashboard – Introduction

This dashboard presents a **comprehensive analysis of AI tools usage data**, 
organized across key dimensions such as:

- **Category**
- **Launch Date**
- **Pricing Model (Free / Paid)**
- **Monthly Traffic**
- **Popularity Score**

### 🎯 Objective
The main objective of this dashboard is to:

- 🔍 Analyze **usage trends across different AI tool categories**
- 📅 Understand **adoption patterns over time** based on launch dates
- 💰 Compare **Free vs Paid tools** in terms of traffic and popularity
- 📈 Identify **high-performing AI tools** using key metrics

### 💡 Key Insight
By converting raw data into **interactive and meaningful visualizations**, 
this dashboard supports **data-driven decision-making** and provides 
clear insights into the **growth of the AI tools ecosystem**.
""")
