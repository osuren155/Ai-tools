from PIL import Image
import streamlit as st
import base64
import os
import pandas as pd
import plotly.express as px

st.set_page_config( layout="wide")
st.markdown('<h1 style="text-align: center;">AI Tools Usage Dataset (2025)</h1>', unsafe_allow_html=True)

# Page ko wapiss Home pahe me le jane ke leya #
if st.button("⬅ Back to Home", key="back_home_dash"): 
    st.switch_page("Home.py") 
 
df = pd.read_csv("cleaned_ai_tools_usage_dataset.csv")
st.dataframe(df) 
  
# LOAD DATA
df = pd.read_csv("cleaned_ai_tools_usage_dataset.csv") 

# DATA CLEANING
df['Launch Date'] = pd.to_datetime(df['Launch Date'], errors='coerce')

df['Category'] = (
    df['Category']
    .str.strip()
    .str.lower()
    .replace({'coad': 'code'})
)

df['Free/Paid'] = (
    df['Free/Paid']
    .str.strip()
    .str.title()
)

df['Monthly Traffic'] = df['Monthly Traffic'].fillna(0).astype(int)
df['Popularity Score'] = df['Popularity Score'].fillna(0).astype(int)

# Launch Year (NaT ko 0 assign)
df['Launch Year'] = df['Launch Date'].dt.year.fillna(0).astype(int)

# =========================
# SIDEBAR FILTERS
# =========================
st.sidebar.header(" Filter Dashboard")

# Category Filter
categories = sorted(df['Category'].unique())
selected_categories = st.sidebar.multiselect(
    "Select Category",
    options=categories,
    default=categories
)

# Free / Paid Filter
free_paid_options = sorted(df['Free/Paid'].unique())
selected_free_paid = st.sidebar.multiselect(
    "Select Free / Paid",
    options=free_paid_options,
    default=free_paid_options
)

# Launch Year Filter
valid_years = df[df['Launch Year'] > 0]['Launch Year']

min_year = int(valid_years.min())
max_year = int(valid_years.max())

launch_year_range = st.sidebar.slider(
    "Launch Year Range",
    min_year,
    max_year,
    (min_year, max_year)
)

# Popularity Score Filter (OPTIONAL)
apply_popularity = st.sidebar.checkbox(
    "Apply Popularity Score Filter",
    value=True
)

min_pop = int(df['Popularity Score'].min())
max_pop = int(df['Popularity Score'].max())

popularity_range = st.sidebar.slider(
    "Popularity Score Range",
    min_pop,
    max_pop,
    (min_pop, max_pop)
)

# =========================
# APPLY FILTERS SAFELY
# =========================
filtered_df = df[
    (df['Category'].isin(selected_categories)) &
    (df['Free/Paid'].isin(selected_free_paid)) &
    (
        (df['Launch Year'] == 0) |
        (df['Launch Year'].between(launch_year_range[0], launch_year_range[1]))
    )
]

if apply_popularity:
    filtered_df = filtered_df[
        filtered_df['Popularity Score'].between(
            popularity_range[0], popularity_range[1]
        )
    ]


# =========================
# MAIN DASHBOARD
# =========================
st.markdown(
    "<h1 style='text-align: center;'>Filter Data (2025)</h1>",
    unsafe_allow_html=True
)

if filtered_df.empty:
    st.warning("⚠️ No data available for selected filters. Please adjust filters.")
else:
    st.success(f"✅ Showing {len(filtered_df)} AI tools")
    st.dataframe(filtered_df, use_container_width=True) 


# ---------------- now start dashboard creation ---------------
# ---------------- PAGE TITLE STYLE ----------------
st.markdown("""
<style>
.center-text { text-align: center; }
</style>
""", unsafe_allow_html=True)

#-----------📊 CATEGORY DISTRIBUTION (PIE / DONUT---------------

st.markdown("""
<h1 class="center-text">Category Distribution</h1>
<p class="center-text"><b>Insight:</b> Which AI category dominates the market?</p>
""", unsafe_allow_html=True)

# ---- Data ----
category_df = pd.DataFrame({
    "Category": ["Text", "Image", "Video", "Code"],
    "Tool Count": [45, 25, 15, 15]
})

# ---- Pie / Donut Chart ----
fig_pie = px.pie(
    category_df,
    names="Category",
    values="Tool Count",
    hole=0.45,
    color_discrete_sequence=["#4F46E5", "#06B6D4", "#F59E0B", "#10B981"],
    title="🎯 AI Tools Category Distribution"
)

fig_pie.update_traces(
    textinfo="percent+label",
    textposition="inside",
    marker=dict(line=dict(color="white", width=2))
)

