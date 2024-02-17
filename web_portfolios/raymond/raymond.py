from pathlib import Path
from PIL import Image
import streamlit as st

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic = "raymond.jpg"
# https://sdbncode.github.io/SdbnCode/

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Raymond"
NAME = "Raymond Zeng"
DESCRIPTION = """
I am a computer science student based in Toronto with a passion for web development"""
Profession="Aspiring Web Developer"
EMAIL = "isteyak@uwindsor.ca"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/isteyak-409578230/",
    "GitHub": "https://github.com/SdbnCode",

}


st.set_page_config(page_title=PAGE_TITLE)
# st.title("Hello, Friends!")

profile_pic = Image.open(profile_pic)
# --HERO SECTION---
col1, col2= st.columns(2, gap="small")
with col2:
        st.image(profile_pic, width=230)
with col1:
        st.title(NAME)
        st.title(Profession)
        st.write(DESCRIPTION)
