
import streamlit as st
import random

def change_level(level):
    st.session_state["level"] = level  # Змінюємо рівень
    reset_game()  # Очищуємо дані після зміни рівня

def reset_game():
    """Функція для скидання гри (нове слово, 5 спроб, порожній список букв)."""
    if st.session_state["level"] == "easy":
        st.session_state["random_word"] = random.choice(["ДОБРО", "ЛЮБОВ", "ДРУЗІ"])
        st.session_state["count"] = 5
    elif st.session_state["level"] == "medium":
        st.session_state["random_word"] = random.choice(["СМІЛИВИЙ", "ЧАРІВНИЙ", "ВАЖЛИВИЙ"])
        st.session_state["count"] = 8
    elif st.session_state["level"] == "hard":
        st.session_state["random_word"] = random.choice(["ВИПРОБУВАННЯ", "МАТЕМАТИКА", "ЕНЕРГІЯ"])
        st.session_state["count"] = 12  # Збільшено кількість спроб для складного рівня

    st.session_state["guessed_letters"] = []
    st.session_state["current_letter"] = ""

def app(): 
    if "level" not in st.session_state:
        st.session_state["level"] = "menu"

    st.title("Гра")

    st.markdown(
        """<style>
          .stButton>button {
        background-color: #4F9A8C !important; /* Бірюзовий (перезовий) колір кнопки */
        border: 2px solid #4F9A8C !important; /* Початковий контур */
        color: white !important;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #4F9A8C !important; /* Колір кнопки не змінюється */
        border-color: #3A7D72 !important; /* Темніший бірюзовий контур при наведенні */
        color: white !important; 
        
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
            "hard": ("Складний рівень", [
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
            ])
        }

        level_name, image_paths = levels.get(st.session_state["level"], ("", []))
        st.subheader(level_name)

        if "random_word" not in st.session_state:
            reset_game()

        random_word = st.session_state["random_word"]
        count = st.session_state["count"]
        guessed_letters = st.session_state["guessed_letters"]

        img_index = max(0, min(len(image_paths) - 1, len(image_paths) - 1 - count))

        # Центрування зображення з use_container_width
        col1, col2, col3 = st.columns([1, 4, 1])  # Три колонки, центральна велика
        with col2:
            st.image(image_paths[img_index], use_container_width=True)

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
           
        elif st.session_state["count"] == 0:
            st.error(f"❌ Ви програли. Загадане слово: {random_word}")
            st.markdown('<div class="retry-button">', unsafe_allow_html=True)
            
        col1, col2 = st.columns([1, 1])
        with col1:
            st.button("Спробувати ще раз", on_click=reset_game, key="retry_button_col1")
        with col2:
            st.button("Назад", on_click=change_level, args=("menu",), key="back_button")

