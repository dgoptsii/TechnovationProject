import streamlit as st
import utils
# Function to load the CSS


Spread=("Перекладач жестової мови Spread the Sign – це міжнародний онлайн-словник жестової мови, який допомагає вивчати та розуміти жести різних країн. Сервіс містить відео з жестами та їх значеннями.")
Megogo=("Курс жестової мови для MEGOGO – це цикл повноцінних уроків, що охоплює основи жестової мови та дактилю (жестовий алфавіт). Курс допоможе вам опанувати базові жести для повсякденного спілкування та краще зрозуміти культуру глухих людей.")
Timecode =("Таймкод: 1.24- алфавіт. У цьому відео детально розповідають що таке дактиль, базові жести і дають пораду як його вивчити")
Video = ("Відео, яке допоможе вивчити привітання")

def app():
  st.markdown('<div class="titi">Навчальні матеріали</div>', unsafe_allow_html=True)
  st.markdown(
    f"""
    <div style="text-align:center;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTp4si91mL3kimJO2EZY-_sB6Gt5bE4oktPdw&s" width="300" height="450">
    </div>
    """,
    unsafe_allow_html=True
)

 # Videos 
  st.markdown(f'<div class="titi">Відео жестів</div>', unsafe_allow_html=True)
  col1, col2 = st.columns(2)  # Два столбца
  with col1:
    st.video("https://youtu.be/J6Kb4hMAbHE?si=fjXLA9rZvZ9WBX_Z")
    st.markdown(f'<div class="text">{Timecode}</div>', unsafe_allow_html=True) 
    with col2:
      st.video("https://youtu.be/YKD8q4OQhPo?si=4YgiNlWU8sDv-dKP") 
      st.markdown(f'<div class="text">{Video}</div>', unsafe_allow_html=True) 

  st.header(" Ресурси для вивчення жестової мови")
  st.markdown("[Spread The Sign – онлайн-словник](https://spreadthesign.com/uk.ua/search/?cls=1)")
  st.markdown(f'<div class="text">{Spread}</div>', unsafe_allow_html=True)
  st.markdown("[Курс жестової мови на Megogo](https://megogo.net/ua/view/3820211-kurs-zhestovo-movi-ukra-nskoyu-movoyu.html)")
  st.markdown(f'<div class="text">{Megogo}</div>', unsafe_allow_html=True)
