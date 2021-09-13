import chemics as cm
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Sidebar
# ----------------------------------------------------------------------------

st.sidebar.header('Ultimate analysis')

yc = st.sidebar.number_input('Carbon %', min_value=45.00, max_value=75.00, value=53.00, step=1.0)
yh = st.sidebar.number_input('Hydrogen %', min_value=4.00, max_value=11.00, value=6.00, step=0.1)
yh2o = st.sidebar.number_input('H₂O %', min_value=1.00, max_value=30.00, value=2.00, step=0.1)
yash = st.sidebar.number_input('ash %', min_value=1.00, max_value=30.00, value=2.00, step=0.1)

st.sidebar.header('Splitting parameters')

st.sidebar.button('Optimize')

alpha = st.sidebar.slider('α', 0.0, 1.0, 0.6)
beta = st.sidebar.slider('β', 0.0, 1.0, 0.8)
gamma = st.sidebar.slider('γ', 0.0, 1.0, 0.8)
delta = st.sidebar.slider('δ', 0.0, 1.0, 1.0)
epsilon = st.sidebar.slider('ε', 0.0, 1.0, 1.0)

# Content
# ----------------------------------------------------------------------------

st.title('Biomass composition')

st.markdown(
    'Estimate biomass composition based on the carbon and hydrogen fractions \
    from ultimate analysis data. Adjust the splitting parameter values with the sliders.'
)

col1, _ = st.columns([2, 1])

with col1:
    # Convert mass percent to mass fraction
    yc = yc / 100
    yh = yh / 100
    yh2o = yh2o / 100
    yash = yash / 100

    # Plot biomass composition
    bc = cm.biocomp(yc, yh, yh2o=yh2o, yash=yash, alpha=alpha, beta=beta, gamma=gamma, delta=delta, epsilon=epsilon)
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
