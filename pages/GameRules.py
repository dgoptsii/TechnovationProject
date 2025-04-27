import streamlit as st
import utils

def app():
    utils.load_css("style.css")

    # Сесійний стан для мови
    if 'language' not in st.session_state:
        st.session_state.language = 'uk'

    # Кнопки вибору мови в правому верхньому куті з відступом
    col1, col2, col3, col4 = st.columns([6, 1, 0.5, 1])
    with col2:
        if st.button("Українська"):
            st.session_state.language = 'uk'
    with col4:
        if st.button("English"):
            st.session_state.language = 'en'

    # Тексти правил на двох мовах
    texts = {
        'uk': {
            'title': "Правила гри",
            'rules': [
                "Гра складається зі статичних жестів української мови. По черзі ви показуєте літери з перервами. Складність на початку вибираєте.<br>",
                "Всі жести в грі виконуються правою рукою.<br>",
                "Ви можете бачити слово як серію пропусків («_»), що позначають кожну літеру. Це означає, що кожна літера, яку ви ще не вгадали, залишиться у слові у вигляді підкреслення (_).<br>"
                "Для того щоб гра зарахувала вашу відповідь, тримайте руку в одному положенні 5 секунд.<br>"
                "Якщо жест вже був показаний і розпізнаний, він буде позначений як «already captured».<br>",
                "Відсутні такі букви як: Ґ Д З Ї Й К Ц Щ Ь, оскільки вони нестатичні.<br>",
                "За кожну неправильну відповідь квітка втрачає одну пелюстку. Якщо квітка залишилась без пелюсток, гра програна.<br>",
                "Коли слово вгадано відображається вгадане слово і привітання переможця.<br>",
                "Гра лише українською мовою."
            ]
        },
        'en': {
            'title': "Game Rules",
            'rules': [
                "The game consists of static gestures of the Ukrainian sign language. You sequentially show letters with pauses. Choose difficulty at the start.<br>",
                "To have your answer counted, hold your hand in the same position for 5 seconds.<br>",
                "Letters like: Ґ, Д, З, Ї, Й, К, Ц, Щ, Ь are missing because they are not static.<br>",
                "For each wrong answer, the flower loses a petal. If the flower loses all petals, the game is over.<br>",
                "When a word is guessed, it is displayed along with a winner's congratulations.<br>",
                "The game is only available in Ukrainian."
            ]
        }
    }

    lang = st.session_state.language

    # Заголовок
    st.markdown(f'<div class="title_header">{texts[lang]["title"]}</div>', unsafe_allow_html=True)

    # Показ правил гри
    for idx, rule in enumerate(texts[lang]['rules']):
        st.markdown(f'<div class="text">{rule}</div>', unsafe_allow_html=True)

        # Вставка картинок після певних правил
        if idx == 0:
            st.markdown("""
            <div style="text-align:center;">
                <img src="https://i.postimg.cc/mknsdQ2c/1.jpg">
            </div>
            """, unsafe_allow_html=True)
        if idx == 2:
            st.markdown("""
            <div style="text-align:center;">
                <img src="https://i.postimg.cc/fLJZY2M4/3.jpg">
            </div>
            """, unsafe_allow_html=True)
        if idx == 3:
            st.markdown("""
            <div style="text-align:center;">
                <img src="https://i.postimg.cc/sg4VzGTL/2.jpg">
            </div>
            """, unsafe_allow_html=True)
        if idx == 4:
            st.markdown("""
            <div style="text-align:center;">
                <img src="https://i.postimg.cc/0jSsBz6c/4.jpg">
            </div>
            <div style="text-align:center;">
                <img src="https://i.postimg.cc/NG2BMzNm/5.jpg">
            </div>
            <div style="text-align:center;">
                <img src="https://i.postimg.cc/fT4Z0fFF/6.jpg">
            </div>
            """, unsafe_allow_html=True)

