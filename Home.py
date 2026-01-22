# py -m streamlit run home.py

import streamlit as st
import base64
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI Tools Project",
    layout="wide"
)

# ---------- TITLE ----------
st.markdown(
    '<h1 style="text-align: center;">AI Tools Usage (2025)</h1>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- IMAGE ----------
image_path = r"Q3.jpg"

if os.path.exists(image_path):
    with open(image_path, "rb") as img_file:
        encoded_img = base64.b64encode(img_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .image-container {{
            display: flex;
            justify-content: center;
            margin-top: 20px;
            margin-bottom: 40px;
        }}

        .image-container img {{
            width: 100%;
            max-width: 1100px;
            border-radius: 16px;
            box-shadow: 0px 20px 45px rgba(0, 0, 0, 0.35);
        }}

        /* ---------- BUTTON STYLE ---------- */
        div.stButton > button {{
            width: 100%;
            padding: 10px 30px;
            border-radius: 18px;
            font-size: 17px;
            font-weight: 600;

            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            cursor: pointer;

            box-shadow: 0px 10px 25px rgba(102, 126, 234, 0.45);
            transition: all 0.3s ease;
        }}

        div.stButton > button:hover {{
            transform: translateY(-3px);
            box-shadow: 0px 18px 35px rgba(118, 75, 162, 0.6);
        }}
        </style>

        <div class="image-container">
            <img src="data:image/jpeg;base64,{encoded_img}">
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.error("❌ Image not found")

# ---------- BUTTONS ----------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    b1, b2 = st.columns(2)

    with b1:
        if st.button("Dashboard", use_container_width=True):
            st.switch_page("pages/Dashboard.py")

    with b2:
        if st.button("Summary", use_container_width=True):
            st.switch_page("pages/Summary.py")

# ---------- INTRO ----------
st.markdown("""
## 📊 Dashboard – Introduction

This dashboard presents a **comprehensive and interactive analysis of AI tools usage data**, organized across key dimensions such as:

- **Category** (Text, Image, Video, Code)  
- **Launch Date**  
- **Pricing Model** (Free / Paid / Both)  
- **Monthly Traffic**  
- **Popularity Score**

---

## 🎯 Objectives

- Analyze **AI tools usage trends over time**  
- Understand **adoption patterns across categories**  
- Compare **Free vs Paid tools performance**  
- Identify **top-performing and high-growth AI tools**  
- Support **data-driven insights for product and market analysis**

---

## 💡 Key Insights

- Discover **which AI categories dominate user traffic**  
- Track **growth patterns of newly launched AI tools**  
- Evaluate how **pricing models impact adoption and popularity**  
- Highlight **tools with high traffic but lower popularity (and vice versa)**

---

## 🚀 Value of This Dashboard

This dashboard transforms **raw Kaggle data into meaningful visual insights** using interactive charts and filters, enabling:

- Faster decision-making  
- Clear trend identification  
- Effective storytelling through data  

It is especially useful for **data analysts, researchers, and AI enthusiasts** exploring the evolving AI tools ecosystem.
""")
