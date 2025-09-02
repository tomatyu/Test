import streamlit as st
import streamlit.components.v1 as components

# JavaScriptでマウス座標を取得し、Streamlitに送るHTML+JSコード
component_code = """
<div id="canvas-container" style="position:relative; width: 400px; height: 400px; border:1px solid black;">
  <canvas id="canvas" width="400" height="400" style="background-color: white;"></canvas>
</div>

<script>
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

function drawCircle(x, y) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
    ctx.arc(x, y, 10, 0, 2 * Math.PI);
    ctx.fillStyle = 'red';
    ctx.fill();
}

window.addEventListener('mousemove', (event) => {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    
    if (x >= 0 && x <= rect.width && y >= 0 && y <= rect.height) {
        drawCircle(x, y);
        // Streamlitに座標を送る
        window.parent.postMessage({x: x, y: y}, '*');
    }
});
</script>
"""

# Streamlit側でJavaScriptからのメッセージを受け取るためのiframe埋め込み
# 受け取った座標はsession_stateに保存して画面に表示
coords = st.empty()

components.html(component_code, height=420)

# JavaScriptのpostMessageを受け取るには、Streamlit側では
# 残念ながら直接的なリスナーが標準では用意されていません。
# そこで、代替としてst_js_on_eventなどのサードパーティコンポーネントを使う方法もあります。

st.write("※ こちらのサンプルはマウスの動きに合わせてCanvas内で赤い点が動きます。")
