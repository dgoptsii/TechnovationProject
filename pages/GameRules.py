import streamlit as st
import utils

# Function to load the CSS

rules = (
    "Гра складається зі статичних жестів української мови. По черзі ви показуєте літери з перервами. Складність на початку вибираєте.<br>"
    "Для того щоб гра зарахувала вашу відповідь, тримайте руку в одному положенні 5 секунд.<br>"
    "Відсутні такі букви як: Ґ Д З Ї Й К Ц Щ Ь, оскільки вони нестатичні.<br>"
    "За кожну неправильну відповідь квітка втрачає одну пелюстку. Якщо квітка залишилась без пелюсток, гра програна.<br>"
    "Коли слово вгадано відображається вгадане слово і привітання переможця."
)

def app():
    # Load the CSS file to apply styles globally
    utils.load_css("style.css")
    st.markdown('<div class="title">Правила гри</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{rules}</div>', unsafe_allow_html=True)

def app():
  st.header("Приклади")
  st.markdown(
    f"""
    <div style="text-align:center;">
        <img src="https://i.postimg.cc/jSM8KWcd/1.jpg">
    </div>
    """,
    unsafe_allow_html=True
)