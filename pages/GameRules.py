import streamlit as st
import utils

# Function to load the CSS

rules = (
    "Гра складається зі статичних жестів української мови.<br>"
    "Для того щоб гра зарахувала вашу відповідь, тримайте руку в одному положенні 5 секунд.<br>"
    "Відсутні такі букви як (Нестатичні: Ґ Д З Ї Й К Ц Щ Ь)<br>"
    "За кожну неправильну відповідь квітка втрачає пелюстку. Якщо квітка залишилась без пелюсток, гра програна.<br>"
    "За кожну правильну відповідь квітка росте. Коли слово вгадане, квітка виростає до максимальних розмірів."
)

def app():
    # Load the CSS file to apply styles globally
    utils.load_css("style.css")
    st.markdown('<div class="title">Правила гри</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{rules}</div>', unsafe_allow_html=True)