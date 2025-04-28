import streamlit as st
import utils

def app():
    utils.load_css("style.css")

    # Сесійний стан для мови
    if 'language' not in st.session_state:
        st.session_state.language = 'uk'

    # Кнопки вибору мови по центру
    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

    col_empty, col1, col2, col_empty2 = st.columns([2, 1, 1, 2])
    with col1:
        if st.button("Українська", use_container_width=True, key="ua_btn_learning"):
            st.session_state.language = 'uk'
    with col2:
        if st.button("English", use_container_width=True, key="en_btn_learning"):
            st.session_state.language = 'en'

    # Стилі для довших кнопок
    st.markdown(
        """
        <style>
        div.stButton > button {
            padding: 0.8em 3em;
            font-size: 18px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Тексти навчальних матеріалів
    texts = {
        'uk': {
            'title': "Навчальні матеріали",
            'video_title': "Відео жестів",
            'timecode_text': "Таймкод: 1.24 - алфавіт. У цьому відео детально розповідають що таке дактиль, базові жести і дають пораду як його вивчити.",
            'greeting_video_text': "Відео, яке допоможе вивчити привітання.",
            'materials_title': "Навчальні матеріали",
            'links': ('<a href="https://spreadthesign.com/uk.ua/search/?cls=1" target="_blank">Spread The Sign – онлайн-словник</a><br>'
                      '<a href="https://megogo.net/ua/view/3820211-kurs-zhestovo-movi-ukra-nskoyu-movoyu.html" target="_blank">Курс жестової мови на Megogo</a>')
        },
        'en': {
            'title': "Educational Materials",
            'video_title': "Gesture Videos",
            'timecode_text': "Timestamp: 1.24 - alphabet. This video explains in detail what dactylology is, basic gestures, and gives advice on how to learn it.",
            'greeting_video_text': "A video that helps to learn greetings.",
            'materials_title': "Educational Resources",
            'links': ('<a href="https://spreadthesign.com/uk.ua/search/?cls=1" target="_blank">Spread The Sign – online dictionary</a><br>'
                      '<a href="https://megogo.net/ua/view/3820211-kurs-zhestovo-movi-ukra-nskoyu-movoyu.html" target="_blank">Sign language course on Megogo</a>')
        }
    }

    lang = st.session_state.language

    # Заголовок
    st.markdown(f'<div class="title_header">{texts[lang]["title"]}</div>', unsafe_allow_html=True)

    # Відео розділ
    st.markdown(f'<div class="titi">{texts[lang]["video_title"]}</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.video("https://youtu.be/J6Kb4hMAbHE?si=fjXLA9rZvZ9WBX_Z")
        st.markdown(f'<div class="text">{texts[lang]["timecode_text"]}</div>', unsafe_allow_html=True)
    with col2:
        st.video("https://youtu.be/YKD8q4OQhPo?si=4YgiNlWU8sDv-dKP")
        st.markdown(f'<div class="text">{texts[lang]["greeting_video_text"]}</div>', unsafe_allow_html=True)

    # Навчальні матеріали лінки
    st.markdown(f'<div class="title_subheader">{texts[lang]["materials_title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{texts[lang]["links"]}</div>', unsafe_allow_html=True)
