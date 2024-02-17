from pathlib import Path
from PIL import Image
import streamlit as st

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "isteyak_cs_resume.pdf"
profile_pic = "isteyak.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Isteyak"
NAME = "Isteyak "
DESCRIPTION = """
I am a third-year student at the University of Windsor currently pursuing a Bachelor of
Computer Science degree and actively looking for coop opportunities. I have started my 
computer science journey back in 2021 at the highest ranked private university of 
Bangladesh, infamously known as Independent University, Bangladesh, until I transferred 
to University of Windsor for a better hands-on learning experience. As a volunteer in a 
systems administration position, I am currently working for DEFEND, a tech company known
for making technologies that are focused primarily on authentication systems for the safety 
of vulnerable people. Similarly, it has been a great Fall 2023 semester as I was a teaching
assistant for a data structure and algorithms course at the University of Windsor where 
I taught 100+ students how to apply Java in various data structure problems. 
Fun fact: I am a big fan of C++, but my projects are based on Python. Personally, 
I believe I make the best chicken stew, I love listening to R&B and soft rock, and on 
weekends, I enjoy riding my E Scooter at night."""

EMAIL = "isteyak@uwindsor.ca"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/isteyak-409578230/",
    "GitHub": "https://github.com/Isteyak12",

}

PROJECTS = {
    "🏆Github Repos--> ": "https://github.com/Isteyak12?tab=repositoriess",
}

st.set_page_config(page_title=PAGE_TITLE)
st.title("Hello, Friends!")



profile_pic = Image.open(profile_pic)
# --HERO SECTION---
col1, col2= st.columns(2, gap="small")
with col2:
        st.image(profile_pic, width=230)
with col1:
        st.title(NAME)
        st.write(DESCRIPTION)
        # st.download_button(
            # label= "📄 Download Resume",
            # data=PDFbyte,
            # file_name=resume_file.name,
            # mime="application/octet-stream",)
        # st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
# st.write("#")
# cols=st.columns(len(SOCIAL_MEDIA))
# for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#       cols[index].write(f"[{platform}]({link})")
        
        
# ---EXPERIENCE & QUALIFICATIONS ---
