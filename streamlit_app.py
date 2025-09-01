import streamlit as st
import plotly.graph_objects as go

st.title("点の操作（スライダーで移動）")

# スライダーで座標入力
x = st.slider("X 座標", -10.0, 10.0, 0.0, step=0.1)
y = st.slider("Y 座標", -10.0, 10.0, 0.0, step=0.1)

# 点を描画するPlotlyグラフ
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[x],
    y=[y],
    mode='markers',
    marker=dict(size=10, color='red')
))

# 軸の範囲とスタイル
fig.update_layout(
    xaxis=dict(range=[-10, 10]),
    yaxis=dict(range=[-10, 10]),
    width=500,
    height=500,
    title="スライダーで点を移動",
    showlegend=False
)

# グラフ表示
st.plotly_chart(fig)
