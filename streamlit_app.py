import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="点をリアルタイム操作", layout="centered")

st.title("点の操作（リアルタイムで）")

# スライダーで座標入力
col1, col2 = st.columns(2)
with col1:
    x = st.slider("X 座標", -10.0, 10.0, 0.0, step=0.1)
with col2:
    y = st.slider("Y 座標", -10.0, 10.0, 0.0, step=0.1)

# Plotly を使ってリアルタイムに近い描画
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[x],
    y=[y],
    mode='markers',
    marker=dict(size=16, color='red'),
))

# レイアウト設定
fig.update_layout(
    xaxis=dict(range=[-10, 10], zeroline=True),
    yaxis=dict(range=[-10, 10], zeroline=True),
    width=500,
    height=500,
    margin=dict(l=20, r=20, t=40, b=20),
    title="点の位置を操作",
    showlegend=False,
)

# Plotly グラフを表示（ラグ少ない）
st.plotly_chart(fig, use_container_width=True)
