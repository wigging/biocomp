import streamlit as st

st.title("Usage")

p = """
<p>A description of the input parameters are given below. The ultimate and chemical analysis parameters refer to measured data for a particular biomass feedstock. The only required parameters for BioComp are carbon and hydrogen from ultimate analysis data. However, it is recommended to provide as much of the parameters as possible for best results.</p>

<strong>Ultimate analysis</strong>
<ul>
    <li>Carbon % - mass percent of carbon (C), dry ash-free basis </li>
    <li>Hydrogen % - mass percent of hydrogen (H), dry ash-free basis</li>
    <li>H₂O % - mass percent of water, as received basis</li>
    <li>Ash % - mass percent of ash, as received basis</li>
</ul>

<strong>Chemical analysis</strong>
<ul>
    <li>Cellulose % - mass percent of cellulose (CELL), dry ash-free basis</li>
    <li>Hemicellulose % - mass percent of hemicellulose (HEMI), dry ash-free basis</li>
    <li>Lignin % - mass percent of total lignin, dry ash-free basis</li>
</ul>

<strong>Splitting parameters</strong>
<ul>
    <li>α - molar ratio of cellulose and hemicellulose</li>
    <li>β - molar ratio of lignin LIG-O and lignin LIG-C </li>
    <li>γ - molar ratio of lignin LIG-H and lignin LIG-C</li>
    <li>δ - molar ratio of lignins (LIG-H and LIG-C) and extractive TGL</li>
    <li>ε - molar ratio of lignins (LIG-O and LIG-C) and extractive TANN</li>
</ul>

<strong>Optimize</strong>
<ul>
    <li>If selected, optimized splitting parameters are determined using the given ultimate and chemical analysis values. The biomass composition is determined using the optimized splitting parameters.</li>
    <li>If not selected, the biomass composition is calculated using the given or default splitting parameter values.</li>
</ul>

<p>The calculated results will automatically update when the input parameters are changed.</p>
"""

st.write(p, unsafe_allow_html=True)
