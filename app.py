import streamlit as st
import google.generativeai as genai

# 1. API KEY SETUP
# Yahan apni copy ki hui key paste karna ' ' ke beech mein
GOOGLE_API_KEY = "AIzaSyCCfn6tBRCJtcKbUYe5LgYgwRFs-aunuxw"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# 2. Page Config & Professional Branding
st.set_page_config(page_title="GlobalScript AI Pro", page_icon="🤖")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #FF0000;'>🤖 GlobalScript AI Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Professional Video Scripts & SEO Strategy</p>", unsafe_allow_html=True)

# 3. Sidebar Configuration
st.sidebar.title("🌐 Engine Settings")
lang_map = {
    "English": "en", "Hindi": "hi", "Punjabi": "pa", "Spanish": "es", "Arabic": "ar"
}
selected_lang = st.sidebar.selectbox("Output Language", list(lang_map.keys()))
st.sidebar.write("---")
st.sidebar.info("AI Engine: Google Gemini Pro (Active 🟢)")

# 4. User Input
topic = st.text_input("Enter Video Topic:", placeholder="e.g. How to grow on YouTube in 2026")

if st.button("Generate Viral Script ✨"):
    if topic:
        with st.spinner("AI is thinking and writing..."):
            try:
                # Prompt for the AI
                prompt = f"Write a professional YouTube video script and SEO tags for the topic: '{topic}' in {selected_lang} language. Include a catchy title, introduction, main points, and viral tags."
                
                response = model.generate_content(prompt)
                
                st.success("Your Content is Ready!")
                st.markdown("---")
                st.write(response.text)
                
                # Copy Button (Instruction)
                st.info("Tip: You can select and copy the text above.")
            except Exception as e:
                st.error("Engine Error. Please check your API Key.")
    else:
        st.warning("Please enter a topic.")

# 5. Admin Info (Hidden)
with st.sidebar.expander("System Info"):
    st.caption("Version 2.1 Global")
    st.caption("Developed for High Performance")
