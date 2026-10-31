import streamlit as st
import time
from paper_brain import generate_answer

st.set_page_config(
    page_title="ML Research Assistant",
    page_icon="🧠",
    layout="wide"
)

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- CSS ---------------- #

st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {
background: linear-gradient(270deg,#0f2027,#203a43,#2c5364,#1f4037);
background-size: 800% 800%;
animation: gradientMove 15s ease infinite;
color:white;
}

@keyframes gradientMove {
0% {background-position:0% 50%;}
50% {background-position:100% 50%;}
100% {background-position:0% 50%;}
}

/* HEADER */

.title {
text-align:center;
font-size:55px;
font-weight:700;
letter-spacing:1px;
}

.subtitle {
text-align:center;
font-size:20px;
opacity:0.8;
margin-bottom:25px;
}

/* REMOVE STREAMLIT INPUT WRAPPERS */

[data-testid="stTextInput"] {
background: transparent !important;
border: none !important;
box-shadow: none !important;
}

[data-testid="stTextInput"] > div {
background: transparent !important;
border: none !important;
}

[data-testid="stTextInput"] > div > div {
background: transparent !important;
border: none !important;
}

/* CENTER SEARCH BAR */

.stTextInput {
display:flex;
justify-content:center;
}

/* SEARCH BAR */

.stTextInput input {
background: rgba(255,255,255,0.08);
border: 1px solid rgba(255,255,255,0.18);
border-radius: 40px;
padding: 18px 25px;
font-size: 17px;
color: white;
width: 850px;
max-width: 90%;
backdrop-filter: blur(14px);
transition: all 0.3s ease;
}

/* PLACEHOLDER */

.stTextInput input::placeholder{
color: rgba(255,255,255,0.6);
}

/* FOCUS EFFECT */

.stTextInput input:focus {
border:1px solid #4cc9f0;
box-shadow:0 0 18px rgba(76,201,240,0.55);
outline:none;
}

/* BUTTON */

.stButton{
display:flex;
justify-content:center;
margin-top:10px;
}

.stButton>button {
border-radius:40px;
padding:14px 35px;
font-size:17px;
font-weight:600;
background:#4cc9f0;
color:black;
border:none;
transition:all 0.3s ease;
}

.stButton>button:hover {
background:#90e0ef;
transform:scale(1.05);
box-shadow:0 0 12px rgba(144,224,239,0.6);
}

/* CHAT BUBBLES */

.chat-user {
background:#4cc9f0;
color:black;
padding:15px;
border-radius:15px;
margin:10px 0;
width:60%;
margin-left:auto;
font-size:16px;
}

.chat-ai {
background: rgba(255,255,255,0.08);
padding:18px;
border-radius:15px;
margin:10px 0;
width:65%;
border:1px solid rgba(255,255,255,0.2);
backdrop-filter: blur(10px);
}

/* THINKING ANIMATION */

.thinking {
display:flex;
gap:5px;
}

.thinking span {
width:8px;
height:8px;
background:white;
border-radius:50%;
animation: blink 1.4s infinite both;
}

.thinking span:nth-child(2) {
animation-delay:0.2s;
}

.thinking span:nth-child(3) {
animation-delay:0.4s;
}

@keyframes blink {
0% {opacity:0.2;}
20% {opacity:1;}
100% {opacity:0.2;}
}

/* FLOATING ICONS */

.icons {
text-align:center;
font-size:30px;
margin-bottom:20px;
}

.icons span {
margin:0 8px;
animation: float 4s ease-in-out infinite;
}

@keyframes float {
0% {transform:translateY(0px);}
50% {transform:translateY(-8px);}
100% {transform:translateY(0px);}
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown('<div class="title">🧠 ML Research Paper Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask questions from your Machine Learning research papers</div>', unsafe_allow_html=True)

st.markdown("""
<div class="icons">
<span>📚</span>
<span>📊</span>
<span>🧠</span>
<span>⚡</span>
<span>🤖</span>
</div>
""", unsafe_allow_html=True)

# ---------------- CHAT HISTORY ---------------- #

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-user">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-ai">{msg["content"]}</div>', unsafe_allow_html=True)

# ---------------- INPUT ---------------- #

query = st.text_input("", placeholder="Ask something about your ML research papers...")

ask = st.button("Ask AI")

# ---------------- AI RESPONSE ---------------- #

if ask and query:

    st.session_state.messages.append({"role":"user","content":query})
    st.markdown(f'<div class="chat-user">{query}</div>', unsafe_allow_html=True)

    thinking = st.empty()

    thinking.markdown(
        """
        <div class="chat-ai">
        <div class="thinking">
        <span></span><span></span><span></span>
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    answer = generate_answer(query)

    thinking.empty()

    placeholder = st.empty()
    typed = ""

    for char in answer:
        typed += char
        placeholder.markdown(
            f'<div class="chat-ai">{typed}</div>',
            unsafe_allow_html=True
        )
        time.sleep(0.01)

    st.session_state.messages.append({"role":"assistant","content":answer})
