import streamlit as st

home_page = st.Page("home_page.py", title="BioComp", icon="🌳")
about_page = st.Page("about_page.py", title="About")
usage_page = st.Page("usage_page.py", title="Usage")

pg = st.navigation([home_page, about_page, usage_page])
pg.run()
