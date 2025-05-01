import streamlit as st
import random
import utils


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.keypoint_classifier import recognition




def change_level(level):
    st.session_state.clear()  # Скидає весь session_state
    st.session_state["level"] = level
    if level != "menu":
        reset_game()


def reset_game():
    levels = {
        "easy": (["СОН", "ШУМ", "МАК", "РІК", "НІС", "ШИЯ", "ІКРА","КОШКА", "КОМА" "МОШКА", "СМАК", "КАМІН", "РАКУРС", "РАК", "МІШОК", "СУМ"], 3),
        "medium": (["РАНОК", "БУРЯК", "РОМАН", "ФАРБА", "ШТОРА", "МОСТИ", "РОМАШКА", "ЛІТАК", "ШАРФ", "СУМКА", "ЯНТАР", "КАША", "ТОРБА", "МІШОК", "КАРТКА"], 5),
        "hard": (["АВТОМОБІЛЬ", "ГУМАННІСТ", "АВТОРИТЕТ", "ФАРБУВАННЯ", "АВТОБУС", "ЧАРІВНИК", "БАРОМЕТР", "ФЛЕШКА", "СПАЛАХ", "ІНЖЕНЕР", "ЕЛЕКТРОН", "ПЕЧИВО"], 10)
    }

    words, tries = levels[st.session_state["level"]]
    st.session_state["random_word"] = random.choice(words)
    st.session_state["count"] = tries
    st.session_state["guessed_letters"] = []
    st.session_state["not_guessed_letters"] = []
    st.session_state["recognized_letter"] = ""
    st.session_state["game_won"] = False
    st.session_state["display_word"] = " ".join(["_" for _ in st.session_state["random_word"]])


def set_placeholders():
    col1, col2 = st.columns(2)
    with col1:
        if "gesture_placeholder" not in st.session_state:
            st.session_state.gesture_placeholder = st.empty()
        if "guessed_placeholder" not in st.session_state:
            st.session_state.guessed_placeholder = st.empty()
    with col2:
        if "word_placeholder" not in st.session_state:
            st.session_state.word_placeholder = st.empty()
        if "not_guessed_placeholder" not in st.session_state:
            st.session_state.not_guessed_placeholder = st.empty()
       


def app():
    utils.load_css("style.css")

    # Застосовуємо білий фон тільки для цієї сторінки
    st.markdown("""
        <style>
        .stApp {
            background-color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    if "level" not in st.session_state:
        st.session_state.level = "menu"

    if st.session_state.level == "menu":
        st.markdown('<div class="title_header">Гра</div>', unsafe_allow_html=True)
        st.markdown('<div class="title_subheader">Виберіть рівень:</div>', unsafe_allow_html=True)
        st.session_state.easy = st.button("Легкий", on_click=change_level, args=("easy",), key="easy_button", use_container_width=True)
        st.session_state.medium = st.button("Середній", on_click=change_level, args=("medium",), key="medium_button", use_container_width=True)
        st.session_state.hard = st.button("Складний", on_click=change_level, args=("hard",), key="hard_button", use_container_width=True)
    else:
        st.session_state.easy = st.empty()
        st.session_state.medium = st.empty()
        st.session_state.hard = st.empty()

        level_titles = {
            "easy": ("Легкий рівень",0),
            "medium": ("Середній рівень",1),
            "hard": ("Складний рівень",2)
        }

        image_sets = {
            "easy": [
                "images/1.svg","images/1.svg","images/1.svg"
            ],
            "medium": [
                "https://i.postimg.cc/cJ6PZYYY/5-5.png",
                "https://i.postimg.cc/HWbRpTJS/5-4.png",
                "https://i.postimg.cc/q7tDWrVx/5-3.png",
                "https://i.postimg.cc/DZLjyczW/5-2.png",
                "https://i.postimg.cc/hvnCJ7J2/5-1.png"
            ],
            "hard": [
                "https://i.postimg.cc/m28dDkTS/10-10.png",
                "https://i.postimg.cc/g2jg6pJb/10-9.png",
                "https://i.postimg.cc/Cx2mG2BB/10-8.png",
                "https://i.postimg.cc/xdbgtPMs/10-7.png",
                "https://i.postimg.cc/441PLyHT/10-6.png",
                "https://i.postimg.cc/CxR4x4PF/10-5.png",
                "https://i.postimg.cc/t48NZVwF/10-4.png",
                "https://i.postimg.cc/yx6m4h3C/10-3.png",
                "https://i.postimg.cc/66zVVPFW/10-2.png",
                "https://i.postimg.cc/VLVjpCY2/10-1.png"
            ]
        }

        level = st.session_state.level
        level_name, level_index = level_titles[level]
       
        
        images = image_sets[level]

        st.markdown(f'<div class="title_subheader">{level_name}</div>', unsafe_allow_html=True)

        if "random_word" not in st.session_state:
            reset_game()

        word = st.session_state["random_word"]
        count = st.session_state["count"]

        if "images" not in st.session_state:
            st.session_state.images = images
        col1, col2 = st.columns(2)

        with col1:
            if "image_placeholder" not in st.session_state:
                st.session_state.image_placeholder = st.empty()
        with col2:
            if "video_placeholder" not in st.session_state:
                st.session_state.video_placeholder = st.empty()

        img_index = max(0, min(len(images) - 1, len(images) - count))
        svg_path = images[img_index]
        st.session_state.image_placeholder.image(svg_path, width=300)
                 

        set_placeholders()

        st.button("Назад", on_click=lambda: change_level("menu"), key="back_1button", use_container_width=True)

        st.session_state.gesture_placeholder.markdown(
            f'<div class="text">✋ Жест: {st.session_state.get("recognized_letter", [])}</div>', unsafe_allow_html=True)
        st.session_state.word_placeholder.markdown(
            f'<div class="text">Слово: {st.session_state["display_word"]}</div>', unsafe_allow_html=True)
        st.session_state.guessed_placeholder.markdown(
            f'<div class="text">👍 Вгадані літери: </div>', unsafe_allow_html=True)
        st.session_state.not_guessed_placeholder.markdown(
            f'<div class="text">👎 Невгадані літери: </div>', unsafe_allow_html=True)

        recognition.video_capture()
        images_win = [
                "images/1.svg","images/1.svg","images/1.svg"
            ]
        
        if st.session_state["game_won"]:
            svg_path = images_win[level_index]
            st.session_state.image_placeholder.image(svg_path, width=300)
        else:
            svg_path = "images/1.svg"
            st.session_state.image_placeholder.image(svg_path, width=300)
        
          
