import streamlit as st

st.title("🎈 My new app 0519")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import pandas as pd

# ===============================
# 1. 資料載入與基本顯示
# ===============================
st.title("運動表現資料分析")

# 狀態訊息
st.success('分析環境載入成功 ✅')
st.info("請使用側邊欄進行篩選與互動分析", icon='ℹ️')
st.error('This is an error', icon="🚨")

# 載入資料
df = pd.read_csv("bodyPerformance.csv")
df["BMI"] = df["weight_kg"] / ((df["height_cm"] / 100) ** 2)

# 顯示部分資料
st.header("原始資料預覽")
st.dataframe(df.head(50))
