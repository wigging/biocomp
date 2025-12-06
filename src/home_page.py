"""Home page."""

import chemics as cm
import streamlit as st
from streamlit_bokeh import streamlit_bokeh

from optimize_biocomp import calc_opt_biocomp
from plotter import plot_biocomp


st.title("🌳 BioComp")

st.markdown("""Welcome to BioComp, a tool for calculating biomass
composition from ultimate and chemical analysis data. Adjust the
parameters below to update the results. See the About and Usage pages to
learn more.
""")

st.subheader("Ultimate analysis")

col1, col2 = st.columns(2)

with col1:
    ult_c = st.number_input("Carbon, %", min_value=45.0, max_value=75.0, value=53.0)
    ult_h = st.number_input("Hydrogen, %", min_value=4.0, max_value=11.0, value=6.0)

with col2:
    ult_h2o = st.number_input("H₂O, %", min_value=1.0, max_value=30.0, value=2.0)
    ult_ash = st.number_input("Ash, %", min_value=1.0, max_value=30.0, value=2.0)

st.subheader("Chemical analysis")

col3, col4 = st.columns(2)

with col3:
    chem_cell = st.number_input("Cellulose, %", min_value=20.0, max_value=70.0, value=28.9)
    chem_hemi = st.number_input("Hemicellulose, %", min_value=20.0, max_value=70.0, value=22.0)

with col4:
    chem_lig = st.number_input("Lignin, %", min_value=20.0, max_value=70.0, value=36.5)

st.subheader("Splitting parameters")

col5, col6 = st.columns(2)

with col5:
    alpha = st.number_input("α", min_value=0.0, max_value=1.0, value=0.6)
    beta = st.number_input("β", min_value=0.0, max_value=1.0, value=0.8)
    gamma = st.number_input("γ", min_value=0.0, max_value=1.0, value=0.8)

with col6:
    delta = st.number_input("δ", min_value=0.0, max_value=1.0, value=1.0)
    epsilon = st.number_input("ε", min_value=0.0, max_value=1.0, value=1.0)

yc = ult_c / 100
yh = ult_h / 100
yh2o = ult_h2o / 100
yash = ult_ash / 100

ycell = chem_cell / 100
yhemi = chem_hemi / 100
ylig = chem_lig / 100
ychem = [ycell, yhemi, ylig]

if st.checkbox("Optimize"):
    # Biomass composition using optimized splitting parameters
    bc, splits = calc_opt_biocomp(yc, yh, ychem, yh2o, yash)
else:
    # Biomass composition using given splitting parameters
    bc = cm.biocomp(yc, yh, yh2o=yh2o, yash=yash, alpha=alpha, beta=beta,
                    gamma=gamma, delta=delta, epsilon=epsilon)

    splits = [alpha, beta, gamma, delta, epsilon]

st.header("Results")

# Format results for viewing on the web page
splits = [round(s, 2) for s in splits]

st.markdown(f"Using splitting parameters α = {splits[0]}, β = {splits[1]},\
    γ = {splits[2]}, δ = {splits[3]}, and ε = {splits[4]}")

d = {
    "Biomass": ["CELL", "HEMI", "LIG-C", "LIG-H", "LIG-O", "TANN", "TGL"],
    "X (daf)": [i for i in bc["x_daf"]],
    "X (wet)": [i for i in bc["x_wet"]],
    "Y (daf)": [i for i in bc["y_daf"]],
    "Y (wet)": [i for i in bc["y_wet"]],
    "Y (wetash)": [i for i in bc["y_wetash"]]
}

st.table(d)

st.space("medium")

fig = plot_biocomp(yc, yh, bc['y_rm1'], bc['y_rm2'], bc['y_rm3'])
streamlit_bokeh(fig, theme="light_minimal", key="plot")

# CSS to inject contained in a string
hide_table_row_index = """
<style>
thead tr th:first-child {display:none}
tbody th {display:none}
</style>
"""

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

