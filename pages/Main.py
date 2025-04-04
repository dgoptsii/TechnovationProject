import streamlit as st 
import GameRules 
import Game
import AboutUs
import PublicOrganizations
import LearningMaterials
import utils


#dictionary (key, value)
PAGES = {
    "Про проект": AboutUs,
    "Правила гри": GameRules,
    "Гра": Game, 
    "Начальні матеріали": LearningMaterials, 
    "Громадські організації": PublicOrganizations
}

st.sidebar.title('Меню')
selection = st.sidebar.radio("Перейти на", list(PAGES.keys()))

page = PAGES[selection]
utils.load_css("style.css")
page.app()