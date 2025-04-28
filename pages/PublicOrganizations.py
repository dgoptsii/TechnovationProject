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
        if st.button("Українська", use_container_width=True, key="ua_btn_org"):
            st.session_state.language = 'uk'
    with col2:
        if st.button("English", use_container_width=True, key="en_btn_org"):
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

    # Тексти для громадських організацій
    texts = {
        'uk': {
            'title': "Громадські організації",
            'utog_title': "УТОГ",
            'utog_text': ("Всеукраїнська громадська організація людей з вадами слуху. Була заснована у 1933 році. "
                          "Член Всесвітньої федерації глухих. Об'єднує понад 50 тисяч громадян України."),
            'invasport_title': "ІНВАСПОРТ",
            'invasport_text': ("Всеукраїнська спортивна організація для людей з порушенням слуху. Основна мета - розвиток дефлімпійського руху в Україні."),
            'pog_title': "ПОГ",
            'pog_text': ("Центр соціального бізнесу, який надає послуги перекладу жестової мови та проводить заходи з безбар'єрності.")
        },
        'en': {
            'title': "Public Organizations",
            'utog_title': "UTOG",
            'utog_text': ("The All-Ukrainian Public Organization of People with Hearing Impairments. Founded in 1933. "
                          "Member of the World Federation of the Deaf. Unites over 50,000 citizens of Ukraine."),
            'invasport_title': "INVASPORT",
            'invasport_text': ("All-Ukrainian sports organization for people with hearing impairments. Main goal - development of the Deaflympic movement in Ukraine."),
            'pog_title': "POG",
            'pog_text': ("Center for Social Business, providing sign language translation services and barrier-free communication activities.")
        }
    }

    lang = st.session_state.language

    # Заголовок
    st.markdown(f'<div class="title_header">{texts[lang]["title"]}</div>', unsafe_allow_html=True)

    # УТОГ
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://cnap-pl.gov.ua/UTOG_OVAL.png", width=150)
    with col2:
        st.markdown(f'<div class="title_subheader">{texts[lang]["utog_title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="text">{texts[lang]["utog_text"]}</div>', unsafe_allow_html=True)

    # ІНВАСПОРТ
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2LzUJRpQ_EDlyT0Wgkl9ccfboOfBD3f6n3A&s", width=150)
    with col2:
        st.markdown(f'<div class="title_subheader">{texts[lang]["invasport_title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="text">{texts[lang]["invasport_text"]}</div>', unsafe_allow_html=True)

    # ПОГ
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRa7-D_kDabaXFJgBVHmstmmsyAZfTLstru9A&s", width=150)
    with col2:
        st.markdown(f'<div class="title_subheader">{texts[lang]["pog_title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="text">{texts[lang]["pog_text"]}</div>', unsafe_allow_html=True)
