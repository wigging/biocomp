import chemics as cm
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from calc_biocomp import calc_biocomp

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

st.sidebar.header('Chemical analysis')
cell = st.sidebar.number_input('Cellulose %', min_value=20.00, max_value=70.00, value=28.98, step=0.1)
hemi = st.sidebar.number_input('Hemicellulose %', min_value=20.00, max_value=70.00, value=22.02, step=0.1)
lig = st.sidebar.number_input('Lignin %', min_value=20.00, max_value=70.00, value=36.53, step=0.1)

# Convert chemical analysis percent to mass fractions
ycell = cell / 100
yhemi = hemi / 100
ylig = lig / 100
ychem = [ycell, yhemi, ylig]

st.sidebar.header('Splitting parameters')
optimize = st.sidebar.button('Optimize')

if not optimize:
    alpha = st.sidebar.slider('α', 0.0, 1.0, 0.6)
    beta = st.sidebar.slider('β', 0.0, 1.0, 0.8)
    gamma = st.sidebar.slider('γ', 0.0, 1.0, 0.8)
    delta = st.sidebar.slider('δ', 0.0, 1.0, 1.0)
    epsilon = st.sidebar.slider('ε', 0.0, 1.0, 1.0)
    bc = cm.biocomp(yc, yh, yh2o=yh2o, yash=yash, alpha=alpha, beta=beta, gamma=gamma, delta=delta, epsilon=epsilon)

if optimize:
    bc, splits = calc_biocomp(yc, yh, ychem)
    alpha = st.sidebar.slider('α', 0.0, 1.0, float(splits[0]))
    beta = st.sidebar.slider('β', 0.0, 1.0, float(splits[1]))
    gamma = st.sidebar.slider('γ', 0.0, 1.0, float(splits[2]))
    delta = st.sidebar.slider('δ', 0.0, 1.0, float(splits[3]))
    epsilon = st.sidebar.slider('ε', 0.0, 1.0, float(splits[4]))

# Content
# ----------------------------------------------------------------------------

st.title('Biomass composition')

st.markdown(
    'Estimate biomass composition based on the carbon and hydrogen fractions \
    from ultimate analysis data. Adjust the splitting parameter values with the sliders.'
)

col1, _ = st.columns([2, 1])

with col1:
    # Plot biomass composition
    fig, ax = plt.subplots()
    cm.plot_biocomp(ax, yc, yh, bc['y_rm1'], bc['y_rm2'], bc['y_rm3'])
    st.pyplot(fig)

results = {
    'x_daf': bc['x_daf'],
    'x_wet': bc['x_wet'],
    'y_daf': bc['y_daf'],
    'y_wet': bc['y_wet'],
    'y_wetash': bc['y_wetash']
}
df = pd.DataFrame(results, index=['cell', 'hemi', 'lig-c', 'lig-h', 'lig-o', 'tann', 'tgl'])
st.table(df)
