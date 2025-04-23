import streamlit as st
import utils

# Тексти описів
Spread = ("Перекладач жестової мови Spread the Sign – це міжнародний онлайн-словник жестової мови, який допомагає вивчати та розуміти жести різних країн. Сервіс містить відео з жестами та їх значеннями.")
Megogo = ("Курс жестової мови для MEGOGO – це цикл повноцінних уроків, що охоплює основи жестової мови та дактилю (жестовий алфавіт). Курс допоможе вам опанувати базові жести для повсякденного спілкування та краще зрозуміти культуру глухих людей.")
Timecode = ("Таймкод: 1.24 - алфавіт. У цьому відео детально розповідають що таке дактиль, базові жести і дають пораду як його вивчити")
Video = ("Відео, яке допоможе вивчити привітання")

def app():
    st.markdown('<div class="titi">Навчальні матеріали</div>', unsafe_allow_html=True)

    # Відео в 4 колонки (Streamable)
    st.markdown(f'<div class="titi">Колекція жестів (Streamable)</div>', unsafe_allow_html=True)

    video_links = [
        "https://streamable.com/s1a52u", "https://streamable.com/yek737", "https://streamable.com/x0e6aw", "https://streamable.com/b924oz",
        "https://streamable.com/1eoqcp", "https://streamable.com/2vyljf", "https://streamable.com/ei1z6l", "https://streamable.com/4dck4r",
        "https://streamable.com/u0xtq5", "https://streamable.com/wbfmpk", "https://streamable.com/6axis0", "https://streamable.com/3nhig0",
        "https://streamable.com/zke9k4", "https://streamable.com/7hfdi3", "https://streamable.com/afxdho", "https://streamable.com/xino0r",
        "https://streamable.com/mns2jy", "https://streamable.com/44gvq5", "https://streamable.com/zkbh0n", "https://streamable.com/69354p",
        "https://streamable.com/qbmjb4"
    ]

    for i in range(0, len(video_links), 4):
        cols = st.columns(4)
        for j in range(4):
            if i + j < len(video_links):
                with cols[j]:
                    st.markdown(f"""
                        <iframe src="{video_links[i + j]}" width="100%" height="220" frameborder="0" allowfullscreen></iframe>
                    """, unsafe_allow_html=True)

    # Блок з двома відео (YouTube)
    st.markdown(f'<div class="titi">Відео жестів</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.video("https://youtu.be/J6Kb4hMAbHE?si=fjXLA9rZvZ9WBX_Z")
        st.markdown(f'<div class="text">{Timecode}</div>', unsafe_allow_html=True)
    with col2:
        st.video("https://youtu.be/YKD8q4OQhPo?si=4YgiNlWU8sDv-dKP")
        st.markdown(f'<div class="text">{Video}</div>', unsafe_allow_html=True)

    # Корисні ресурси
    st.header(" Ресурси для вивчення жестової мови")
    st.markdown("[Spread The Sign – онлайн-словник](https://spreadthesign.com/uk.ua/search/?cls=1)")
    st.markdown(f'<div class="text">{Spread}</div>', unsafe_allow_html=True)
    st.markdown("[Курс жестової мови на Megogo](https://megogo.net/ua/view/3820211-kurs-zhestovo-movi-ukra-nskoyu-movoyu.html)")
    st.markdown(f'<div class="text">{Megogo}</div>', unsafe_allow_html=True)
