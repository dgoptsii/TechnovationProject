import streamlit as st
import os
import utils

def app():
    utils.load_css("style.css")

    # Сесійний стан для мови
    if 'language' not in st.session_state:
        st.session_state.language = 'uk'

    # Сесійний стан для мови
    if 'language' not in st.session_state:
        st.session_state.language = 'uk'

    # Кнопки вибору мови по центру
    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

    col_empty, col1, col2, col_empty2 = st.columns([2, 1, 1, 2])
    with col1:
        if st.button("Українська", use_container_width=True, key="ua_btn_about_final"):
            st.session_state.language = 'uk'
    with col2:
        if st.button("English", use_container_width=True, key="en_btn_about_final"):
            st.session_state.language = 'en'

    # Стилі для красивих кнопок

    # Тексти правил на двох мовах
    texts = {
        'uk': {
            'title': "Правила гри",
            'rules': [
                "Спочатку обирається рівень складності. Гра побудована на жестах алфавіту української мови: літери демонструються по черзі з паузами.<br>",
                "На кожному рівні з’являється вікно з камерою, в якому ви виконуватимете жести, а система розпізнаватиме їх за допомогою скелетної моделі руки.<br>",
                "Всі жести в грі виконуються правою рукою.<br>",
                "Ви можете бачити слово як серію пропусків («_»), що позначають кожну літеру. Це означає, що кожна літера, яку ви ще не вгадали, залишиться у слові у вигляді підкреслення (_).<br>"
                "Для того щоб гра зарахувала вашу відповідь, тримайте руку в одному положенні 5 секунд.<br>"
                "Якщо жест вже був показаний і розпізнаний, він буде позначений як «already captured».<br>",
                "Відсутні такі букви як: Ґ Д З Ї Й К Ц Щ Ь, оскільки вони нестатичні.<br>",
                "Після того як ви вгадали всі літери, слово відображається на екране  та повідомлення з привітанням переможця.<br>"
                "За кожну неправильну відповідь квітка втрачає одну пелюстку. Якщо квітка залишилась без пелюсток, гра програна.<br>",
                "Гра лише українською мовою."
            ]
        },
        'en': {
            'title': "Game Rules",
            'rules': [
                "First, you choose the difficulty level. The game is based on the gestures of the Ukrainian alphabet: letters are shown in turn with pauses.<br>",
                "At each level, a window with a camera appears in which you will perform gestures, and the system will recognize them using a skeletal model of the hand.<br>",
                "All gestures in the game are performed with the right hand.<br>",
                "You can see the word as a series of spaces (“_”) representing each letter. This means that any letter you haven't guessed yet will remain in the word as an underscore (_).<br>",
                "To have your answer counted, hold your hand in the same position for 5 seconds.<br>",
                "After you have guessed all the letters, the word is displayed on the screen and a message congratulating the winner.<br>",
                "Letters like: Ґ, Д, З, Ї, Й, К, Ц, Щ, Ь are missing because they are not static.<br>",
                "For each wrong answer, the flower loses a petal. If the flower loses all petals, the game is over.<br>",
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
                    st.image(svg_path, width=700)
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
                        st.image(svg_path, width=300)
                    else:
                        st.write(f"Не вдалося знайти файл за шляхом: {svg_path}. Поточна директорія: {os.getcwd()}")
                with col_right:
                    svg_path = "images/6.svg"
                    if os.path.exists(svg_path):
                        st.image(svg_path, width=300)
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
