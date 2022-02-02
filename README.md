# 🌳 BioComp

BioComp is a web tool for estimating biomass composition from ultimate and chemical analysis data. The code is based on the biomass characterization method discussed in the Ranzi, Debiagi, et al. papers referenced below. The composition is for use with the Ranzi, Debiagi, et al. biomass pyrolysis kinetics scheme.

View the web tool at https://biocomp.herokuapp.com

## Local installation

To install BioComp on your local machine, download or clone this repository then create and activate a Python virtual environment. Install the dependencies using `pip` then run the Flask web app using `flask run`. See the terminal commands below.

```bash
# Create and activate the Python virtual environment
$ python -m venv venv
$ source venv/bin/activate

# Install the dependencies
(venv) $ pip install -r requirements.txt

# Run the web app
(venv) $ flask run
```

## Usage

See the [Usage page](https://biocomp.herokuapp.com/usage) for information about using BioComp.

## Citation

To cite this work, use the "Cite this repository" feature available on the right side of this repository page or use the reference text given below.

> Gavin Wiggins. BioComp: A web tool for estimating biomass composition. Version 22.02. Available at https://github.com/wigging/biocomp.

## References

Paulo Debiagi, Chiara Pecchi, Giancarlo Gentile, Alessio Frassoldati, Alberto Cuoci, Tiziano Faravelli, and Eliseo Ranzi. "Extractives Extend the Applicability of Multistep Kinetic Scheme of Biomass Pyrolysis." Energy & Fuels, vol. 29, no. 10, pp. 6544-6555, 2015.

Paulo Debiagi, Giancarlo Gentile, Alberto Cuoci, Alessio Frassoldati, Eliseo Ranzi, Tiziano Faravelli. "A predictive model of biochar formation and characterization." Journal of Analytical and Applied Pyrolysis, vol. 134, pp. 326-335, 2018.
