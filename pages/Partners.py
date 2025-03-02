import streamlit as st
import utils
# Function to load the CSS

partners = (
        "Для нас важливі партнери, оскільки вони допомагають розширювати наш проект та підвищують довіру до нашої аудіторії, що дозволяє нам реалізувати соціпальну ініціативу для розвитку жествої мови, та досягнути ефективніше нашу ціль.<br>"
        "Всеукраїнська громадська організація людей з вадами слуху. Була заснована у 1933 році. Член Всесвітньої федерації глухих. На сьогодні обласні і територіальні організації УТОГ об'єднують понад 50 тисяч громадян України з порушеннями слуху та мови.<br>"
        "Всеукраїнська громадська організація спортивного спрямування. Спортивна федерація глухих України є добровільним всеукраїнським об'єднанням фізичних осіб з інвалідністю зі слуху фізкультурно - спортивної спрямованості, основним завданням якої є забезпечення розвитку дефлімпійського руху і спорту глухих в Україні.<br>"
        "Команда ПОГ «Центр соціального бізнесу» надає послуги перекладу жестової мови. Послуги надаються Замовнику в будь-якому зручному форматі. Багатьох слів, особливо сучасних, не існує в жестовій мові. Тому деякі слова, для яких відсутнє жестове позначення, просто неможливо перекласти без використання української дактильної абетки. Вони також проводят захости по безбар’єрності.<br>"
    )


def app():
    # Load the CSS file to apply styles globally
    
    utils.load_css("style.css")
    st.markdown('<div class="title">Партнери</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text">{partners}</div>', unsafe_allow_html=True) 

 
    st.header("Партнери")
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Flag_utog.svg/150px-Flag_utog.svg.png"
    st.image(image_url, caption="Партнери 1", use_column_width=150)

    st.header("Партнери")
    image_url = "https://www.invasport.kiev.ua/images/partnery/partner-06.jpg"
    st.image(image_url, caption="Партнери 2", use_column_width=150)

    st.header("Партнери")
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRa7-D_kDabaXFJgBVHmstmmsyAZfTLstru9A&s"
    st.image(image_url, caption="Партнери 3", use_column_width=150)
    



   
   
   
   

