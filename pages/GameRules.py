import streamlit as st
import utils

# Function to load the CSS

rules1 = ("Гра складається зі статичних жестів української мови. По черзі ви показуєте літери з перервами. Складність на початку вибираєте.<br>")
st.image("https://i.postimg.cc/44VpG0zP/IT-GIRLS.png", unsafe_allow_html=True)
rules2 = ("Для того щоб гра зарахувала вашу відповідь, тримайте руку в одному положенні 5 секунд.<br>")
rules3 = ("Відсутні такі букви як: Ґ Д З Ї Й К Ц Щ Ь, оскільки вони нестатичні.<br>")
rules4 = ("За кожну неправильну відповідь квітка втрачає одну пелюстку. Якщо квітка залишилась без пелюсток, гра програна.<br>")
rules5 =("Коли слово вгадано відображається вгадане слово і привітання переможця.")

def app():
    # Load the CSS file to apply styles globally
    utils.load_css("style.css")
    st.markdown('<div class="title">Правила гри</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{rules1}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{rules2}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{rules3}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{rules4}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{rules5}</div>', unsafe_allow_html=True)

  