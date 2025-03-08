import streamlit as st
import random


def app():
 st.title("Game")
 st.write("Game will be implemented here.")

 # Список слів для гри
 word = ["ДОБРО", "ЛЮБОВ", "ДРУЗІ"]

  # Вибір випадкового слова
 random_word = random.choice(word)
 print(random_word)  
 count = st.session_state.get("count", 5)  # Кількість спроб (зберігається між запусками)
 guessed_letters = st.session_state.get("guessed_letters", [])  # Відгадані букви

  # Завантажуємо зображення для відображення
 image_paths = ["https://i.postimg.cc/QN7GYxrM/2025-03-08-201156.png", "https://i.postimg.cc/QCcC1v85/photo-2025-03-08-20-13-40.jpg", "https://i.postimg.cc/CLdDptmd/2025-03-08-201338.png", "", "https://i.postimg.cc/TYXpf20c/photo-2025-03-08-20-13-46.jpg", "https://i.postimg.cc/SQn8w3ZR/2025-03-08-201424.png", "https://i.postimg.cc/PrzNxGFn/photo-2025-03-08-20-13-52.jpg"]

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