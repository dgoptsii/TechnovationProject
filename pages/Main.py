import streamlit as st 
import GameRules 
import Game
import AboutUs 
import Partners
import LearningMaterials
import utils


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
utils.load_css("style.css")
page.app()