import streamlit as st
import utils

def app():
    utils.load_css("style.css")  # Завантаження стилів

    # Логотип по центру над текстом
    st.markdown(
        """
        <div style="display: flex; justify-content: center; margin-top: -20px; margin-bottom: 20px;">
            <img src="https://i.postimg.cc/44VpG0zP/IT-GIRLS.png" width="200">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Заголовок "Про нас"
    st.markdown('<div class="title_header">Про нас</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="text">
            Ми - група підлітків, які є учасниками міжнародного проекту "Technovation Girls". <br> <br>
            Ми довго думали над темою нашого проєкту, проте врешті-решт зупинилися на інклюзії. 
            Нашою мрією стало допомагати дітям з вадами слуху вливатися в сучасне суспільство і не відчувати себе зайвими, 
            допомагати їм рухатися далі. 
            Із часом зародилася ідея створення доступної і сучасної гри, яка є інструментом для навчання жестової мови, яка об'єднувала б людей з різних культур та середовищ.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Розділ "Місія, Візія, Мета"
    st.markdown('<div class="title_subheader">Місія 🎯</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="text">
           Сприяти розвитку інклюзивного суспільства, де кожен має голос.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title_subheader">Візія 👓</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="text">
            Світ, у якому мовне різноманіття сприймається як сила, а кожна людина — незалежно від її здатності чути — має рівний доступ до спілкування, освіти й можливостей.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title_subheader">Мета 🌍</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="text">
        Сприяти побудові інклюзивного суспільства, де жестова мова є природною частиною взаємодії, а технології стають засобом рівності, підтримки та взаєморозуміння.
        </div>
        """,
        unsafe_allow_html=True
    )

