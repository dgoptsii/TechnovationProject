import streamlit as st
import utils 
# Function to load the CCS

aboutus = ('Ми - група підлітків, які є учасниками міжнародного проекту "Technovation Girls".<br>'
"Ми довго думали над темою нашого проєкту, проте врешті-решт зупинилися на інклюзії.<br>" 
"Нашою мрією стало допомагати дітям з вадами слуху вливатися в сучасне суспільство і не відчувати себе зайвими,<br>" 
"допомагати їм рухатися далі.<br>"

"Із часом зародилася ідея створення доступної і сучасної гри, яка є інструментом для навчання жестової мови,<br>" 
"яка об'єднувала б людей з різних культур та середовищ."
)

additionalinfo = ("Приєднуйтесь до нас і допоможіть будувати інклюзивне майбутнє!<br>"
"Станьте частиною нашої спільноти – разом ми можемо змінити світ!!<br>"

"Якщо у вас виникають питання чи якісь проблеми, ви можете звернутися до нас за електронною адресою:<br>" 
"HiG_support@gmail.com"
)
   
def app():
   # Load the CSS file to apply styles globally
    utils.load_css("style.css") 
    st.markdown('<div class="title">Про нас</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{aboutus}</div>', unsafe_allow_html=True) 
    st.markdown(f'<div class="text">{additionalinfo}</div>', unsafe_allow_html=True) 



   


