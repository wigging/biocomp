import chemics as cm
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Sidebar
# ----------------------------------------------------------------------------

st.sidebar.header('Parameters')

yc = st.sidebar.number_input('Carbon', min_value=0.45, max_value=0.75, value=0.53)
yh = st.sidebar.number_input('Hydrogen', min_value=0.04, max_value=0.11, value=0.06, step=0.001, format='%f')
yh2o = st.sidebar.number_input('H₂O', min_value=0.01, max_value=0.30, value=0.02)
yash = st.sidebar.number_input('ash', min_value=0.01, max_value=0.30, value=0.02)

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
