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
            HiG_support@gmail.com
        </div>
        """,
        unsafe_allow_html=True
    )