import streamlit as st 
import GameRules 
import Game
import AboutUs
import Partners
import LearningMaterials
import utils

# Dictionary (key, value) у потрібному порядку
PAGES = {
    "Про проект": AboutUs,
    "Правила гри": GameRules,
    "Навчальні матеріали": LearningMaterials, 
    "Гра": Game, 
    "Партнери": Partners
}

st.sidebar.title('Меню')
selection = st.sidebar.radio("Перейти на", list(PAGES.keys())
)
page = PAGES[selection]
utils.load_css("style.css")
page.app()
