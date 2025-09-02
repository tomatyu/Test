import streamlit as st
import time

# 初期位置をセッション状態に保存
if 'x' not in st.session_state:
    st.session_state.x = 200
if 'y' not in st.session_state:
    st.session_state.y = 200
if 'step' not in st.session_state:
    st.session_state.step = 10

# レイアウト
st.title("🔴 AWSDキーで点を動かす（Streamlitのみ）")

# キー入力の代わりにボタンで操作
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("W（↑）"):
        st.session_state.y -= st.session_state.step

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("A（←）"):
        st.session_state.x -= st.session_state.step
with col3:
    if st.button("D（→）"):
        st.session_state.x += st.session_state.step

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("S（↓）"):
        st.session_state.y += st.session_state.step

# キャンバスの描画（matplotlib）
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(4, 4))
ax.set_xlim(0, 400)
ax.set_ylim(0, 400)
ax.set_xticks([])
ax.set_yticks([])
ax.invert_yaxis()  # 上下逆にしてゲームっぽく

# 点の描画
ax.plot(st.session_state.x, st.session_state.y, 'ro', markersize=10)

st.pyplot(fig)

# 座標表示
st.markdown(f"**現在の位置:** x = {st.session_state.x}, y = {st.session_state.y}")
