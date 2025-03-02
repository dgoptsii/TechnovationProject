import streamlit as st
import utils
# Function to load the CSS

Misia = (
    "Навчити людей жестової мови, покращити комунікацію\n"
    "між чуючими та людьми з порушеннями слуху, сприяти\n"
    "розвитку інклюзивного суспільства."
)

Visis = (
    "Зробити вивчення мови для дітей захоплюючим і\n"
    "доступним розвитком, допомагаючи їм розвивати мовні\n "
    "навички інтерактивні завдання та веселий процес гри."
)

Meta = (
    "Створити інклюзивний інтерактивний простір, який\n"
    "допоможе дітям з обмеженими можливостями слуху\n"
    "розвинути навички спілкування, критичного мислення тa\n"
    "креативності через доступну та захоплюючу гру. Сприяти\n"
    "їх соціалізації, самореалізації та інтеграції у сучасне\n"
    "суспільство, використовуючи інноваційні технології, які\n"
    "будуть враховувати особисті потреби дітей."
)

def app():
    # Load the CSS file to apply styles globally
    utils.load_css("style.css")

    sections = {
        "Місія": Misia,
        "Візія": Visis,
        "Мета": Meta
    }

    for s in sections.items():
      # Load the CSS file to apply styles globally
     st.markdown(f'<div class="title">{s[0]}</div>', unsafe_allow_html=True)
     st.markdown(f'<div class="text">{s[1]}</div>', unsafe_allow_html=True)