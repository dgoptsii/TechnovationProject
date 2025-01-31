import streamlit as st 
import AboutUs
import Game
import GameRules
import Partners


#dictionary (key, value)
PAGES = {
    "Game rules": GameRules,
    "About Us": AboutUs,
    "Game": GameRules, 
    "Partners": Partners, 
}

st.sidebar.title('My Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()