# 📈 Qiu Huiting’s KOSPI200 Stock Recommendation System
# English version inspired by the Korean reference site

import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Qiu Huiting’s KOSPI200 Recommender", page_icon="📈", layout="wide")

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
<style>
body { background-color: #f7f7f7; }
h1, h2, h3 { color: #1b3b5f; }
p.subtitle { text-align:center; color:gray; margin-top:-10px; margin-bottom:30px; }
.sidebar .sidebar-content { background-color: #f4f6f9; }
.stButton > button {
    border-radius: 20px;
    background-color: #1b6ca8;
    color: white;
    font-weight: 600;
    padding: 8px 25px;
}
.table th, .table td {
    padding: 8px 12px;
}
.card {
    background-color: white;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1>📊 KOSPI200 Stock Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>A simple analysis tool to help beginners understand KOSPI200 market trends</p>", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Settings")

api_key = st.sidebar.text_input("🔑 API Key Information (optional)", placeholder="Enter your API key here")
st.sidebar.markdown("---")

st.sidebar.header("📊 Analysis Settings")
num_stocks = st.sidebar.slider("Number of recommended stocks", 1, 20, 5)
min_volume = st.sidebar.slider("Minimum trading volume (in 100M KRW)", 10, 500, 100)

st.sidebar.markdown("---")
st.sidebar.header("🔁 Data Refresh")
if st.sidebar.button("Update Data"):
    st.sidebar.success("Data updated successfully!")

# ---------------- MAIN CONTENT ----------------
st.markdown("### 🧩 How to Start the Analysis")
st.info("Please enter your API key in the left menu and click **‘Start Analysis’** after selecting settings!")

st.markdown("## 📘 What is this tool?")
st.markdown("""
This dashboard automatically analyzes **KOSPI200 companies**  
and recommends stocks with good potential for buying decisions.

**Analysis criteria include:**
- 📈 **Uptrend check**: Detects whether prices are showing upward momentum  
- ⚡ **Rising speed**: Evaluates how fast prices have increased recently  
- 💹 **Trading activity**: Measures how actively the stock is being traded  
- 💰 **Fair price zone**: Avoids stocks that are too expensive or too cheap  
- 🧠 **Stability**: Prefers stocks with smaller price fluctuations
""")

# ---------------- SCORE TABLE ----------------
st.markdown("## 💯 How is the recommendation score calculated?")

score_data = {
    "Criteria": [
        "Uptrend continuation",
        "Strong upward momentum",
        "Increased trading volume",
        "Reasonable price range",
        "Rise vs. previous day",
        "Low price volatility"
    ],
    "Score": [
        "+4 points",
        "+2 ~ +3 points",
        "+1 ~ +2 points",
        "+1.5 points",
        "+1 point",
        "+0.5 ~ +1 point"
    ]
}
score_df = pd.DataFrame(score_data)

st.table(score_df)

# ---------------- DEMO RESULT SECTION ----------------
st.markdown("## 📈 Example of Recommended Stocks (Demo Data)")
demo_data = {
    "Rank": [1, 2, 3, 4, 5],
    "Company": ["Samsung Electronics", "LG Chem", "Hyundai Motor", "Kakao Corp", "SK Hynix"],
    "Score": [96, 91, 89, 87, 85],
    "Trend": ["⬆️ Strong Uptrend", "⬆️ Uptrend", "↗️ Moderate", "➡️ Stable", "⬆️ Uptrend"]
}
demo_df = pd.DataFrame(demo_data)
st.dataframe(demo_df, use_container_width=True)

st.success("✅ Analysis complete! This is demo data for layout preview.")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:gray;'>© 2025 Qiu Huiting | Built with Streamlit & ❤️</p>",
    unsafe_allow_html=True
)
