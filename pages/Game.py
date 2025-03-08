import streamlit as st
import random

# Список слів для гри
word_list = ["Добро", "Любов", "Друзі"]
word = random.choice(word_list).upper()  # Вибираємо випадкове слово з списку
count = st.session_state.get("count", 5)  # Кількість спроб (зберігається між запусками)
guessed_letters = st.session_state.get("guessed_letters", [])  # Відгадані букви

# Завантажуємо зображення для відображення
image_paths = ["image_5.png", "image_4.png", "image_3.png", "image_2.png", "image_1.png", "image_0.png"]

# Інтерфейс Streamlit
st.title("Гра: Вгадай слово!")
st.image(image_paths[5 - count])  # Показуємо зображення в залежності від кількості спроб

# Відображаємо поточний стан слова (відгадані букви або "_")
display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
st.subheader(f"Слово: {display_word}")

# Введення букви (без кнопки)
letter = st.text_input("Введіть букву:", max_chars=1).upper()

# Перевіряємо введену букву відразу після вводу
if letter and letter not in guessed_letters:
    if letter in word:
        guessed_letters.append(letter)  # Додаємо букву до списку відгаданих
        st.session_state["guessed_letters"] = guessed_letters
    else:
        count -= 1  # Якщо букви немає, зменшуємо кількість спроб
        st.session_state["count"] = count

# Перевірка на виграш або поразку
if "_" not in display_word:
    st.success(f"🎉 Ви виграли! Слово: {word}")
elif count == 0:
    st.error(f"Ви програли. Загадане слово: {word}")

# Зберігаємо стан між запусками
st.session_state["count"] = count
st.session_state["guessed_letters"] = guessed_letters

