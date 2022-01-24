from flask import Flask
from flask import render_template
from flask import request
from biocomp import calc_biocomp
import chemics as cm

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():

    # Get ultimate analysis values
    carb = float(request.form['carbon'])
    hydro = float(request.form['hydrogen'])
    h2o = float(request.form['water'])
    ash = float(request.form['ash'])

    # Get chemical analysis values
    cell = float(request.form['cellulose'])
    hemi = float(request.form['hemicellulose'])
    lig = float(request.form['lignin'])

    # Get splitting parameter values
    alpha = float(request.form['alpha'])
    beta = float(request.form['beta'])
    gamma = float(request.form['gamma'])
    delta = float(request.form['delta'])
    epsilon = float(request.form['epsilon'])

    # Get state of the optimize checkbox
    opt = request.form.get('optimize')
    if opt is None:
        optimize = False
    else:
        optimize = True

    # Convert ultimate analysis percent to mass fractions
    yc = carb / 100
    yh = hydro / 100
    yh2o = h2o / 100
    yash = ash / 100

    # Convert chemical analysis percent to mass fractions
    ycell = cell / 100
    yhemi = hemi / 100
    ylig = lig / 100
    ychem = [ycell, yhemi, ylig]

    # Calculate optimized splitting parameters
    _, splits = calc_biocomp(yc, yh, ychem)

    # Calculate biomass composition using optimized splitting parameters, water, and ash
    bc = cm.biocomp(yc, yh, yh2o=yh2o, yash=yash, alpha=splits[0], beta=splits[1],
                    gamma=splits[2], delta=splits[3], epsilon=splits[4])

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
