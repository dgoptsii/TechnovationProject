import streamlit as st
import utils
# Function to load the CSS

Misia = ("Навчити людей жестової мови, покращити комунікацію між чуючими та людьми з порушеннями слуху,<br>"
         "сприяти розвитку інклюзивного суспільства.")

Visis = ("Зробити вивчення мови для дітей захоплюючим і<br>"
         "доступним розвитком, допомагаючи їм розвивати мовні<br>"
          "навички інтерактивні завдання та веселий процес гри.")

Meta = ("Створити інклюзивний інтерактивний простір, який<br>"
        "допоможе дітям з обмеженими можливостями слуху<br>"
        "розвинути навички спілкування, критичного мислення та<br>"
        "креативності через доступну та захоплюючу гру. Сприяти їх<br>"
        "соціалізації, самореалізації та інтеграції у сучасне суспільство,<br>"
        "використовуючи інноваційні технології, які будуть враховувати особисті потреби дітей.")

def app():
     
     utils.load_css("style.css")
     # Load the CSS file to apply styles globally
     
     st.markdown('<div class="title">Місія</div>', unsafe_allow_html=True)
     st.markdown(f'<div class="text">{Misia}</div>', unsafe_allow_html=True)

     st.markdown('<div class="title">Візія</div>', unsafe_allow_html=True)
     st.markdown(f'<div class="text">{Visis}</div>', unsafe_allow_html=True)

     st.markdown('<div class="title">Мета</div>', unsafe_allow_html=True)
     st.markdown(f'<div class="text">{Meta}</div>', unsafe_allow_html=True)