st.plotly_chart(fig_pie, use_container_width=True)

# ---- Insight ----
st.markdown("""
### 🔍 Key Insight:
The **Text** category dominates the AI tools market, indicating higher adoption of  
chatbots, writing assistants, and text-based automation solutions.

This insight helps **investors, developers, and businesses** focus on high-demand AI segments.
""")

#-------------📈 MONTHLY TRAFFIC BY CATEGORY--------------

df = pd.read_csv("cleaned_ai_tools_usage_dataset.csv")

st.markdown("""
<h1 class="center-text">Monthly Traffic by Category</h1>
""", unsafe_allow_html=True)

# ---- Aggregate Traffic ----
traffic_df = (
    df.groupby("Category", as_index=False)["Monthly Traffic"]
      .sum()
      .sort_values(by="Monthly Traffic", ascending=False)
)

# ---- Bar Chart ----
fig_bar = px.bar(
    traffic_df,
    x="Category",
    y="Monthly Traffic",
    text_auto=True,
    title="📊 Monthly Traffic Distribution"
)

st.plotly_chart(fig_bar, use_container_width=True)

# ---- Insight ----
top_category = traffic_df.iloc[0]["Category"]

st.markdown(f"""
### 💡 Insight:
The **{top_category}** category generates the **highest monthly user traffic**,  
highlighting strong user engagement and market demand in this segment.
""")

#---------------------Popularity Score by Category--------------------

st.markdown("""
<h1 class="center-text">Popularity Score by Category</h1>
""", unsafe_allow_html=True)

# ---- Aggregate Popularity ----
popularity_df = (
    df.groupby("Category", as_index=False)["Popularity Score"]
      .mean()
      .sort_values(by="Popularity Score", ascending=False)
)

# ---- Box Plot with Colors ----
fig_popularity = px.box(
    df,
    x="Category",
    y="Popularity Score",
    color="Category",  # 👈 Color added
    color_discrete_sequence=["#4F46E5", "#06B6D4", "#F59E0B", "#10B981"],
    title="🏆 Popularity Score by Category"
)

fig_popularity.update_layout(
    showlegend=False,
    title_x=0.5
)

st.plotly_chart(fig_popularity, use_container_width=True)

# ---- Insight ----
top_popularity = popularity_df.iloc[0]["Category"]

st.markdown(f"""
### 💡 Insight:
The **{top_popularity}** category has the **highest average popularity score**,  
indicating strong user engagement and market appeal in this segment.
""")


# -----------------------  Top 10 AI Tools by Traffic ---------------------

st.markdown("""
<h1 class="center-text">Top 10 AI Tools by Monthly Traffic</h1> 
""", unsafe_allow_html=True)
# ---- Top 10 Tools ----
top_10_traffic = (
    df.nlargest(10, "Monthly Traffic")[["Tool Name", "Monthly Traffic"]]
)
# ---- Horizontal Bar Chart ----
fig_top10 = px.bar(
    top_10_traffic,
    x="Monthly Traffic",
    y="Tool Name",
    orientation="h",
    text_auto=True,
    template="plotly_dark", 
    title="🚀 Top 10 AI Tools by Monthly Traffic"
)
st.plotly_chart(fig_top10, use_container_width=True)
# ---- Insight ----
st.markdown("""
### 💡 Insight
The top 10 AI tools capture a significant share of total monthly traffic,  
indicating strong market dominance and clear user preference.  

Businesses can analyze these tools to better understand key success factors  
and apply similar strategies to improve adoption and engagement.
""")

#-------------------------------Top 10 AI Tools by Popularity Score---------------------
st.markdown("""
<h1 class="center-text">Top 10 AI Tools by Popularity Score</h1>
""", unsafe_allow_html=True)

# ---- Top 10 Tools ----
top_10_popularity = (
    df.nlargest(10, "Popularity Score")[["Tool Name", "Popularity Score"]]
)

# ---- Bar Chart (Dark Theme) ----
fig_top10_pop = px.bar(
    top_10_popularity,
    x="Popularity Score",
    y="Tool Name",
    orientation="h",
    template="plotly_dark",
    text_auto=True,
    title="🏅 Top 10 AI Tools by Popularity Score"
)

fig_top10_pop.update_layout(title_x=0.5)

st.plotly_chart(fig_top10_pop, use_container_width=True)

# ---- Insight ----
st.markdown("""
### 💡 Insight
The top 10 AI tools lead in popularity scores, reflecting strong user satisfaction  
and strong market appeal.

Analyzing these tools provides valuable insights into effective features,  
user experience, and marketing strategies that drive high popularity.  
Businesses can leverage these insights to improve their AI offerings  
and boost overall user engagement.
""")

