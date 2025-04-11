import streamlit as st
import utils
# Function to load the CSS

УТОГ = ("Всеукраїнська громадська організація людей з вадами слуху. Була заснована у 1933 році. Член Всесвітньої федерації глухих. На сьогодні обласні і територіальні організації УТОГ об'єднують понад 50 тисяч громадян України з порушеннями слуху та мови.")

ІНВАСПОРТ = ("Всеукраїнська громадська організація спортивного спрямування. Спортивна федерація глухих України є добровільним всеукраїнським об'єднанням фізичних осіб з інвалідністю зі слуху фізкультурно - спортивної спрямованості, основним завданням якої є забезпечення розвитку дефлімпійського руху і спорту глухих в Україні.")

ПОГ = ("Команда ПОГ «Центр соціального бізнесу» надає послуги перекладу жестової мови. Послуги надаються Замовнику в будь-якому зручному форматі. Багатьох слів, особливо сучасних, не існує в жестовій мові. Тому деякі слова, для яких відсутнє жестове позначення, просто неможливо перекласти без використання української дактильної абетки. Вони також проводят захости по безбар’єрності.")

def app():
    # Load the CSS file to apply styles globally
    
     st.markdown('<div class="title">Партнери</div>', unsafe_allow_html=True)

    
     col1, col2 = st.columns([1, 3])
         
     with col1:
         image_url = "https://cnap-pl.gov.ua/UTOG_OVAL.png"
         st.image(image_url, width=150)
    
     with col2:
         st.markdown('<div class="title">УТОГ</div>', unsafe_allow_html=True)
         st.markdown(f'<div class="text">{УТОГ}</div>', unsafe_allow_html=True) 
    

     col1, col2 = st.columns([1, 3])
 

     with col1:
         image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2LzUJRpQ_EDlyT0Wgkl9ccfboOfBD3f6n3A&s"
         st.image(image_url, width=150)

     with col2:
         st.markdown('<div class="title">ІНВАСПОРТ</div>', unsafe_allow_html=True)
         st.markdown(f'<div class="text">{ІНВАСПОРТ}</div>', unsafe_allow_html=True) 
   

     col1, col2 = st.columns([1, 3])


     with col1:
         image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRa7-D_kDabaXFJgBVHmstmmsyAZfTLstru9A&s"
         st.image(image_url, width=150)

     with col2:
          st.markdown('<div class="title">ПОГ</div>', unsafe_allow_html=True)
          st.markdown(f'<div class="text">{ПОГ}</div>', unsafe_allow_html=True)