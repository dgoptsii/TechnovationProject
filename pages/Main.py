import streamlit as st 
import GameRules 
import Game
import AboutUs
import pages.PublicOrganizations as PublicOrganizations
import LearningMaterials
import utils


#dictionary (key, value)
PAGES = {
    "Правила гри": GameRules,
    "Про проект": AboutUs,
    "Гра": Game, 
    "Начальні матеріали": LearningMaterials, 
    "Партнери": PublicOrganizations
}

st.sidebar.title('Меню')
selection = st.sidebar.radio("Перейти на", list(PAGES.keys()))

page = PAGES[selection]
utils.load_css("style.css")
page.app()