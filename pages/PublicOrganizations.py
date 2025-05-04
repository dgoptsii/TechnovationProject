
import streamlit as st
import utils

def app():
    utils.load_css("style.css")

    if 'language' not in st.session_state:
        st.session_state.language = 'uk'

    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)

    col_empty, col1, col2, col_empty2 = st.columns([2, 1, 1, 2])
    with col1:
        if st.button("Українська", use_container_width=True, key="ua_btn_help"):
            st.session_state.language = 'uk'
    with col2:
        if st.button("English", use_container_width=True, key="en_btn_help"):
            st.session_state.language = 'en'

    texts = {
        'uk': {
            'title': "Партнери/ГО",
            'utog_title': "УТОГ",
            'utog_text': ("Всеукраїнська громадська організація людей з вадами слуху була заснована у 1933 році, і є членом Всесвітньої федерації глухих. На сьогодні обласні і територіальні організації УТОГ об'єднують понад 50 тисяч громадян України з порушеннями слуху та мови."),
            'invasport_title': "ІНВАСПОРТ",
            'invasport_text': ("Всеукраїнська громадська організація спортивного спрямування. Спортивна федерація глухих України є добровільним всеукраїнським об'єднанням фізичних осіб з інвалідністю слуху фізкультурно - спортивної спрямованості, основним завданням якої є забезпечення розвитку олімпійського руху і спорту людей з вадами слуху в Україні."),
            'pog_title': "ПОГ",
            'pog_text': ("Команда ПОГ «Центр соціального бізнесу» надає послуги перекладу жестової мови. Послуги надаються замовнику в будь-якому зручному форматі. Багатьох слів, особливо сучасних, не існує в жестовій мові. Тому слова, для яких відсутнє жестове позначення, просто неможливо перекласти без використання української дактильної абетки. Вони також проводять заходи по безбар’єрності.")
        },
        'en': {
            'title': "Partners/NGOs",
            'utog_title': "UTOG",
            'utog_text': ("The All-Ukrainian Public Organization of People with Hearing Impairments was founded in 1933 and is a member of the World Federation of the Deaf. Today, the regional and territorial organizations of the UPO unite more than 50,000 Ukrainian citizens with hearing and speech impairments."),
            'invasport_title': "INVASPORT",
            'invasport_text': ("All-Ukrainian public organization of sports orientation. The Sports Federation of the Deaf of Ukraine is a voluntary all-Ukrainian association of individuals with hearing disabilities of a physical culture and sports orientation, whose main task is to ensure the development of the Olympic movement and sports for people with hearing impairments in Ukraine."),
            'pog_title': "POG",
            'pog_text': ("The team of the Center for Social Business provides sign language interpretation services. Services are provided to the customer in any convenient format. Many words, especially modern ones, do not exist in sign language. Therefore, words for which there is no sign designation are simply impossible to translate without using the Ukrainian dactylic alphabet. They also carry out barrier-free activities.")
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