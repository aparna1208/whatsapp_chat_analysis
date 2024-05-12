import streamlit as st
from streamlit_option_menu import option_menu

import about
import home
import login


# st.set_page_config(
# page_title="WhatApp Chat Analyzer"
# )

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            'title': title,
            'function': function
        })


    def run():

        with st.sidebar:
            app = option_menu(
                menu_title="Welcome!!, WhatsApp Chat Analyzer",
                options=["home", 'login', 'about'],
                # icons = ['house-fill','person-circle','tropy-fill'],
                # menu_icon = 'chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-algin": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": '#02ab21'}, }
            )

        if app == "home":
            home.app()

        if app == "login":
            login.app()

        if app == "about":
            about.app()

    run()
