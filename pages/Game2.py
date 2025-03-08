import random

def choose_word():
    # Список слів для гри
    words = ['папір', 'комп’ютер', 'машина', 'весна', 'сонце', 'кіт', 'дерево']
    return random.choice(words)

def display_word(word, guessed_letters):
    # Показує поточний стан слова з відгаданими літерами
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6
    print("Вітаємо в грі Вісельниця!")
    
    while tries > 0:
        print("\nВідгадане слово: " + display_word(word, guessed_letters))
        print(f"Залишилось спроб: {tries}")
        
        guess = input("Введіть літеру: ").lower()
        
        if guess in guessed_letters:
            print("Цю літеру ви вже вводили!")
            continue
        
        if len(guess) != 1 or not guess.isalpha():
            print("Будь ласка, введіть тільки одну літеру.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            tries -= 1
            print(f"Немає такої літери в слові.")
        
        if all(letter in guessed_letters for letter in word):
            print(f"\nВітаємо! Ви виграли! Слово було: {word}")
            break
    else:
        print(f"\nВи програли! Слово було: {word}")

# Запуск гри
hangman()
