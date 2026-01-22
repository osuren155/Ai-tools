from PIL import Image
import streamlit as st
import base64
import os

st.set_page_config(layout="wide")

# ---------- TITLE ----------
st.markdown(
    '<h1 style="text-align: center;">Detailed Summary: AI Tools Usage Dataset (2025)</h1>',
    unsafe_allow_html=True
)

# ---------- BACK BUTTON ----------
if st.button("⬅ Back to Home", key="back_home_dash"):
    st.switch_page("Home.py")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- IMAGE ----------
image_path = r"Q1.jpg"

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
            border-radius: 14px;
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
            <img src="data:image/jpeg;base64,{encoded_img}" alt="Dashboard Image">
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.error("❌ Image file not found")

# ---------- CONTENT ----------
st.markdown("""
# 📊 AI Tools Usage Dataset – Detailed Explanation

This section provides a structured and easy-to-understand explanation of the dataset, 
helping users, analysts, and recruiters quickly grasp the data and its purpose.

---

## 🧩 Column-wise Description

### 🔹 Tool Name
- Name of the AI tool (e.g., ChatGPT, Midjourney, GitHub Copilot).
- Each entry represents a **unique AI product**.
- Useful for tool-level comparison and ranking.

---

### 🔹 Category
- Defines the primary domain of the AI tool.
- Common categories include:
  - **Text**
  - **Image**
  - **Video**
  - **Code**
- Helps analyze **which AI domain is growing fastest**.

---

### 🔹 Launch Date
- Month and year when the AI tool was officially launched.
- Enables **trend analysis over time**.
- Useful to compare **new vs mature tools**.

---

### 🔹 Pricing Model (Free / Paid)
- Indicates whether the tool is:
  - Free
  - Paid
  - Freemium
- Helps evaluate how **pricing impacts user adoption**.

---

### 🔹 Monthly Traffic
- Estimated number of monthly users/visits.
- Higher traffic generally indicates **higher market demand**.
- Useful for popularity and reach analysis.

---

### 🔹 Popularity Score
- A numerical score (out of 100) representing overall popularity.
- Based on usage, brand presence, and market relevance.
- Higher score = stronger market position.

---

## 🎯 Key Insights

- **Text-based AI tools** dominate in both traffic and popularity.
- **Freemium tools** attract more users compared to fully paid tools.
- Recently launched tools can still achieve high popularity with strong features.
- Monthly traffic and popularity score show a **positive correlation**.

---

## 🛠️ Use Cases

This dataset can be effectively used for:

- 📈 **Interactive Dashboards** (Streamlit, Plotly, Power BI)
- 📊 **AI Market Trend Analysis (2023–2025)**
- 🧠 **Category-wise Performance Comparison**
- 💰 **Pricing Model vs User Adoption Analysis**
- 📁 **Data Analyst / Data Science Portfolio Projects**
- 🧪 **Business & Product Research**

---

## 🚀 Project Value

By converting raw AI usage data into meaningful visual insights, 
this project demonstrates strong skills in:

- Data understanding
- Dashboard design
- Analytical thinking
- Real-world AI market analysis

📌 *Created by Surendra Oraon*
""")



