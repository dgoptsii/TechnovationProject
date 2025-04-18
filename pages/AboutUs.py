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
    st.markdown('<div class="titi">Про нас</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="text">
            Ми - група підлітків, які є учасниками міжнародного проекту "Technovation Girls".<br>
            Ми довго думали над темою нашого проєкту, проте врешті-решт зупинилися на інклюзії.<br>
            Нашою мрією стало допомагати дітям з вадами слуху вливатися в сучасне суспільство і не відчувати себе зайвими,<br>
            допомагати їм рухатися далі.<br>
            Із часом зародилася ідея створення доступної і сучасної гри, яка є інструментом для навчання жестової мови,<br>
            яка об'єднувала б людей з різних культур та середовищ.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="text">
            Приєднуйтесь до нас і допоможіть будувати інклюзивне майбутнє!<br>
            Станьте частиною нашої спільноти – разом ми можемо змінити світ!<br>
            Якщо у вас виникають питання чи якісь проблеми, ви можете звернутися до нас за електронною адресою:<br> 
            HiG_support@gmail.com
        </div>
        """,
        unsafe_allow_html=True
    )

    # Розділ "Місія, Візія, Мета"
    st.markdown('<div class="title">Місія</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="text">
            Навчити людей жестової мови, покращити комунікацію між чуючими та людьми з порушеннями слуху,<br>
            сприяти розвитку інклюзивного суспільства.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title">Візія</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="text">
            Зробити вивчення мови для дітей захоплюючим і<br>
            доступним розвитком, допомагаючи їм розвивати мовні<br>
            навички інтерактивні завдання та веселий процес гри.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title">Мета</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="text">
            Створити інклюзивний інтерактивний простір, який<br>
            допоможе дітям з обмеженими можливостями слуху<br>
            розвинути навички спілкування, критичного мислення та<br>
            креативності через доступну та захоплюючу гру. Сприяти їх<br>
            соціалізації, самореалізації та інтеграції у сучасне суспільство,<br>
            використовуючи інноваційні технології, які будуть враховувати особисті потреби дітей.
        </div>
        """,
        unsafe_allow_html=True
    )

