import streamlit as st 
import GameRules 
import Game
import AboutUs 
import Partners
import LearningMaterials

def load_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#dictionary (key, value)
PAGES = {
    "Правила гри": GameRules,
    "Про нас": AboutUs,
    "Гра": Game, 
    "Начальні матеріали": LearningMaterials, 
    "Партнери": Partners 
}

st.sidebar.title('My Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
load_css("style.css")
page.app()