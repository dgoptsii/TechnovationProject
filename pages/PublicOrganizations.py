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

    # Тексти на двох мовах
    texts = {
        'uk': {
            'title': "Громадські організації",
            'utog_title': "УТОГ",
            'utog_text': ("Всеукраїнська громадська організація людей з вадами слуху. Була заснована у 1933 році. "
                          "Член Всесвітньої федерації глухих. На сьогодні обласні і територіальні організації УТОГ об'єднують понад 50 тисяч громадян України з порушеннями слуху та мови."),
            'invasport_title': "ІНВАСПОРТ",
            'invasport_text': ("Всеукраїнська громадська організація спортивного спрямування. Спортивна федерація глухих України є добровільним всеукраїнським об'єднанням фізичних осіб з інвалідністю зі слуху фізкультурно-спортивної спрямованості, основним завданням якої є забезпечення розвитку дефлімпійського руху і спорту глухих в Україні."),
            'pog_title': "ПОГ",
            'pog_text': ("Команда ПОГ «Центр соціального бізнесу» надає послуги перекладу жестової мови. Послуги надаються Замовнику в будь-якому зручному форматі. "
                         "Багатьох слів, особливо сучасних, не існує в жестовій мові. Тому деякі слова перекладаються через українську дактильну абетку. Вони також проводять заходи з безбар'єрності.")
        },
        'en': {
            'title': "Public Organizations",
            'utog_title': "UTOG",
            'utog_text': ("The All-Ukrainian Public Organization of People with Hearing Impairments. Founded in 1933. "
                          "A member of the World Federation of the Deaf. Today, UTOG's regional and territorial organizations unite over 50,000 citizens of Ukraine with hearing and speech impairments."),
            'invasport_title': "INVASPORT",
            'invasport_text': ("The All-Ukrainian public sports organization. The Sports Federation of the Deaf of Ukraine is a voluntary nationwide association of individuals with hearing impairments, focusing on physical culture and sports, with the main goal of developing the Deaflympic movement and sports for the deaf in Ukraine."),
            'pog_title': "POG",
            'pog_text': ("The POG \"Center for Social Business\" team provides sign language translation services. Services are offered to clients in any convenient format. "
                         "Many words, especially modern ones, do not exist in sign language. Therefore, some words are translated using the Ukrainian finger-spelling alphabet. They also organize barrier-free communication events.")
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



