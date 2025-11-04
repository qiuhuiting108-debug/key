# 📈 Qiu Huiting’s KOSPI200 Explorer — Enhanced Version

import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from io import StringIO

# --- Page config ---
st.set_page_config(page_title="Qiu Huiting’s KOSPI200 Explorer", page_icon="📈", layout="wide")

# --- CSS style ---
st.markdown("""
<style>
body { background-color: #f7f7f7; }
h1 { text-align: center; font-weight: 800; color: #222; }
.card { background-color: white; border-radius: 16px; padding: 20px; margin-bottom: 20px; box-shadow: 0px 2px 6px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1>📈 KOSPI200 Explorer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Explore KOSPI200 index with advanced visuals and statistics</p>", unsafe_allow_html=True)

# --- Sidebar inputs ---
st.sidebar.header("Settings")
symbol = st.sidebar.text_input("Stock/Index Symbol", value="^KS200")
time_range = st.sidebar.selectbox("Time Range", ["1M", "3M", "6M", "1Y", "All"])

upload_csv = st.sidebar.file_uploader("Upload CSV (fallback)", type=["csv"])

# --- Data fetching / loading ---
def fetch_data(symbol):
    # placeholder: fetch via some API or use uploaded CSV
    url = f"https://stooq.com/q/d/l/?s={symbol}&i=d"
    r = requests.get(url)
    r.raise_for_status()
    df = pd.read_csv(StringIO(r.text))
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")
    return df

if upload_csv is not None:
    df = pd.read_csv(upload_csv)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")
else:
    try:
        df = fetch_data(symbol)
    except Exception as e:
        st.error(f"Failed to fetch data: {e}")
        st.stop()

# --- Filter by time range ---
end_date = df["Date"].max()
if time_range != "All":
    mapping = {"1M": 30, "3M": 90, "6M": 180, "1Y": 365}
    days = mapping.get(time_range, 365)
    start_date = end_date - pd.Timedelta(days=days)
    df = df[df["Date"] >= start_date]

# --- Statistics cards ---
latest = df.iloc[-1]
highest = df["High"].max()
lowest = df["Low"].min()
pct_change = (latest["Close"] / df.iloc[0]["Close"] - 1) * 100

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"<div class='card'><h3>Latest Close</h3><p>{latest['Close']:.2f}</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='card'><h3>52-Week High</h3><p>{highest:.2f}</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='card'><h3>Change (%)</h3><p>{pct_change:.2f}%</p></div>", unsafe_allow_html=True)

# --- Chart ---
fig = px.line(df, x="Date", y="Close", title=f"{symbol} Close Price")
fig.update_layout(plot_bgcolor="white", xaxis_title="", yaxis_title="Price (KRW)")
st.plotly_chart(fig, use_container_width=True)

# --- Additional visuals: Moving average ---
df["MA20"] = df["Close"].rolling(window=20).mean()
fig2 = px.line(df, x="Date", y=["Close", "MA20"], title="Close & MA20")
fig2.update_layout(plot_bgcolor="white", xaxis_title="", yaxis_title="Price (KRW)")
st.plotly_chart(fig2, use_container_width=True)

# --- Data table last rows ---
st.markdown("<div class='card'><h3>Recent Data</h3></div>", unsafe_allow_html=True)
st.dataframe(df.tail(10), use_container_width=True)
