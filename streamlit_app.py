import streamlit as st

# 初期位置をセッションで保持
pos = st.session_state.setdefault("pos", {"x": 0, "y": 0})

# キー入力を取得（簡易）
key = st.text_input("←↑↓→キーで操作", label_visibility="collapsed")

# キーに応じて座標を更新
match key:
    case "ArrowUp": pos["y"] -= 1
    case "ArrowDown": pos["y"] += 1
    case "ArrowLeft": pos["x"] -= 1
    case "ArrowRight": pos["x"] += 1

# キー入力をクリア（繰り返し使えるように）
st.session_state["key"] = ""

# 点を表示するHTML（中心からずらして表示）
st.markdown(f"""
<div style="width:300px; height:300px; border:1px solid #999; position:relative;">
  <div style="
    width:10px; height:10px; background:red; border-radius:50%;
    position:absolute;
    left:{150 + pos['x']*10}px;
    top:{150 + pos['y']*10}px;">
  </div>
</div>
""", unsafe_allow_html=True)

# JSでキーをinputに送る（これだけ）
st.markdown("""
<script>
document.addEventListener("keydown", (e) => {
  const keys = ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"];
  if (keys.includes(e.key)) {
    document.querySelector('input').value = e.key;
    document.querySelector('input').dispatchEvent(new Event('input', {bubbles: true}));
  }
});
</script>
""", unsafe_allow_html=True)
