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
        "easy": (["ВІР", "ПАР", "ПІТ"], 3),
        "medium": (["ПРАВО", "ВІРНА", "РІВНО"], 5),
        "hard": (["ПЛАНУВАННЯ", "ПРИВІТАННЯ", "УПРАВЛІННЯ"], 10)
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
    if "level" not in st.session_state:
        st.session_state.level = "menu"

    if st.session_state.level == "menu":
        st.markdown('<div class="title_header">Гра</div>', unsafe_allow_html=True)
        st.markdown('<div class="title_subheader">Виберіть рівень:</div>', unsafe_allow_html=True)
        st.session_state.easy= st.button("Легкий", on_click=change_level, args=("easy",), key="easy_button", use_container_width=True)
        st.session_state.medium= st.button("Середній", on_click=change_level, args=("medium",), key="medium_button", use_container_width=True)
        st.session_state.hard= st.button("Складний", on_click=change_level, args=("hard",), key="hard_button", use_container_width=True)
    else:
        st.session_state.easy = st.empty()  
        st.session_state.medium = st.empty()
        st.session_state.hard = st.empty()
        
        level_titles = {
            "easy": "Легкий рівень",
            "medium": "Середній рівень",
            "hard": "Складний рівень"
        }

        image_sets = {
            "easy": [
                "https://i.postimg.cc/xjbC1sgp/2025-03-16-150455.png",
                "https://i.postimg.cc/TYwtbDLs/2025-03-16-150621.png",
                "https://i.postimg.cc/9fjPLR0C/2025-03-16-150721.png",
                "https://i.postimg.cc/W35Mp5n1/2025-03-16-150757.png",
                "https://i.postimg.cc/28sn5b4h/2025-03-16-150811.png",
                "https://i.postimg.cc/jjKNzp3j/2025-03-16-150835.png"
            ],
            "medium": [
                "https://i.postimg.cc/TwTnVzw9/2025-03-16-154207.png",
                "https://i.postimg.cc/vH4ftLQp/2025-03-16-154229.png",
                "https://i.postimg.cc/1zQFSkpQ/2025-03-16-154249.png",
                "https://i.postimg.cc/tJYZDpHh/2025-03-16-154304.png",
                "https://i.postimg.cc/RVGChj5m/2025-03-16-155003.png",
                "https://i.postimg.cc/6Q4BHq76/2025-03-16-155018.png",
                "https://i.postimg.cc/QC4PGgP2/2025-03-16-155036.png",
                "https://i.postimg.cc/QNmZJ16k/2025-03-16-155049.png",
                "https://i.postimg.cc/wB8rpjfj/2025-03-16-155109.png"
            ],
            "hard": [
                "https://i.postimg.cc/mDb2LmBm/2025-03-18-203502.png",
                "https://i.postimg.cc/sfT9R8s0/2025-03-18-203545.png",
                "https://i.postimg.cc/mr3Cppmj/2025-03-18-204922.png",
                "https://i.postimg.cc/28qvNSHV/2025-03-18-205023.png",
                "https://i.postimg.cc/hvQG6fSn/2025-03-18-205134.png",
                "https://i.postimg.cc/Xv6DyhZk/2025-03-18-205259.png",
                "https://i.postimg.cc/nLMYrG2G/2025-03-18-205352.png",
                "https://i.postimg.cc/MKNzgW4Z/2025-03-18-205441.png",
                "https://i.postimg.cc/43KLqgDG/2025-03-18-205540.png",
                "https://i.postimg.cc/fRQYDhSZ/2025-03-18-205823.png",
                "https://i.postimg.cc/xCZtPFxC/2025-03-18-210035.png",
                "https://i.postimg.cc/B652jYrk/2025-03-18-210123.png",
                "https://i.postimg.cc/k5mZ64D5/2025-03-18-210539.png",
                "https://i.postimg.cc/44D1N0Yf/2025-03-18-210322.png"
            ]
        }

        level = st.session_state.level
        level_name = level_titles[level]
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

        st.session_state.image_placeholder.markdown(
                f'<div><img src="{images[img_index]}" height="300"></div>',
                 unsafe_allow_html=True
                )


        set_placeholders()

        st.button("Назад", on_click=lambda: change_level("menu"), key="back_1button", use_container_width=True)
       
        st.session_state.gesture_placeholder.markdown(f'<div class="text">✋ Жест: {st.session_state.get("recognized_letter", [])}</div>', unsafe_allow_html=True)
        st.session_state.word_placeholder.markdown(f'<div class="text">Слово: {st.session_state["display_word"]}</div>', unsafe_allow_html=True)
        st.session_state.guessed_placeholder.markdown(f'<div class="text">👍 Вгадані літери: </div>', unsafe_allow_html=True)
        st.session_state.not_guessed_placeholder.markdown(f'<div class="text">👎 Невгадані літери: </div>', unsafe_allow_html=True)

        recognition.video_capture()
        
        
        if st.session_state["game_won"]==True:
            st.session_state.image_placeholder.markdown(
                f'<div style="display: flex; justify-content: center;"><img src="" width="200"></div>',
                 unsafe_allow_html=True
                )
        else:
             st.session_state.image_placeholder.markdown(
                f'<div style="display: flex; justify-content: center;"><img src="" width="200"></div>',
                 unsafe_allow_html=True
                )
        