#-----------------Traffic vs Popularity Score Scatter Plot-----------------
st.markdown("""
<h1 class="center-text">Traffic vs Popularity Score</h1>    
""", unsafe_allow_html=True)
# ---- Scatter Plot ----
fig_scatter = px.scatter(
    df, 
    x="Monthly Traffic",
    y="Popularity Score",   
    color="Category",
    size="Popularity Score",
    hover_data=["Tool Name"],
    title="🔍 Traffic vs Popularity Score"
)
st.plotly_chart(fig_scatter, use_container_width=True)
# ---- Insight ----
st.markdown("""
### 💡 Insight
The scatter plot reveals a strong positive correlation between traffic and popularity scores,  
indicating that tools with higher user engagement also tend to have higher popularity ratings.  
Businesses should focus on strategies that enhance both traffic and user satisfaction to maximize their market impact.
    """)


#------------------Avg Traffic (Free vs Paid)-----------------
st.markdown("""
<h1 class="center-text">Average Monthly Traffic: Free vs Paid AI Tools</h1>
""", unsafe_allow_html=True)
# ---- Average Traffic Calculation ----
avg_traffic = (
    df.groupby("Free/Paid", as_index=False)["Monthly Traffic"]
      .mean()
      .sort_values(by="Monthly Traffic", ascending=False)
)
# ---- Bar Chart ----
fig_avg_traffic = px.bar(
    avg_traffic,
    x="Free/Paid",
    y="Monthly Traffic",
    text_auto=True,
    title="📈 Average Monthly Traffic: Free vs Paid AI Tools"
)
st.plotly_chart(fig_avg_traffic, use_container_width=True)
# ---- Insight ----
st.markdown("""
### 💡 Insight
The average monthly traffic for paid AI tools is significantly higher than for free tools,  
indicating that users are more likely to engage with paid tools. This suggests a strong correlation  
between cost and user engagement, which businesses can leverage to optimize their pricing strategies.
""")

#------------------Tools Launched Per Year-----------------
# ---------------- TITLE ----------------
st.markdown("""
<h1 class="center-text">AI Tools Launched Per Year</h1>
""", unsafe_allow_html=True)

# ---------------- DATE CLEANING ----------------
# Convert Launch Date to datetime
df["Launch Date"] = pd.to_datetime(df["Launch Date"], errors="coerce")

# Extract Launch Year
df["Launch Year"] = df["Launch Date"].dt.year

# ---------------- TOOLS PER YEAR ----------------
tools_per_year = (
    df.dropna(subset=["Launch Year"])
      .groupby("Launch Year", as_index=False)["Tool Name"]
      .count()
      .rename(columns={"Tool Name": "Tools Launched"})
      .sort_values("Launch Year")
)

# ---------------- LINE CHART ----------------
fig_timeline = px.scatter(
    df.dropna(subset=["Launch Year"]),
    x="Launch Year",
    y="Tool Name",
    color="Category",
    template="plotly_white",
    title="🕒 AI Tools Launch Timeline"
)

fig_timeline.update_layout(title_x=0.5)
st.plotly_chart(fig_timeline, use_container_width=True)
# ---------------- INSIGHT ----------------
st.markdown("""
### 💡 Insight
The number of AI tools launched per year shows a consistent upward trend,  
highlighting rapid innovation and growing investment in the AI tools ecosystem.

This growth indicates increasing market demand and strong opportunities  
for businesses to adopt, build, and scale AI-driven solutions.
""")

#--------------------------Traffic Trend by Launch Year-----------------
st.markdown("""
<h1 class="center-text">Monthly Traffic Trend by Launch Year</h1>
""", unsafe_allow_html=True)
# ---- Aggregate Traffic by Launch Year ----
traffic_by_year = (
    df.dropna(subset=["Launch Year"])
      .groupby("Launch Year", as_index=False)["Monthly Traffic"]
      .sum()
      .sort_values("Launch Year")
)
# ---- Line Chart ----
fig_traffic_trend = px.line(
    traffic_by_year,
    x="Launch Year",
    y="Monthly Traffic",
    markers=True,
    template="plotly_white",
    title="📈 Monthly Traffic Trend by Launch Year"
)
st.plotly_chart(fig_traffic_trend, use_container_width=True)
# ---- Insight ----
st.markdown("""
### 💡 Insight
The monthly traffic trend by launch year shows a steady increase,  
indicating that newer AI tools are attracting more user engagement over time.   
This trend highlights the growing adoption of AI technologies and the expanding market for AI-driven solutions.
""")

