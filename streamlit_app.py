import streamlit as st
import matplotlib.pyplot as plt

st.title("点の操作（スライダーで）")

# 点の座標をスライダーで調整
x = st.slider("X 座標", -10.0, 10.0, 0.0, 0.1)
y = st.slider("Y 座標", -10.0, 10.0, 0.0, 0.1)

# グラフ描画
fig, ax = plt.subplots()
ax.plot(x, y, 'ro')  # 赤い点
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True)

st.pyplot(fig)
