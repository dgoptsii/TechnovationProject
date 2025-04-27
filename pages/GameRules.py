import streamlit as st
import os
import utils

def app():
    utils.load_css("style.css")

    # Сесійний стан для мови
    if 'language' not in st.session_state:
        st.session_state.language = 'uk'

    # Кнопки вибору мови в правому верхньому куті з відступом
    col1, col2, col3, col4 = st.columns([6, 1, 0.5, 1])
    with col2:
        if st.button("Українська"):
            st.session_state.language = 'uk'
    with col4:
        if st.button("English"):
            st.session_state.language = 'en'

    # Тексти правил на двох мовах
    texts = {
        'uk': {
            'title': "Правила гри",
            'rules': [
                "Гра складається зі статичних жестів української мови. По черзі ви показуєте літери з перервами. Складність на початку вибираєте.<br>",
                "Для того щоб гра зарахувала вашу відповідь, тримайте руку в одному положенні 5 секунд.<br>",
                "Відсутні такі букви як: Ґ Д З Ї Й К Ц Щ Ь, оскільки вони нестатичні.<br>",
                "За кожну неправильну відповідь квітка втрачає одну пелюстку. Якщо квітка залишилась без пелюсток, гра програна.<br>",
                "Коли слово вгадано відображається вгадане слово і привітання переможця.<br>",
                "Гра лише українською мовою."
            ]
        },
        'en': {
            'title': "Game Rules",
            'rules': [
                "The game consists of static gestures of the Ukrainian sign language. You sequentially show letters with pauses. Choose difficulty at the start
