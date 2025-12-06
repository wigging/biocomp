# 🌳 BioComp

BioComp is a web tool for estimating biomass composition from ultimate and chemical analysis data. The code is based on the biomass characterization method discussed in the Ranzi, Debiagi, et al. papers referenced below. The composition is for use with the Ranzi, Debiagi, et al. biomass pyrolysis kinetics scheme.

View the BioComp web tool at https://biocomptool.streamlit.app

## Installation

To install BioComp locally on your computer, first install uv using the instructions at https://docs.astral.sh/uv. Next, clone this repository, then create a Python environment and install the dependencies using the uv sync command as shown below.

```bash
cd biocomp
uv sync
```

## Usage

Run BioComp locally using the uv command shown below.

```bash
uv run streamlit run src/app.py
```

Or go to https://biocomptool.streamlit.app to use it on Streamlit Cloud. See the [Usage page](https://biocomptool.streamlit.app/Usage) for more information about using BioComp.

## Citation

To cite this work, use the "Cite this repository" feature available on the right side of this repository page or use the reference text given below.

> Gavin Wiggins. BioComp: A web tool for estimating biomass composition. Version 25.12. Available at https://github.com/wigging/biocomp.

## References

References that were used for calculating the biomass composition are listed below.

- Paulo Debiagi, Chiara Pecchi, Giancarlo Gentile, Alessio Frassoldati, Alberto Cuoci, Tiziano Faravelli, and Eliseo Ranzi. "Extractives Extend the Applicability of Multistep Kinetic Scheme of Biomass Pyrolysis." Energy & Fuels, vol. 29, no. 10, pp. 6544-6555, 2015.
- Paulo Debiagi, Giancarlo Gentile, Alberto Cuoci, Alessio Frassoldati, Eliseo Ranzi, Tiziano Faravelli. "A predictive model of biochar formation and characterization." Journal of Analytical and Applied Pyrolysis, vol. 134, pp. 326-335, 2018.
