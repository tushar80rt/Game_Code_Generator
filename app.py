import streamlit as st
from agents.code_writer import write_game
from agents.code_runner import run_game
from dotenv import load_dotenv

load_dotenv("api.env")

st.set_page_config(
    page_title="www.game.com", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    st.markdown("""<p style='color: gray; font-size: 14px;'>AI-Powered By CAMEL-AI and OpenAI</p>""", unsafe_allow_html=True)
    st.markdown("###  Navigation")
    st.markdown("- **Home**\n- **Career Assessment**\n- **Saved Profiles**")
    st.markdown("---")
    st.markdown("###  How It Works")
    st.markdown("1. Generate Python Game Code\n2. Save it on Desktop via Terminal Agent\n3. Run the saved game")
    st.markdown("---")
    st.markdown("###  Contact Support")
    st.markdown("<p style='color: gray;'>Having issues?<br>Email: <b>tushar80rt@gmail.com</b></p>", unsafe_allow_html=True)

# Main Content
st.title("⚡ Game Code Generator")
st.markdown("---")
st.markdown("Tell Us About Yourself")

user_input = st.text_area(
    "",
    placeholder="🕹️ Which game do you want to generate?",
    height=150
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_btn = st.button(" Generate Game Code & Run")

if analyze_btn:
    if user_input.strip() == "":
        st.warning(" Please enter a game name before proceeding.")
    else:
        with st.spinner("🔍 Our AI agents are working..."):
            try:
                progress_container = st.container()
                progress_bar = progress_container.progress(0)
                status_text = progress_container.empty()

                # Step 1: Write Game Code
                progress_bar.progress(33)
                status_text.markdown(f"#### 📝 Writing {user_input} game code to file...")
                code_write_output = write_game(user_input)

                with st.expander("📄 **Code Writing Output**", expanded=True):
                    st.success(f" {user_input} game code written successfully")
                    st.markdown(f"<pre>{code_write_output}</pre>", unsafe_allow_html=True)

                # Step 2: Run Game
                progress_bar.progress(66)
                status_text.markdown(f"#### 🕹 Running {user_input} game from saved file...")
                run_game_output = run_game("game.py")

                with st.expander(" **Game Run Output**", expanded=True):
                    st.success(f" {user_input} game executed successfully")
                    st.markdown(f"<pre>{run_game_output}</pre>", unsafe_allow_html=True)

                progress_bar.progress(100)
                status_text.empty()
                st.success(" Process Completed Successfully!")

            except Exception as e:
                st.error(f"###  Process Failed\nError: {str(e)}\nPlease try again later or contact support.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <p>© 2025 AI Game Code Assistant</p>
    <div style='display: flex; justify-content: center; gap: 15px;'>
        <a href='#' style='color: gray; text-decoration: none;'>Terms</a>
        <a href='#' style='color: gray; text-decoration: none;'>Privacy</a>
        <a href='#' style='color: gray; text-decoration: none;'>Docs</a>
    </div>
</div>
""", unsafe_allow_html=True)
