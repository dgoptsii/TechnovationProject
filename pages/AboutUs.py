import streamlit as st
import os
import utils

def app():
    utils.load_css("style.css")  # Завантаження стилів

    # Сесійний стан для мови
    if 'language' not in st.session_state:
        st.session_state.language = 'uk'

    # Кнопки вибору мови в правому верхньому куті з відступом
    col1, col2, col3, col4 = st.columns([6, 1, 0.5, 1])  # Додав проміжок 0.5 між кнопками
    with col2:
        if st.button("Українська"):
            st.session_state.language = 'uk'
    with col4:
        if st.button("English"):
            st.session_state.language = 'en'

    # Тексти на двох мовах
    texts = {
        'uk': {
            'about_us': "Про нас",
            'about_text': ("Ми - група підлітків, які є учасниками міжнародного проекту \"Technovation Girls\". <br><br>"
                           "Ми довго думали над темою нашого проєкту, проте врешті-решт зупинилися на інклюзії. "
                           "Нашою мрією стало допомагати дітям з вадами слуху вливатися в сучасне суспільство і не відчувати себе зайвими, "
                           "допомагати їм рухатися далі. "
                           "Із часом зародилася ідея створення доступної і сучасної гри, яка є інструментом для навчання жестової мови, яка об'єднувала б людей з різних культур та середовищ."),
            'mission': "Місія 🎯",
            'mission_text': "Сприяти розвитку інклюзивного суспільства, де кожен має голос.",
            'vision': "Візія 👓",
            'vision_text': ("Світ, у якому мовне різноманіття сприймається як сила, а кожна людина — незалежно від її здатності чути — "
                            "має рівний доступ до спілкування, освіти й можливостей."),
            'goal': "Мета 🌍",
            'goal_text': ("Сприяти побудові інклюзивного суспільства, де жестова мова є природною частиною взаємодії, "
                          "а технології стають засобом рівності, підтримки та взаєморозуміння.")
        },
        'en': {
            'about_us': "About Us",
            'about_text': ("We are a group of teenagers participating in the international project \"Technovation Girls\". <br><br>"
                           "We spent a lot of time choosing a topic for our project and eventually decided on inclusion. "
                           "Our dream is to help children with hearing impairments integrate into modern society and not feel isolated, "
                           "help them move forward. "
                           "Over time, the idea of creating an accessible and modern game emerged, which would serve as a tool for learning sign language, "
                           "bringing together people from different cultures and backgrounds."),
            'mission': "Mission 🎯",
            'mission_text': "To promote the development of an inclusive society where everyone has a voice.",
            'vision': "Vision 👓",
            'vision_text': ("A world where linguistic diversity is embraced as a strength, and every person — regardless of their ability to hear — "
                            "has equal access to communication, education, and opportunities."),
            'goal': "Goal 🌍",
            'goal_text': ("To help build an inclusive society where sign language is a natural part of interaction, "
                          "and technology becomes a means of equality, support, and understanding.")
        }
    }

    lang = st.session_state.language

    # Перевірка шляху до файлу
    svg_path = "images/1.svg"  # Оновлений шлях до файлу
    if os.path.exists(svg_path):
        st.image(svg_path, width=200)  # Відображення SVG
    else:
        st.write(f"Не вдалося знайти файл за шляхом: {svg_path}. Поточна директорія: {os.getcwd()}")

    # Заголовки і тексти в залежності від мови
    st.markdown(f'<div class="title_header">{texts[lang]["about_us"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{texts[lang]["about_text"]}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="title_subheader">{texts[lang]["mission"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{texts[lang]["mission_text"]}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="title_subheader">{texts[lang]["vision"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{texts[lang]["vision_text"]}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="title_subheader">{texts[lang]["goal"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{texts[lang]["goal_text"]}</div>', unsafe_allow_html=True)
