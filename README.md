# Biomass composition

This is a web tool for estimating biomass composition from ultimate analysis data. The code is based on the biomass characterization method discussed in the papers referenced below. The composition is for use with the Ranzi, Debiagi, et al. biomass pyrolysis kinetics scheme.

View the web tool at https://share.streamlit.io/wigging/biocomp/main/app.py

## Installation

Download or clone this repository then create and activate the Python virtual environment. Install the dependencies using `pip` then run the web app using `streamlit`. The app should automatically appear in your web browser.

```bash
# Create and activate the Python virtual environment
$ python -v venv venv
$ source venv/bin/activate

# Install the dependencies
(venv) $ pip install -r requirements.txt

# Run the web app
(venv) $ streamlit run app.py
```

## Usage

Run the app locally or use the web version. Once the app is running, enter ultimate and chemical analysis data in the parameters column on the left sidebar. Click the Optimize button to estimate the splitting parameters. Use the sliders to further adjust the splitting parameters. Results are shown to the right of the sidebar.

## Citation

To cite this work, use the "Cite this repository" feature available on the right side of this repository page or use the reference text given below.

> Gavin Wiggins. Biocomp: A biomass composition tool. Available at https://github.com/wigging/biocomp.

## References

Paulo Debiagi, Chiara Pecchi, Giancarlo Gentile, Alessio Frassoldati, Alberto Cuoci, Tiziano Faravelli, and Eliseo Ranzi. "Extractives Extend the Applicability of Multistep Kinetic Scheme of Biomass Pyrolysis." Energy & Fuels, vol. 29, no. 10, pp. 6544-6555, 2015.

Paulo Debiagi, Giancarlo Gentile, Alberto Cuoci, Alessio Frassoldati, Eliseo Ranzi, Tiziano Faravelli. "A predictive model of biochar formation and characterization." Journal of Analytical and Applied Pyrolysis, vol. 134, pp. 326-335, 2018.
