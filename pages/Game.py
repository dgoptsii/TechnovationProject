import streamlit as st
import random

def change_level(level):
    st.session_state["level"] = level  # Змінюємо рівень

def reset_game():
    """Функція для скидання гри (нове слово, 5 спроб, порожній список букв)."""
    if st.session_state["level"] == "easy":
        st.session_state["random_word"] = random.choice(["ДОБРО", "ЛЮБОВ", "ДРУЗІ"])
        st.session_state["count"] = 5
    elif st.session_state["level"] == "medium":
        st.session_state["random_word"] = random.choice(["СМІЛИВИЙ", "ЧАРІВНИЙ", "ВАЖЛИВИЙ"])
        st.session_state["count"] = 8
    elif st.session_state["level"] == "hard":
        st.session_state["random_word"] = random.choice(["ПРОГРАМУВАННЯ", "МАТЕМАТИКА", "ЕНЕРГІЯ"])
        st.session_state["count"] = 10

    st.session_state["guessed_letters"] = []
    st.session_state["current_letter"] = ""

def app(): 
    if "level" not in st.session_state:
        st.session_state["level"] = "menu"

    st.title("Гра")

    st.markdown(
        """<style>
        .stButton>button {
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #4F9A8C !important;  /* Світло-бірюзовий фон при наведенні */
            color: white !important;
        }
        .back-button button, .retry-button button, .level-button button {
            background-color: #FFFFFF !important;
            border: 8px solid #4F9A8C !important; /* Світло-бірюзовий бордер */
            color: #4F9A8C !important;  /* Текст світло-бірюзовий */
        }
        .back-button button:hover, .retry-button button:hover, .level-button button:hover {
            background-color: #4F9A8C !important;
            color: white !important;  /* Білий текст при наведенні */
        }
        .button-container {
            display: flex;
            justify-content: space-between;
        }
        </style>""",
        unsafe_allow_html=True
    )

    if st.session_state["level"] == "menu":
        st.subheader("Виберіть рівень:")
        st.button("Легкий", on_click=change_level, args=("easy",), key="easy_button", use_container_width=True)
        st.button("Середній", on_click=change_level, args=("medium",), key="medium_button", use_container_width=True)
        st.button("Складний", on_click=change_level, args=("hard",), key="hard_button", use_container_width=True)

    else:
        levels = {
            "easy": ("Легкий рівень", [
                "https://i.postimg.cc/xjbC1sgp/2025-03-16-150455.png",
                "https://i.postimg.cc/TYwtbDLs/2025-03-16-150621.png",
                "https://i.postimg.cc/9fjPLR0C/2025-03-16-150721.png",
                "https://i.postimg.cc/W35Mp5n1/2025-03-16-150757.png",
                "https://i.postimg.cc/28sn5b4h/2025-03-16-150811.png",
                "https://i.postimg.cc/jjKNzp3j/2025-03-16-150835.png"
            ]),
            "medium": ("Середній рівень", [
                "https://i.postimg.cc/TwTnVzw9/2025-03-16-154207.png",
                "https://i.postimg.cc/vH4ftLQp/2025-03-16-154229.png",
                "https://i.postimg.cc/1zQFSkpQ/2025-03-16-154249.png",
                "https://i.postimg.cc/tJYZDpHh/2025-03-16-154304.png",
                "https://i.postimg.cc/RVGChj5m/2025-03-16-155003.png",
                "https://i.postimg.cc/6Q4BHq76/2025-03-16-155018.png",
                "https://i.postimg.cc/QC4PGgP2/2025-03-16-155036.png",
                "https://i.postimg.cc/QNmZJ16k/2025-03-16-155049.png",
                "https://i.postimg.cc/wB8rpjfj/2025-03-16-155109.png"
            ]),
        }

        level_name, image_paths = levels.get(st.session_state["level"], ("", []))
        st.subheader(level_name)

        if "random_word" not in st.session_state:
            reset_game()

        random_word = st.session_state["random_word"]
        count = st.session_state["count"]
        guessed_letters = st.session_state["guessed_letters"]

        img_index = max(0, min(len(image_paths) - 1, len(image_paths) - 1 - count))
        st.image(image_paths[img_index])

        display_word = "".join([letter if letter in guessed_letters else "_" for letter in random_word])
        display_word = display_word[0].upper() + display_word[1:].lower()
        st.subheader(f"Слово: {display_word}")

        def process_letter():
            letter = st.session_state["current_letter"].upper()
            if letter and letter not in guessed_letters and letter.isalpha():
                if letter in random_word:
                    guessed_letters.append(letter)
                    st.session_state["guessed_letters"] = guessed_letters
                else:
                    st.session_state["count"] -= 1
            st.session_state["current_letter"] = ""

        st.text_input("Введіть букву:", key="current_letter", max_chars=1, on_change=process_letter)

        if "_" not in display_word:
            st.success(f"🎉 Ви виграли! Слово: {random_word}")
            st.markdown('<div class="retry-button">', unsafe_allow_html=True)
            st.button("Спробувати ще раз", on_click=reset_game)
            st.markdown('</div>', unsafe_allow_html=True)

        elif st.session_state["count"] == 0:
            st.error(f"❌ Ви програли. Загадане слово: {random_word}")
            st.markdown('<div class="retry-button">', unsafe_allow_html=True)
            st.button("Спробувати ще раз", on_click=reset_game)
            st.markdown('</div>', unsafe_allow_html=True)

        # Використовуємо 2 колонки для кнопок "Назад" і "Спробувати ще раз"
        col1, col2 = st.columns([1, 1])  # 2 рівні колонки

        with col2:  # Кнопка "Назад" з правого боку
            st.markdown('<div class="back-button">', unsafe_allow_html=True)
            st.button("Назад", on_click=change_level, args=("menu",))
            st.markdown('</div>', unsafe_allow_html=True)

        with col1:  # Кнопка "Спробувати ще раз" з лівого боку
            st.markdown('<div class="retry-button">', unsafe_allow_html=True)
            st.button("Спробувати ще раз", on_click=reset_game)
            st.markdown('</div>', unsafe_allow_html=True)