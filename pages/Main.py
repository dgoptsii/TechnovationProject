import streamlit as st
import GameRules
import Game
import Help
import AboutUs
import PublicOrganizations
import LearningMaterials
import utils

# Сторінки
PAGES = {
    "Про проект": AboutUs,
    "Правила гри": GameRules,
    "Навчальні матеріали": LearningMaterials, 
    "Гра": Game, 
    "Допомогти проекту": Help, 
    "Громадські організації": PublicOrganizations
}

# Кастомне меню з HTML
st.markdown("""
    <style>
    .nav-container {
        border-top: 3px solid #345753;  /* Верхняя граница */
        border-bottom: 3px solid #345753;  /* Нижняя граница */
        width: 1200px;  /* Ширина слайдбара (можно настроить) */
        background-color: #3DB387;
        padding: 10px;
    }
    .nav-container a {
        margin-right: 30px;
        color: white;
        font-weight: bold;
        text-decoration: none;
    }
    .nav-container a:hover {
        text-decoration: underline;
    }
    </style>    
    <div class="nav-container">
        <a href="?page=Про проект">Про проект</a>
        <a href="?page=Правила гри">Правила гри</a>
        <a href="?page=Навчальні матеріали">Навчальні матеріали</a>
        <a href="?page=Гра">Гра</a>
        <a href="?page=Допомогти проекту">Допомогти проекту</a>
        <a href="?page=Громадські організації">Громадські організації</a>
    </div>
""", unsafe_allow_html=True)

# Вибір сторінки
query_params = st.query_params
selection = query_params.get("page", ["Про проект"])[0]
page = PAGES.get(selection, AboutUs)

utils.load_css("style.css")
page.app()