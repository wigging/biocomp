import chemics as cm
import streamlit as st
import pandas as pd
from biocomp import calc_biocomp
from plotter import plot_biocomp

# App state
# ----------------------------------------------------------------------------

if 'alpha' not in st.session_state:
    st.session_state['alpha'] = 0.6
    st.session_state['beta'] = 0.8
    st.session_state['gamma'] = 0.8
    st.session_state['delta'] = 1.0
    st.session_state['epsilon'] = 1.0

# Sidebar
# ----------------------------------------------------------------------------

st.sidebar.header('Ultimate analysis')
carb = st.sidebar.number_input('Carbon %', min_value=45.00, max_value=75.00, value=53.00, step=1.0)
hydro = st.sidebar.number_input('Hydrogen %', min_value=4.00, max_value=11.00, value=6.00, step=0.1)
h2o = st.sidebar.number_input('H₂O %', min_value=1.00, max_value=30.00, value=2.00, step=0.1)
ash = st.sidebar.number_input('ash %', min_value=1.00, max_value=30.00, value=2.00, step=0.1)

# Convert ultimate analysis percent to mass fractions
yc = carb / 100
yh = hydro / 100
yh2o = h2o / 100
yash = ash / 100

# ---

st.sidebar.header('Chemical analysis')
cell = st.sidebar.number_input('Cellulose %', min_value=20.00, max_value=70.00, value=28.98, step=0.1)
hemi = st.sidebar.number_input('Hemicellulose %', min_value=20.00, max_value=70.00, value=22.02, step=0.1)
lig = st.sidebar.number_input('Lignin %', min_value=20.00, max_value=70.00, value=36.53, step=0.1)

# Convert chemical analysis percent to mass fractions
ycell = cell / 100
yhemi = hemi / 100
ylig = lig / 100
ychem = [ycell, yhemi, ylig]

# ---

st.sidebar.header('Splitting parameters')

if st.sidebar.button('Optimize'):
    _, splits = calc_biocomp(yc, yh, ychem)
    st.session_state['alpha'] = float(splits[0])
    st.session_state['beta'] = float(splits[1])
    st.session_state['gamma'] = float(splits[2])
    st.session_state['delta'] = float(splits[3])
    st.session_state['epsilon'] = float(splits[4])

st.sidebar.slider('α', min_value=0.0, max_value=1.0, key='alpha')
st.sidebar.slider('β', min_value=0.0, max_value=1.0, key='beta')
st.sidebar.slider('γ', min_value=0.0, max_value=1.0, key='gamma')
st.sidebar.slider('δ', min_value=0.0, max_value=1.0, key='delta')
st.sidebar.slider('ε', min_value=0.0, max_value=1.0, key='epsilon')

# Content
# ----------------------------------------------------------------------------

st.title('🌳 Biomass composition tool')

st.markdown(
    """
    Estimate biomass composition based on the carbon and hydrogen fractions
    from ultimate analysis data. Use chemical analysis data to optimize the
    splitting parameters. Adjust the splitting parameter values with the
    sliders. Results are for use with the Ranzi, Debiagi, et al. kinetics
    scheme for biomass pyrolysis.
    """)

bc = cm.biocomp(yc, yh, yh2o=yh2o, yash=yash,
                alpha=st.session_state['alpha'],
                beta=st.session_state['beta'],
                gamma=st.session_state['gamma'],
                delta=st.session_state['delta'],
                epsilon=st.session_state['epsilon'])

# Plot biomass composition
# p = plot_biocomp(yc, yh, bc['y_rm1'], bc['y_rm2'], bc['y_rm3'])
# st.bokeh_chart(p)

results = {
    'x_daf': bc['x_daf'],
    'x_wet': bc['x_wet'],
    'y_daf': bc['y_daf'],
    'y_wet': bc['y_wet'],
    'y_wetash': bc['y_wetash']
}

df = pd.DataFrame(results, index=['cell', 'hemi', 'lig-c', 'lig-h', 'lig-o', 'tann', 'tgl'])
st.table(df)
