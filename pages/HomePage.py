import streamlit as st
import utils

Misia = ("Навчити людей жестової мови, покращити комунікацію<br>"
          "між чуючими та людьми з порушеннями слуху, сприяти<br>"
           "розвитку інклюзивного суспільства."
           )

Visis = ("Зробити вивчення мови для дітей захоплюючим і<br>"
         "доступним розвитком, допомагаючи їм розвивати мовні<br>"
         "навички інтерактивні завдання та веселий процес гри."
         )

Meta = ("Створити інклюзивний інтерактивний простір, який<br>"
        "допоможе дітям з обмеженими можливостями слуху<br>"
         "розвинути навички спілкування, критичного мислення та<br>"
         "креативності через доступну та захоплюючу гру. Сприяти<br>"
          "їх соціалізації, самореалізації та інтеграції у сучасне<br>"
          "суспільство, використовуючи інноваційні технології, які<br>"
          "будуть враховувати особисті потреби дітей."
          )

def app():
    # Load the CSS file to apply styles globally
     utils.load_css("style.css")

     st.markdown('<div class="title">Місія</div>', unsafe_allow_html=True)
     st.markdown(f'<div class="rules">{Misia}</div>', unsafe_allow_html=True)

     st.markdown('<div class="title">Візія</div>', unsafe_allow_html=True)
     st.markdown(f'<div class="rules">{Visis}</div>', unsafe_allow_html=True)

     st.markdown('<div class="title">Мета</div>', unsafe_allow_html=True)
     st.markdown(f'<div class="rules">{Meta}</div>', unsafe_allow_html=True)