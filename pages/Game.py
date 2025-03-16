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
        st.session_state["random_word"] = random.choice(["СМІЛИВИЙ", "ЧАРІВНИЙ", "ВАЖЛИВИЙ"])  # Слова для середнього рівня
        st.session_state["count"] = 8  # 8 спроб для середнього рівня
    elif st.session_state["level"] == "hard":
        st.session_state["random_word"] = random.choice(["ПРОГРАМУВАННЯ", "МАТЕМАТИКА", "ЕНЕРГІЯ"])
        st.session_state["count"] = 10  # 10 спроб для складного рівня

    st.session_state["guessed_letters"] = []
    st.session_state["current_letter"] = ""

def app(): 
    if "level" not in st.session_state:
        st.session_state["level"] = "menu"

    st.title("Гра")

    if st.session_state["level"] == "menu":
        st.subheader("Виберіть рівень:")
        st.button("Легкий", on_click=change_level, args=("easy",))
        st.button("Середній", on_click=change_level, args=("medium",))
        st.button("Складний", on_click=change_level, args=("hard",))

    elif st.session_state["level"] == "easy":
        st.subheader("Легкий рівень")
        st.write("Ви граєте на легкому рівні!")
        st.title("Гра: Вгадай слово!")

        if "random_word" not in st.session_state:
            reset_game()

        random_word = st.session_state["random_word"]
        count = st.session_state["count"]
        guessed_letters = st.session_state["guessed_letters"]

        image_paths = [
            "https://i.postimg.cc/xjbC1sgp/2025-03-16-150455.png",
            "https://i.postimg.cc/TYwtbDLs/2025-03-16-150621.png",
            "https://i.postimg.cc/9fjPLR0C/2025-03-16-150721.png",
            "https://i.postimg.cc/W35Mp5n1/2025-03-16-150757.png",
            "https://i.postimg.cc/28sn5b4h/2025-03-16-150811.png",
            "https://i.postimg.cc/jjKNzp3j/2025-03-16-150835.png"
        ]

        img_index = max(0, min(5, 5 - count))
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

        display_word = "".join([letter if letter in guessed_letters else "_" for letter in random_word])
        display_word = display_word[0].upper() + display_word[1:].lower()

        if "_" not in display_word:
            st.success(f"🎉 Ви виграли! Слово: {random_word}")
            st.button("Спробувати ще раз", on_click=reset_game)

        elif st.session_state["count"] == 0:
            st.error(f"❌ Ви програли. Загадане слово: {random_word}")
            st.button("Спробувати ще раз", on_click=reset_game)

        st.button("Назад", on_click=change_level, args=("menu",))

    # Рівень "Середній"
    elif st.session_state["level"] == "medium":
        st.subheader("Середній рівень")
        st.write("Ви граєте на середньому рівні!")

        if "random_word" not in st.session_state:
            reset_game()

        random_word = st.session_state["random_word"]
        count = st.session_state["count"]
        guessed_letters = st.session_state["guessed_letters"]

        image_paths = [
            "https://i.postimg.cc/TwTnVzw9/2025-03-16-154207.png",
            "https://i.postimg.cc/vH4ftLQp/2025-03-16-154229.png",
            "https://i.postimg.cc/1zQFSkpQ/2025-03-16-154249.png",
            "https://i.postimg.cc/tJYZDpHh/2025-03-16-154304.png",
            "https://i.postimg.cc/RVGChj5m/2025-03-16-155003.png",
            "https://i.postimg.cc/6Q4BHq76/2025-03-16-155018.png",
            "https://i.postimg.cc/QC4PGgP2/2025-03-16-155036.png",
            "https://i.postimg.cc/QNmZJ16k/2025-03-16-155049.png",
            "https://i.postimg.cc/wB8rpjfj/2025-03-16-155109.png"
        ]

        img_index = max(0, min(8, 8 - count))
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

        display_word = "".join([letter if letter in guessed_letters else "_" for letter in random_word])
        display_word = display_word[0].upper() + display_word[1:].lower()

        if "_" not in display_word:
            st.success(f"🎉 Ви виграли! Слово: {random_word}")
            st.button("Спробувати ще раз", on_click=reset_game)

        elif st.session_state["count"] == 0:
            st.error(f"❌ Ви програли. Загадане слово: {random_word}")
            st.button("Спробувати ще раз", on_click=reset_game)

        st.button("Назад", on_click=change_level, args=("menu",))

    # Рівень "Складний"
    elif st.session_state["level"] == "hard":
        st.subheader("Складний рівень")
        st.write("Ви граєте на складному рівні!")

        # Кнопка "Назад"
        st.button("Назад", on_click=change_level, args=("menu",))