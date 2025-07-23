
import streamlit as st
from agents.code_writer import write_game
from agents.code_runner import run_game
from dotenv import load_dotenv

load_dotenv("api.env")

# --- PAGE CONFIG (Dark Theme + Custom CSS) ---
st.set_page_config(
    page_title="www.gameforgeAI.com", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    /* --- GLOBAL STYLES --- */
    body {
        background: linear-gradient(135deg, #0f0f0f, #1a1a2e);
        font-family: 'Segoe UI', sans-serif;
        color: #ffffff;
    }
    
    /* --- SIDEBAR STYLES --- */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .sidebar-title {
        font-size: 24px;
        font-weight: 700;
        background: linear-gradient(90deg, #00dbde, #fc00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* --- BUTTON STYLES --- */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 30px;
        padding: 12px 30px;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 20px rgba(0, 0, 0, 0.3);
    }
    
    /* --- TEXT AREA --- */
    .stTextArea > div > div > textarea {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        color: white;
        font-size: 16px;
    }
    
    /* --- EXPANDER STYLES --- */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 10px;
        color: white !important;
    }
    
    /* --- FOOTER --- */
    .footer {
        text-align: center;
        padding: 30px;
        color: gray;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<div class="sidebar-title">🎮 GameForge AI</div>', unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("### 🧭 Navigation")
    st.markdown("- **🏠 Home**\n- **🎮 Game generates**\n- **🗂️ Saved Profiles**")
    st.markdown("---")
    
    st.markdown("### 🛠️ How It Works")
    st.markdown("""
    1. **Describe** your dream game
    2. **AI generates** Python code instantly
    3. **Runs automatically** - no setup needed
    """)
    st.markdown("---")
    
    st.markdown("### 📞 Support")
    st.markdown("""
    **Issues?**  
    📧 **tushar80rt@gmail.com**
    """)

# --- MAIN CONTENT ---
st.markdown("<h1 style='text-align: center; font-size: 48px; color: white;'>⚡ GameForge AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray; font-size: 20px;'>Transform your game ideas into reality in seconds</p>", unsafe_allow_html=True)
st.markdown("---")

# Game Input
st.markdown("### 🎯 Describe Your Game")
user_input = st.text_area(
    "",
    placeholder="🕹️ 'A space shooter with power-ups and boss battles' or 'A 2D platformer with pixel art'",
    height=120
)

# Generate Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Generate & Run Game", use_container_width=True):
        if not user_input.strip():
            st.error("❗ Please describe your game first!")
        else:
            with st.spinner("🤖 AI agents are crafting your game..."):
                progress_bar = st.progress(0)
                status_text = st.empty()

                try:
                    # Step 1: Write Code
                    progress_bar.progress(25)
                    status_text.markdown("### 📝 Writing game code...")
                    code_output = write_game(user_input)
                    
                    with st.expander("📄 View Generated Code", expanded=True):
                        st.code(code_output, language="python")

                    # Step 2: Run Game
                    progress_bar.progress(75)
                    status_text.markdown("### 🎮 Launching your game...")
                    run_output = run_game("game.py")
                    
                    with st.expander("🚀 Game Output", expanded=True):
                        st.success("✅ Game launched successfully!")
                        st.text(run_output)

                    progress_bar.progress(100)
                    status_text.empty()
                    
                    st.balloons()
                    st.success("🎉 Your game is ready to play!")

                except Exception as e:
                    st.error(f"💥 Error: {str(e)}")
                    st.info("📧 Contact support if this persists")

st.markdown(
    """
    <div class="footer">
        <p>© 2025 GameForge AI | Built with CAMEL-AI & OpenAI</p>
        <div style="display: flex; justify-content: center; gap: 20px;">
            <a href="#" style="color: #667eea;">Terms</a>
            <a href="#" style="color: #667eea;">Privacy</a>
            <a href="#" style="color: #667eea;">GitHub</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
