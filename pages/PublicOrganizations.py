import streamlit as st
import utils
# Function to load the CSS

УТОГ = ("Всеукраїнська громадська організація людей з вадами слуху була заснована у 1933 році, і є членом Всесвітньої федерації глухих. На сьогодні обласні і територіальні організації УТОГ об'єднують понад 50 тисяч громадян України з порушеннями слуху та мови.")

ІНВАСПОРТ = ("Всеукраїнська громадська організація спортивного спрямування. Спортивна федерація глухих України є добровільним всеукраїнським об'єднанням фізичних осіб з інвалідністю слуху фізкультурно - спортивної спрямованості, основним завданням якої є забезпечення розвитку олімпійського руху і спорту людей з вадами слуху в Україні.")

ПОГ = ("Команда ПОГ «Центр соціального бізнесу» надає послуги перекладу жестової мови. Послуги надаються замовнику в будь-якому зручному форматі. Багатьох слів, особливо сучасних, не існує в жестовій мові. Тому слова, для яких відсутнє жестове позначення, просто неможливо перекласти без використання української дактильної абетки. Вони також проводять заходи по безбар’єрності.")

def app():
    # Load the CSS file to apply styles globally
    
     st.markdown('<div class="title">Громадські організації</div>', unsafe_allow_html=True)

    
     col1, col2 = st.columns([1, 3])
         
     with col1:
         image_url = "https://cnap-pl.gov.ua/UTOG_OVAL.png"
         st.image(image_url, width=150)
    
     with col2:
         st.markdown('<div class="title">УТОГ</div>', unsafe_allow_html=True)
         st.markdown(f'<div class="text">{УТОГ}</div>', unsafe_allow_html=True) 
    

     col1, col2 = st.columns([1, 3])
 

     with col1:
         image_url = "https://afloo.od.ua/frontend/webcontent/images/websites/12/teams/2021_11_29_19_11_31_1638207332.png"
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