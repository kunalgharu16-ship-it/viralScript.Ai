import streamlit as st

# 1. Page Configuration (Browser Tab Name)
st.set_page_config(page_title="ViralScript AI", page_icon="🚀")

# 2. Hide Streamlit Footer (Branding hatao)
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_style, unsafe_allow_html=True)

# 3. Main Interface
st.markdown("<h1 style='text-align: center;'>🚀 ViralScript AI</h1>", unsafe_allow_html=True)
st.write("Professional YouTube scripts and SEO in one click.")

# User Input
topic = st.text_input("Video Topic:", placeholder="e.g. 5 Ways to earn online")
lang = st.selectbox("Language:", ["English", "Hindi", "Punjabi"])

if st.button("Generate Content"):
    if topic:
        st.info(f"Generating strategy for: {topic}...")
        # Baad mein hum yahan AI ka dimaag jodd denge
    else:
        st.error("Please enter a topic.")

# Hidden Settings (Privacy safe)
with st.sidebar.expander("System Info"):
    st.write("Version 1.0 (Stable)")
    st.write("Server: Global Cloud")
