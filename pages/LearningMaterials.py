import streamlit as st
import utils
# Function to load the CSS

def app():
 # Load the CSS file to apply styles globally
 utils.load_css("style.css")

 st.header("Навчальні матеріали")
 image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTp4si91mL3kimJO2EZY-_sB6Gt5bE4oktPdw&s"
 st.image(image_url, caption="А", use_column_width=True)

 st.header("Навчальні матеріали")
 st.markdown(
     f"""
    <div style="text-align:center;">
        <imge_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTp4si91mL3kimJO2EZY-_sB6Gt5bE4oktPdw&s" width="300" height="200">
        <p>А</p>
    </div>
    """,
    unsafe_allow_html=True
    )
 
 # Videos 
st.header ("Відео жестів")


col1, col2 = st.columns(2)  # Два столбца

with col1:
    st.video("https://youtu.be/J6Kb4hMAbHE?si=fjXLA9rZvZ9WBX_Z")
    st.markdown("Таймкод: 1.24- алфавіт. У цьому відео детальніше розповідають що таке дактиль, базові жести і дають пораду як його вивчити")


with col2:
    st.video("https://youtu.be/YKD8q4OQhPo?si=4YgiNlWU8sDv-dKP") 

    st.markdown("Відео, яке допоможе вивчити привітання")