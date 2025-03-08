import streamlit as st
import random

# Список слів, який можна змінити
words = ["python", "streamlit", "developer", "machine", "learning"]

# Список зображень для висмикування
hangman_images = [
    "https://upload.wikimedia.org/wikipedia/commons/9/92/Hangman-0.png",  # без помилок
    "https://upload.wikimedia.org/wikipedia/commons/5/5c/Hangman-1.png",  # 1 помилка
    "https://upload.wikimedia.org/wikipedia/commons/4/4b/Hangman-2.png",  # 2 помилки
    "https://upload.wikimedia.org/wikipedia/commons/6/6a/Hangman-3.png",  # 3 помилки
    "https://upload.wikimedia.org/wikipedia/commons/0/03/Hangman-4.png",  # 4 помилки
    "https://upload.wikimedia.org/wikipedia/commons/2/24/Hangman-5.png",  # 5 помилок
    "https://upload.wikimedia.org/wikipedia/commons/4/4d/Hangman-6.png",  # 6 помилок
    "https://upload.wikimedia.org/wikipedia/commons/0/09/Hangman-7.png",  # 7 помилок
    "https://upload.wikimedia.org/wikipedia/commons/0/0c/Hangman-8.png",  # 8 помилок
    "https://upload.wikimedia.org/wikipedia/commons/a/a2/Hangman-9.png",  # 9 помилок
    "https://upload.wikimedia.org/wikipedia/commons/d/d7/Hangman-10.png"  # 10 помилок
]

def start_game():
    # Вибір випадкового слова
    word = random.choice(words)
    word_list = list(word)  # перетворюємо слово в список літер
    guessed_letters = ["_"] * len(word)  # список, що відображає введені літери
    incorrect_guesses = 0  # лічильник неправильних спроб
    return word, word_list, guessed_letters, incorrect_guesses

# Основний інтерфейс
def game():
    st.title("Гра: Відгадай слово!")
    
    # Кнопка для початку гри
    if "game_started" not in st.session_state:
        st.session_state.game_started = False

    if not st.session_state.game_started:
        if st.button("Почати гру"):
            st.session_state.word, st.session_state.word_list, st.session_state.guessed_letters, st.session_state.incorrect_guesses = start_game()
            st.session_state.game_started = True

    if st.session_state.game_started:
        # Відображення поточного стану гри
        st.write("Слово: " + " ".join(st.session_state.guessed_letters))
        st.image(hangman_images[st.session_state.incorrect_guesses])  # відображаємо картину в залежності від помилок

        letter = st.text_input("Введіть літеру:", max_chars=1)

        if letter:
            # Перевірка, чи буква правильна
            if letter in st.session_state.word_list:
                # Якщо буква правильна, оновлюємо відображення
                for i, char in enumerate(st.session_state.word_list):
                    if char == letter:
                        st.session_state.guessed_letters[i] = letter
                st.success(f"Вірно! Ви відгадали букву: {letter}")
            else:
                # Якщо буква неправильна, збільшуємо лічильник помилок
                st.session_state.incorrect_guesses += 1
                st.error(f"Невірно! Ви не вгадали букву: {letter}")

            # Перевірка на виграш
            if "_" not in st.session_state.guessed_letters:
                st.success("Вітаємо! Ви виграли!")
                st.session_state.game_started = False

            # Перевірка на програш
            if st.session_state.incorrect_guesses >= 10:
                st.error("На жаль, ви програли!")
                st.session_state.game_started = False
