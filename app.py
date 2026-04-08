import streamlit as st
from env.env import AIOpsEnv
import time

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="AI Ops Control", layout="wide")

env = AIOpsEnv()

# =========================
# CUSTOM CSS (CYBERPUNK UI)
# =========================
st.markdown("""
<style>
body {
    background-color: #020617;
    color: white;
}

.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: cyan;
    text-shadow: 0px 0px 20px cyan;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 25px rgba(0,255,255,0.2);
    text-align: center;
}

.glow {
    text-shadow: 0 0 10px cyan, 0 0 20px cyan;
}

.btn {
    background-color: transparent;
    border: 2px solid cyan;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    cursor: pointer;
}

.log-box {
    background: black;
    padding: 15px;
    border-radius: 10px;
    font-family: monospace;
    color: lime;
}

.memory-box {
    background: rgba(255,255,255,0.03);
    padding: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<div class='title'>🤖 AI OPS CONTROL CENTER</div>", unsafe_allow_html=True)

# =========================
# SELECT TASK
# =========================
level = st.selectbox("⚡ Select Scenario", ["easy", "medium", "hard"])

obs = env.reset(level)

# =========================
# METRICS
# =========================
col1, col2, col3 = st.columns(3)

col1.markdown(f"<div class='card glow'>🔥 CPU<br><h1>{obs.cpu}%</h1></div>", unsafe_allow_html=True)
col2.markdown(f"<div class='card glow'>💾 Memory<br><h1>{obs.memory}%</h1></div>", unsafe_allow_html=True)
col3.markdown(f"<div class='card glow'>⚠️ Errors<br><h1>{obs.errors}</h1></div>", unsafe_allow_html=True)

# =========================
# PROGRESS BARS
# =========================
st.markdown("### 📊 System Load")

st.progress(int(obs.cpu))
st.progress(int(obs.memory))

# =========================
# ANOMALY
# =========================
if obs.anomaly:
    st.error("🚨 CRITICAL ANOMALY DETECTED")
else:
    st.success("✅ SYSTEM STABLE")

# =========================
# LOGS
# =========================
st.markdown("### 📜 SYSTEM LOG TERMINAL")
st.markdown(f"<div class='log-box'>{obs.logs}</div>", unsafe_allow_html=True)

# =========================
# AI STATUS PANEL
# =========================
st.markdown("### 🧠 AI STATUS")

status_col1, status_col2 = st.columns(2)

status_col1.metric("Agent Mode", "Autonomous")
status_col2.metric("Health Score", f"{100 - obs.errors}%")

# =========================
# ACTION PANEL
# =========================
st.markdown("### 🎮 CONTROL PANEL")

c1, c2, c3 = st.columns(3)

action = None

if c1.button("🚀 SCALE SYSTEM"):
    action = "scale"

if c2.button("🔁 RESTART SERVICE"):
    action = "restart"

if c3.button("😴 IGNORE"):
    action = "ignore"

# =========================
# RESULT
# =========================
if action:
    with st.spinner("AI processing decision..."):
        time.sleep(1)

    _, reward, _, info = env.step({"action": action})

    st.markdown("### 📊 RESULT")

    if reward > 0:
        st.success(f"✅ SUCCESS | Reward: {reward}")
    else:
        st.error(f"❌ FAILURE | Reward: {reward}")

    st.info(f"🧠 Explanation: {info['explanation']}")

# =========================
# MEMORY TIMELINE
# =========================
st.markdown("### 🧠 MEMORY TIMELINE")

if env.memory.history:
    for i, (s, a) in enumerate(env.memory.history):
        st.markdown(f"<div class='memory-box'>Step {i+1}: Action → {a}</div>", unsafe_allow_html=True)
else:
    st.write("No actions yet")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("🚀 Built with AI | Autonomous Ops Simulation")