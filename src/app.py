import streamlit as st

home_page = st.Page("home.py", title="BioComp", icon="🌳")
about_page = st.Page("about.py", title="About")
usage_page = st.Page("usage.py", title="Usage")

pg = st.navigation([home_page, about_page, usage_page])
pg.run()
