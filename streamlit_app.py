import streamlit as st
import matplotlib.pyplot as plt

st.title("点の操作（方向ボタンで移動）")

# セッション状態の初期化
if "x" not in st.session_state:
    st.session_state.x = 0.0
if "y" not in st.session_state:
    st.session_state.y = 0.0

# 移動量
step = 0.1

# 操作ボタンの表示
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("⬆️ 上"):
        st.session_state.y += step

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("⬅️ 左"):
        st.session_state.x -= step
with col2:
    st.write("位置調整")
with col3:
    if st.button("➡️ 右"):
        st.session_state.x += step

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("⬇️ 下"):
        st.session_state.y -= step

# グラフ描画
fig, ax = plt.subplots()
ax.plot(st.session_state.x, st.session_state.y, 'ro')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True)

st.pyplot(fig)

# 座標の表示
st.write(f"現在の座標: (x={st.session_state.x:.1f}, y={st.session_state.y:.1f})")
