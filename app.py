import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="ViralScript Global AI", page_icon="🌐")

# 2. Styling for Professional Look
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .main { background-color: #fafafa; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - Global Settings
st.sidebar.title("🌍 Global Settings")
# Yahan humne saari major languages ka support de diya hai
lang_map = {
    "English": "en", "Hindi": "hi", "Punjabi": "pa", "Spanish": "es", 
    "French": "fr", "Arabic": "ar", "German": "de", "Japanese": "ja", 
    "Russian": "ru", "Portuguese": "pt", "Bengali": "bn"
}
selected_lang = st.sidebar.selectbox("Select Output Language", list(lang_map.keys()))

# 4. Main UI
st.markdown("<h1 style='text-align: center;'>🌐 ViralScript Global AI</h1>", unsafe_allow_html=True)
st.write(f"Currently creating content in: **{selected_lang}**")

topic = st.text_input("Enter Video Topic:", placeholder="e.g. Best places to visit in 2026")

if st.button("Generate Viral Script ✨"):
    if topic:
        st.success(f"Processing '{topic}' for our global audience...")
        st.info(f"Target Language: {selected_lang} ({lang_map[selected_lang]})")
        # Next step: AI Integration will use this lang_map code
    else:
        st.error("Please enter a topic first.")

# 5. Professional Footer (Hidden Settings)
with st.expander("System Logs"):
    st.caption("Engine: Multilingual Neural Network")
    st.caption("Region: Global")
