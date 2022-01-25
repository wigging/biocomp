from flask import Flask
from flask import render_template
from flask import request
from biocomp import calc_opt_biocomp
import chemics as cm

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():

    # Get ultimate analysis values and convert to mass fractions
    carb = float(request.form['carbon'])
    hydro = float(request.form['hydrogen'])
    h2o = float(request.form['water'])
    ash = float(request.form['ash'])

    yc = carb / 100
    yh = hydro / 100
    yh2o = h2o / 100
    yash = ash / 100

    # Get chemical analysis values and convert to percent mass fractions
    cell = float(request.form['cellulose'])
    hemi = float(request.form['hemicellulose'])
    lig = float(request.form['lignin'])

    ycell = cell / 100
    yhemi = hemi / 100
    ylig = lig / 100
    ychem = [ycell, yhemi, ylig]

    # Get splitting parameter values
    alpha = float(request.form['alpha'])
    beta = float(request.form['beta'])
    gamma = float(request.form['gamma'])
    delta = float(request.form['delta'])
    epsilon = float(request.form['epsilon'])

    # Get state of the optimize checkbox
    if request.form.get('optimize') is None:
        optimize = False

        # Biomass composition using given splitting parameters
        bc = cm.biocomp(yc, yh, yh2o=yh2o, yash=yash, alpha=alpha, beta=beta,
                        gamma=gamma, delta=delta, epsilon=epsilon)
        splits = [alpha, beta, gamma, delta, epsilon]
    else:
        optimize = True

        # Biomass composition using optimized splitting parameters
        bc, splits = calc_opt_biocomp(yc, yh, ychem, yh2o, yash)

    # Format results for viewing on the web page
    splits = [round(s, 2) for s in splits]

    biocomp = {
        'xdaf': [round(x, 2) for x in bc['x_daf']],
        'xwet': [round(x, 2) for x in bc['x_wet']],
        'ydaf': [round(x, 2) for x in bc['y_daf']],
        'ywet': [round(x, 2) for x in bc['y_wet']],
        'ywetash': [round(x, 2) for x in bc['y_wetash']]
    }

    return render_template('results.html', splits=splits, biocomp=biocomp, optimize=optimize)
