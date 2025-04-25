import streamlit as st
import utils
# Function to load the CSS

def app():
    # Load the CSS file to apply styles globally
    
    st.markdown('<div class="title_header">Допомогти проекту</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="text">
            Приєднуйтесь до нас і допоможіть будувати інклюзивне майбутнє!<br>
            Станьте частиною нашої спільноти – разом ми можемо змінити світ!<br> <br>
            Якщо у вас виникають питання чи якісь проблеми, ви можете звернутися до нас за електронною адресою:<br> 
            hartingestures@gmail.com
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="title_subheader">Ваші відгуки - важливі для нас ☺️!</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="text" style="margin-top: 30px;">
            <strong>Нам важлива ваша думка!</strong><br>
            Якщо у вас є ідеї щодо покращення гри або ви хочете поділитися своїми враженнями — напишіть нам!<br><br>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLScAlVmTQe6wKm4U7bqtnEbU8pravDP0XuGnP7ZlMWWw9SPSHA/viewform?usp=header" target="_blank">Надіслати відгук</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title_subheader">Розповсюджнення інформації 🤳</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
         <div class="text">
           Розкажіть про наш проєкт друзям, у соцмережах чи на заходах. 
           Це допомагає нам знайти нову аудиторію та потенціальних партнерів.<br><br>
           <a href="https://www.instagram.com/heartingestures_/profilecard/?igsh=bHd2bGJnaWg4Ynp4" target="_blank">Наш Інстаграм</a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title_subheader">Партнерсво 🤝</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="text">
            Ми відкриті для співпраці з огранізаціями, які поділяють наші цінності!<br> 
            Напишіть нам, якщо хочете стати частиною змін:<br> 
            heartingestures@gmail.com
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title_subheader">З повагою, команда Grlpwr!</div>', unsafe_allow_html=True)