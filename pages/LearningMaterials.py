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
    col1, col2,= st.columns(2)
    with col1:
        st.video("https://youtu.be/J6Kb4hMAbHE?si=fjXLA9rZvZ9WBX_Z")
        st.markdown(f'<div class="text">{texts[lang]["timecode_text"]}</div>', unsafe_allow_html=True)
    with col2:
        st.video("https://youtu.be/YKD8q4OQhPo?si=4YgiNlWU8sDv-dKP")
        st.markdown(f'<div class="text">{texts[lang]["greeting_video_text"]}</div>', unsafe_allow_html=True)
        

    # Навчальні матеріали лінки
    st.markdown(f'<div class="title_subheader">{texts[lang]["materials_title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{texts[lang]["links"]}</div>', unsafe_allow_html=True)


    # Алфавіт
    st.markdown(f'<div class="titi">{texts[lang]["video_title"]}</div>', unsafe_allow_html=True)

    # Создаем 3 колонки
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
     # Видео для першого столбца
    with col1:
     st.video("https://www.youtube.com/watch?v=Y3yPvsOLc5k")
     st.video("https://www.youtube.com/watch?v=A4kQCBdG5HA")
     st.video("https://www.youtube.com/watch?v=q_6cni-XkUY")
     st.video("https://www.youtube.com/watch?v=X2ymxV1SB_M")

     # Видео для другого столбца
    with col2:
     st.video("https://www.youtube.com/watch?v=8j7KZnsBfhY")
     st.video("https://www.youtube.com/watch?v=teAEIt6anLE")
     st.video("https://www.youtube.com/watch?v=B78Ou5oPtdo")
     st.video("https://www.youtube.com/watch?v=uCRSEbYOys4")

     # Видео для третього столбца
    with col3:
     st.video("https://www.youtube.com/watch?v=nJfXbqjyaB4")
     st.video("https://www.youtube.com/watch?v=9ivfqYlRQw4")
     st.video("https://www.youtube.com/watch?v=rin2PWlz2Ns")
     st.video("https://www.youtube.com/watch?v=02Cb_huQRmw")

    # Видео для четвертого столбца
    with col4:
     st.video("https://www.youtube.com/watch?v=m2pcbkZKQCU")
     st.video("https://www.youtube.com/watch?v=2Xzzg2Qk_zA")
     st.video("https://www.youtube.com/watch?v=LJjonvptVAo")
     st.video("https://www.youtube.com/watch?v=WeBxscv_iFE")

    # Видео для п'ятого столбца
    with col5:
     st.video("https://www.youtube.com/watch?v=LfGdX20yQ_g")
     st.video("https://www.youtube.com/watch?v=b41xE7IH5DM")
     st.video("https://www.youtube.com/watch?v=S1Mz4FtK3y0")
     st.video("https://www.youtube.com/watch?v=o-UzR-smI90")

    # Видео для шостого столбца
    with col6:
     st.video("https://www.youtube.com/watch?v=uqcAzaxvmQg")
     st.video("https://www.youtube.com/watch?v=s5pHhi0l_ZY")
     st.video("https://www.youtube.com/watch?v=Ziqz_58nOVo")

    