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
                "The game consists of static gestures of the Ukrainian sign language. You sequentially show letters with pauses. Choose difficulty at the start.<br>",
                "To have your answer counted, hold your hand in the same position for 5 seconds.<br>",
                "Letters like: Ґ, Д, З, Ї, Й, К, Ц, Щ, Ь are missing because they are not static.<br>",
                "For each wrong answer, the flower loses a petal. If the flower loses all petals, the game is over.<br>",
                "When a word is guessed, it is displayed along with a winner's congratulations.<br>",
                "The game is only available in Ukrainian."
            ]
        }
    }

    lang = st.session_state.language

    # Заголовок
    st.markdown(f'<div class="title_header">{texts[lang]["title"]}</div>', unsafe_allow_html=True)

    # Показ правил гри
    for idx, rule in enumerate(texts[lang]['rules']):
        st.markdown(f'<div class="text">{rule}</div>', unsafe_allow_html=True)

        # Перше зображення — по центру
        if idx == 0:
            col1, col2, col3 = st.columns([1, 2, 1])  # Перша колонка — порожня, друга — для зображення
            with col1:
                pass
            with col2:
                svg_path = "images/2.1.svg"
                if os.path.exists(svg_path):
                    st.image(svg_path, width=500)
                else:
                    st.write(f"Не вдалося знайти файл за шляхом: {svg_path}. Поточна директорія: {os.getcwd()}")
            with col3:
                pass

        # Друге і третє зображення — горизонтально, по центру
        if idx == 3:
            col1, col2, col3 = st.columns([1, 2, 1])  # Перша і третя колонка — порожні, друга — для зображень
            with col1:
                pass
            with col2:
                # Два зображення в одній колонці, горизонтально один від одного
                col_left, col_right = st.columns([1, 1])  # Створюємо дві рівні колонки для зображень
                with col_left:
                    svg_path = "images/3.svg"
                    if os.path.exists(svg_path):
                        st.image(svg_path, width=200)
                    else:
                        st.write(f"Не вдалося знайти файл за шляхом: {svg_path}. Поточна директорія: {os.getcwd()}")
                with col_right:
                    svg_path = "images/6.svg"
                    if os.path.exists(svg_path):
                        st.image(svg_path, width=200)
                    else:
                        st.write(f"Не вдалося знайти файл за шляхом: {svg_path}. Поточна директорія: {os.getcwd()}")
            with col3:
                pass

        # Четверте, п'яте і шосте зображення — в три колонки поруч
        if idx == 4:
            col1, col2, col3 = st.columns([1, 1, 1])  # Три рівні колонки для зображень
            with col1:
                svg_path = "images/2.svg"
                if os.path.exists(svg_path):
                    st.image(svg_path, width=200)
                else:
                    st.write(f"Не вдалося знайти файл за шляхом: {svg_path}. Поточна директорія: {os.getcwd()}")
            with col2:
                svg_path = "images/4.svg"
                if os.path.exists(svg_path):
                    st.image(svg_path, width=200)
                else:
                    st.write(f"Не вдалося знайти файл за шляхом: {svg_path}. Поточна директорія: {os.getcwd()}")
            with col3:
                svg_path = "images/5.svg"
                if os.path.exists(svg_path):
                    st.image(svg_path, width=200)
                else:
                    st.write(f"Не вдалося знайти файл за шляхом: {svg_path}. Поточна директорія: {os.getcwd()}")
