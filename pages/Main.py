import streamlit as st
import GameRules
import Game
import Help
import AboutUs
import PublicOrganizations
import LearningMaterials
import utils
from streamlit_navigation_bar import st_navbar

# Сторінки
PAGES = {
    "Про проект": AboutUs,
    "Правила гри": GameRules,
    "Навчальні матеріали": LearningMaterials, 
    "Гра": Game, 
    "Допомогти проекту": Help, 
    "Громадські організації": PublicOrganizations
}
st.set_page_config(layout="wide")


# Кастомне меню з HTML
page = st_navbar(["GameRules", "Game", "Help", "AboutUs", "PublicOrganizations", "LearningMaterials"])
st.write(page)

# Вибір сторінки
query_params = st.query_params
selection = query_params.get("page", ["Про проект"])[0]

page = PAGES.get(selection, AboutUs)

utils.load_css("style.css")
page.app()