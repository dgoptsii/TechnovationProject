
import streamlit as st
import random

def app():
    st.title("Гра: Вгадай слово!")

    # Список слів для гри
    words = ["ДОБРО", "ЛЮБОВ", "ДРУЗІ"]

    # Зберігаємо випадкове слово в session_state
    if "random_word" not in st.session_state:
        st.session_state["random_word"] = random.choice(words)

    random_word = st.session_state["random_word"]

    # Ініціалізація session_state для спроб і відгаданих букв
    if "count" not in st.session_state:
        st.session_state["count"] = 5
    if "guessed_letters" not in st.session_state:
        st.session_state["guessed_letters"] = []
    if "current_letter" not in st.session_state:
        st.session_state["current_letter"] = ""

    count = st.session_state["count"]
    guessed_letters = st.session_state["guessed_letters"]

    # Завантажуємо зображення
    image_paths = [
        "https://i.postimg.cc/QN7GYxrM/2025-03-08-201156.png",
        "https://i.postimg.cc/QCcC1v85/photo-2025-03-08-20-13-40.jpg",
        "https://i.postimg.cc/CLdDptmd/2025-03-08-201338.png",
        "https://i.postimg.cc/TYXpf20c/photo-2025-03-08-20-13-46.jpg",
        "https://i.postimg.cc/SQn8w3ZR/2025-03-08-201424.png",
        "https://i.postimg.cc/PrzNxGFn/photo-2025-03-08-20-13-52.jpg"
    ]

    # Переконаємось, що не виходимо за межі списку зображень
    img_index = max(0, min(5, 5 - count))
    st.image(image_paths[img_index])

    # Відображаємо поточний стан слова (відгадані букви або "_")
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in random_word])
    
    # Перша буква заглавная, остальные маленькие
    display_word = display_word[0].upper() + display_word[1:].lower()

    st.subheader(f"Слово: {display_word}")

    # Функция для обработки ввода буквы
    def process_letter():
        letter = st.session_state["current_letter"].upper()

        if letter and letter not in guessed_letters and letter.isalpha():
            if letter in random_word:
                guessed_letters.append(letter)
                st.session_state["guessed_letters"] = guessed_letters
            else:
                st.session_state["count"] -= 1

        # Очищаем поле ввода
        st.session_state["current_letter"] = ""

    # Поле для ввода буквы (автообновление после ввода)
    st.text_input("Введіть букву:", key="current_letter", max_chars=1, on_change=process_letter)

    # Обновляем display_word после каждого ввода буквы
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in random_word])

    # Первая буква заглавная, остальные маленькие
    display_word = display_word[0].upper() + display_word[1:].lower()

    # Перевірка на виграш або поразку
    if "_" not in display_word:
        st.success(f"🎉 Ви виграли! Слово: {random_word}")
        st.button("🔄 Грати знову", on_click=lambda: st.session_state.clear())  # Сброс состояния
    elif st.session_state["count"] == 0:
        st.error(f"❌ Ви програли. Загадане слово: {random_word}")
        st.button("🔄 Спробувати ще раз", on_click=lambda: st.session_state.clear())  # Сброс состояния