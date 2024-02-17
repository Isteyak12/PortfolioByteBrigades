from pathlib import Path
from PIL import Image
import streamlit as st

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic = "parin.jpg"
# https://sdbncode.github.io/SdbnCode/

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Parin"
NAME = "Parin"
DESCRIPTION = """
Hello! I am a recent computer science graduate passionate about technology and eager to kick-start my career in the field. Despite having no prior professional experience, 
                I have honed my skills in various programming languages, including HTML, CSS, JavaScript, Python, Java, and C. My academic journey has equipped me with a solid foundation in 
                computer science principles and a hands-on approach to problem-solving. During my time in school, I actively engaged in creating practical projects that showcase my abilities.
                I'm enthusiastic about connecting with like-minded professionals, sharing insights, and exploring opportunities in the vast realm of computer science. If you're passionate about technology, 
                software development, or just a good conversation, let's connect and explore the possibilities!"""
Profession="Software Dev | Full Stack Dev"
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
