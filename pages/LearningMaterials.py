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
    

    # Тексти навчальних матеріалів
    texts = {
        'uk': {
            'title': "Навчальні матеріали",
            'subtitle1': "Посилання на інші ресурси",
            'subtitle2': "Легкий рівень",
            'subtitle3': "Середній рівень",
            'subtitle4': "Складний рівень",
            'video_title': "Відео жестів",
            'timecode_text': "Таймкод: 1.24 - алфавіт. У цьому відео детально розповідають що таке дактиль, базові жести і дають пораду як його вивчити.",
            'greeting_video_text': "Відео, яке допоможе вивчити привітання.",
            'materials_title': "Навчальні матеріали",
            'links': ('<a href="https://spreadthesign.com/uk.ua/search/?cls=1" target="_blank">Spread The Sign – онлайн-словник</a><br>'
                      '<a href="https://megogo.net/ua/view/3820211-kurs-zhestovo-movi-ukra-nskoyu-movoyu.html" target="_blank">Курс жестової мови на Megogo</a>')
        },
        'en': {
            'title': "Educational Materials",
            'subtitle1': "Links to other resources",
            'subtitle2': "Easy level",
            'subtitle3': "Medium level",
            'subtitle4': "Hard level",
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
    st.markdown(f'<div class="title_subheader">{texts[lang]["subtitle1"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{texts[lang]["links"]}</div>', unsafe_allow_html=True)

    
    st.markdown(f'<div class="title_subheader">{texts[lang]["subtitle2"]}</div>', unsafe_allow_html=True)
    # Створюємо 3 колонки
    col1, col2, = st.columns(2)
    
     # Видео для першого столбца
    with col1:
     
     st.video("https://www.youtube.com/watch?v=Y3yPvsOLc5k")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">А</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=B78Ou5oPtdo")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">И</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=B78Ou5oPtdo")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Н</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=LJjonvptVAo")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">С</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=nJfXbqjyaB4")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Л</p>', unsafe_allow_html=True)

     # Видео для другого столбца
    with col2:
     
     st.video("https://www.youtube.com/watch?v=8j7KZnsBfhY")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Е</p>', unsafe_allow_html=True) 
     st.video("https://www.youtube.com/watch?v=02Cb_huQRmw") 
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">О</p>', unsafe_allow_html=True)   
     st.video("https://www.youtube.com/watch?v=m2pcbkZKQCU")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">П</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=WeBxscv_iFE")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Т</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=9ivfqYlRQw4")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">М</p>', unsafe_allow_html=True)

    st.markdown(f'<div class="title_subheader">{texts[lang]["subtitle3"]}</div>', unsafe_allow_html=True)
    # Створюємо 3 колонки
    col1, col2, = st.columns(2)
    
     # Видео для першого столбца
    with col1:
     
     st.video("https://www.youtube.com/watch?v=Y3yPvsOLc5k")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">А</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=q_6cni-XkUY")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">В</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=B78Ou5oPtdo")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">И</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=B78Ou5oPtdo")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Н</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=9ivfqYlRQw4")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">М</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=m2pcbkZKQCU")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">П</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=WeBxscv_iFE")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Т</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=2Xzzg2Qk_zA")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Р</p>', unsafe_allow_html=True)
     
     # Видео для другого столбца
    with col2:
     
     st.video("https://www.youtube.com/watch?v=A4kQCBdG5HA")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Б</p>', unsafe_allow_html=True) 
     st.video("https://www.youtube.com/watch?v=8j7KZnsBfhY") 
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Е</p>', unsafe_allow_html=True)   
     st.video("https://www.youtube.com/watch?v=uCRSEbYOys4")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">І</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=nJfXbqjyaB4")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Л</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=02Cb_huQRmw") 
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">О</p>', unsafe_allow_html=True) 
     st.video("https://www.youtube.com/watch?v=LJjonvptVAo")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">С</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=LfGdX20yQ_g")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">У</p>', unsafe_allow_html=True)
     

    st.markdown(f'<div class="title_subheader">{texts[lang]["subtitle4"]}</div>', unsafe_allow_html=True)
    # Створюємо 3 колонки
    col1, col2, = st.columns(2)
    
     # Видео для першого столбца
    with col1:
     
     st.video("https://www.youtube.com/watch?v=Y3yPvsOLc5k")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">А</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=q_6cni-XkUY")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">В</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=8j7KZnsBfhY") 
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Е</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=B78Ou5oPtdo")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">И</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=nJfXbqjyaB4")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Л</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=02Cb_huQRmw") 
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">О</p>', unsafe_allow_html=True) 
     st.video("https://www.youtube.com/watch?v=2Xzzg2Qk_zA")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Р</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=WeBxscv_iFE")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Т</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=b41xE7IH5DM")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Ф</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=o-UzR-smI90")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Ч</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=s5pHhi0l_ZY")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Ю</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=B78Ou5oPtdo")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Н</p>', unsafe_allow_html=True)

     # Видео для другого столбца
    with col2:
     
     st.video("https://www.youtube.com/watch?v=A4kQCBdG5HA")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Б</p>', unsafe_allow_html=True) 
     st.video("https://www.youtube.com/watch?v=X2ymxV1SB_M") 
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Г</p>', unsafe_allow_html=True)   
     st.video("https://www.youtube.com/watch?v=teAEIt6anLE")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Ж</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=uCRSEbYOys4")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">І</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=9ivfqYlRQw4")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">М</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=m2pcbkZKQCU")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">П</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=LJjonvptVAo")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">С</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=LfGdX20yQ_g")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">У</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=S1Mz4FtK3y0")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Х</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=uqcAzaxvmQg")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Ш</p>', unsafe_allow_html=True)
     st.video("https://www.youtube.com/watch?v=Ziqz_58nOVo")
     st.markdown('<p style="text-align: center; color: #276B5A; font-weight: bold;">Я</p>', unsafe_allow_html=True)