import streamlit as st 
import GameRules 
import Game
import Help
import AboutUs
import PublicOrganizations
import LearningMaterials
import utils


# Словник для меню на українській мові
PAGES_UK = {
    "Про проект": AboutUs,
    "Правила гри": GameRules,
    "Навчальні матеріали": LearningMaterials, 
    "Гра": Game, 
    "Допомогти проекту": Help, 
    "Партнери/ГО": PublicOrganizations
}

# Словник для меню на англійській мові
PAGES_EN = {
    "About the Project": AboutUs,
    "Game Rules": GameRules,
    "Learning Materials": LearningMaterials, 
    "Game": Game, 
    "Support the Project": Help, 
    "Partners/NGOs": PublicOrganizations
}

# Перемикач мови
language = st.sidebar.radio("Виберіть мову / Choose language", ("Українська", "English"))

# Вибір сторінки в залежності від мови
if language == "Українська":
    PAGES = PAGES_UK
else:
    PAGES = PAGES_EN

# Меню
st.sidebar.title('Меню/Menu')
selection = st.sidebar.radio("Перейти на / Go to", list(PAGES.keys()))

# Завантаження вибраної сторінки
page = PAGES[selection]
utils.load_css("style.css")
page.app()