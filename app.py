import streamlit as st
from agents.interest_mapper import map_interests
from agents.career_recommender import recommend_careers
from agents.roadmap_generator import generate_roadmap
from dotenv import load_dotenv


load_dotenv("api.env")


st.set_page_config(
    page_title="🎯 CareerGPT Pro", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
    <style>
        :root {
            --primary: #6f42c1;
            --primary-dark: #5a32a3;
            --secondary: #00c4cc;
            --dark-bg: #0f172a;
            --darker-bg: #0b1120;
            --card-bg: #1e293b;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --success: #10b981;
            --warning: #f59e0b;
            --error: #ef4444;
            --font-main: 'Inter', sans-serif;
        }
        
        body {
            background-color: var(--dark-bg);
            color: var(--text-primary);
            font-family: var(--font-main);
        }
        
        .stApp {
            background: linear-gradient(to bottom, var(--darker-bg), var(--dark-bg));
        }
        
        /* Input fields */
        .stTextArea>div>div>textarea {
            background-color: var(--card-bg) !important;
            color: var(--text-primary) !important;
            border: 1px solid #334155 !important;
            border-radius: 8px !important;
            padding: 12px !important;
        }
        
        /* Buttons */
        .stButton>button {
            background: linear-gradient(to right, var(--primary), var(--primary-dark)) !important;
            color: white !important;
            border: none !important;
            padding: 12px 24px !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            transition: all 0.3s !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15) !important;
        }
        
        /* Sidebar */
        [data-testid="stSidebar"] {
            background: linear-gradient(to bottom, var(--darker-bg), var(--dark-bg)) !important;
            border-right: 1px solid #1e293b !important;
        }
        
        /* Cards */
        .st-expander {
            background-color: var(--card-bg) !important;
            border: 1px solid #334155 !important;
            border-radius: 10px !important;
        }
        
        /* Progress bar */
        .stProgress>div>div>div {
            background: linear-gradient(to right, var(--primary), var(--secondary)) !important;
        }
        
        /* Markdown text */
        .stMarkdown {
            color: var(--text-primary) !important;
        }
        
        /* Success/Warning/Error boxes */
        .stAlert {
            border-radius: 8px !important;
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: var(--darker-bg);
        }
        ::-webkit-scrollbar-thumb {
            background: var(--primary);
            border-radius: 4px;
        }
    </style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.markdown("""
    <div style='margin-top: -20px; margin-bottom: 30px;'>
        <p style='color: var(--text-secondary); font-size: 14px;'>
        AI-Powered By CAMEL-AI and Groq
        </p>
    </div>
    """, unsafe_allow_html=True)

    
    
    st.markdown("### 🧭 Navigation")
    st.markdown("""
    - **Home**
    - **Career Assessment**
    - **Roadmap Generator**
    - **Saved Profiles**
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 How It Works")
    st.markdown("""
    1. Describe your skills/interests
    2. AI analyzes your profile
    3. Get career matches
    4. Receive personalized roadmap
    """)
    
    st.markdown("---")
    
    st.markdown("### 📬 Contact Support")
    st.markdown("""
    <p style='color: var(--text-secondary);'>
    Having issues?<br>
    Email: <span style='color: var(--secondary);'>tushar80rt@gmail.com</span>
    </p>
    """, unsafe_allow_html=True)


col1, col2 = st.columns([1, 3])
with col1:
    
 with col2:
    st.title("⚡SuccessTrack GPT")

st.markdown("---")

st.markdown("Tell Us About Yourself")
user_input = st.text_area(
    "",
    placeholder="• Describe your skills, interests, and experience\n• Mention your education background\n• Share your career aspirations\n• Or paste your resume text here...",
    height=180,
    help="Be as detailed as possible for better recommendations"
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    analyze_btn = st.button(
        "🚀 Analyze My Profile & Generate Roadmap", 
        use_container_width=True,
        type="primary"
    )

if analyze_btn:
    if not user_input.strip():
        st.warning("Please enter some details about yourself to proceed")
    else:
        with st.spinner("🔍 Our AI agents are analyzing your profile..."):
            try:
                progress_container = st.container()
                progress_bar = progress_container.progress(0)
                status_text = progress_container.empty()
                
                progress_bar.progress(25)
                status_text.markdown("#### 🔮 Identifying your key interests and skills...")
                interests = map_interests(user_input)
                
                with st.expander("🎯 **Your Profile Analysis**", expanded=True):
                    st.success("✅ Successfully identified your core competencies")
                    st.markdown(f"""
                    <div style='background-color: var(--card-bg); padding: 20px; border-radius: 10px;'>
                        {interests}
                    </div>
                    """, unsafe_allow_html=True)
                
                progress_bar.progress(50)
                status_text.markdown("#### 💼 Finding best career matches for you...")
                careers = recommend_careers(interests)
                
                with st.expander("🌟 **Recommended Career Paths**", expanded=True):
                    st.success("✅ Discovered career options matching your profile")
                    st.markdown(f"""
                    <div style='background-color: var(--card-bg); padding: 20px; border-radius: 10px;'>
                        {careers}
                    </div>
                    """, unsafe_allow_html=True)
                
                progress_bar.progress(75)
                status_text.markdown("#### 🛣 Building your personalized roadmap...")
                roadmap = generate_roadmap(careers)
                
                with st.expander("🗺 **Your Career Roadmap**", expanded=True):
                    st.success("✅ Personalized roadmap generated successfully")
                    st.markdown(f"""
                    <div style='background-color: var(--card-bg); padding: 20px; border-radius: 10px;'>
                        {roadmap}
                    </div>
                    """, unsafe_allow_html=True)
                
                progress_bar.progress(100)
                status_text.empty()
                
                st.success("""
                ### 🎉 Analysis Complete!
                You can now:
                - Explore detailed roadmaps
                """)
                
            except Exception as e:
                st.error(f"""
                ### ❌ Analysis Failed
                We encountered an error processing your request:
                
{str(e)}

                Please try again later or contact support.
                """)

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: var(--text-secondary); padding: 20px;'>
    <p>© 2025 CareerGPT Pro | AI Career Assistant</p>
    <div style='display: flex; justify-content: center; gap: 15px; margin-top: 10px;'>
        <a href='#' style='color: var(--secondary); text-decoration: none;'>Terms</a>
        <a href='#' style='color: var(--secondary); text-decoration: none;'>Privacy</a>
        <a href='#' style='color: var(--secondary); text-decoration: none;'>Docs</a>
    </div>
</div>
""", unsafe_allow_html=True)

































