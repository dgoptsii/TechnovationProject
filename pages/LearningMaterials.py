import streamlit as st
import utils
# Function to load the CSS


Timecode =("Таймкод: 1.24- алфавіт. У цьому відео детально розповідають що таке дактиль, базові жести і дають пораду як його вивчити")
Video = ("Відео, яке допоможе вивчити привітання")

def app():
  st.markdown('<div class="title_header">Навчальні матеріали</div>', unsafe_allow_html=True)
  
 # Videos 
  col1, col2 = st.columns(2)  # Два столбца
  with col1:
    st.video("https://youtu.be/J6Kb4hMAbHE?si=fjXLA9rZvZ9WBX_Z")
    st.markdown(f'<div class="text">{Timecode}</div>', unsafe_allow_html=True) 
    with col2:
      st.video("https://youtu.be/YKD8q4OQhPo?si=4YgiNlWU8sDv-dKP") 
      st.markdown(f'<div class="text">{Video}</div>', unsafe_allow_html=True) 

  st.markdown('<div class="title_subheader">Навчальні матеріали</div>', unsafe_allow_html=True)
  
  st.markdown(
    '<div class="text"><a href="https://spreadthesign.com/uk.ua/search/?cls=1" target="_blank">Spread The Sign – онлайн-словник</a><br> ' \
    '<a href="https://megogo.net/ua/view/3820211-kurs-zhestovo-movi-ukra-nskoyu-movoyu.html" target="_blank">Курс жестової мови на Megogo</a>',
    unsafe_allow_html=True
  )
