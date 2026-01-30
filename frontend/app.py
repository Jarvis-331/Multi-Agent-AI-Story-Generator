import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/generate"

st.set_page_config(page_title="AI Story Generator", layout="centered")

st.title("🧠 Multi-Agent AI Story Generator")

prompt = st.text_area(
    "Enter your story prompt:",
    placeholder="A dragon in a modern city...",
    height=120
)

if st.button("Generate Story"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Agents are crafting your story..."):
            response = requests.post(
                BACKEND_URL,
                json={"prompt": prompt}
            )

            if response.status_code == 200:
                story = response.json()["story"]
                st.success("Story Generated!")
                st.write(story)
            else:
                st.error("Error generating story.")
