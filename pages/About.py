import streamlit as st

st.title("About")

p = """
<p>BioComp is a web tool for estimating biomass composition using ultimate and chemical analysis data. Calculations are based on the biomass characterization method discussed in the Debiagi, Ranzi, et al. papers listed below. Also, see the <a href="https://chemics.readthedocs.io/en/latest/biomass_composition.html">documentation</a> for the Chemics biocomp() function for implementation details of the characterization procedure.

<p>The BioComp source code is available on <a href="https://github.com/wigging/biocomp">GitHub</a>. Submit a Pull Request if you would like to contribute to the project. Questions and other comments can be submitted on the GitHub <a href="https://github.com/wigging/pythonic/issues">Issues</a> page. You can also contact Gavin Wiggins via <a href="mailto:wiggingATmeDOTcom" onclick="this.href=this.href.replace(/AT/,'&#64;').replace(/DOT/,'&#46;')">Email</a> or <a href="https://twitter.com/wigging">Twitter</a>.</p>

<h2>References</h2>

<p>Paulo Debiagi, Chiara Pecchi, Giancarlo Gentile, Alessio Frassoldati, Alberto Cuoci, Tiziano Faravelli, and Eliseo Ranzi. <a href="https://doi.org/10.1021/acs.energyfuels.5b01753">Extractives Extend the Applicability of Multistep Kinetic Scheme of Biomass Pyrolysis.</a> Energy & Fuels, vol. 29, no. 10, pp. 6544-6555, 2015.</p>

<p>Paulo Debiagi, Giancarlo Gentile, Alberto Cuoci, Alessio Frassoldati, Eliseo Ranzi, Tiziano Faravelli. <a href="https://doi.org/10.1016/j.jaap.2018.06.022">A predictive model of biochar formation and characterization.</a> Journal of Analytical and Applied Pyrolysis, vol. 134, pp. 326-335, 2018.</p>
"""

st.write(p, unsafe_allow_html=True)
