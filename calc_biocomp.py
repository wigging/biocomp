import chemics as cm
import numpy as np
from objfunc import objfunc
from scipy.optimize import minimize


def calc_biocomp(yc, yh, ychem):
    """
    Calculate the optimized splitting parameters and associated biomass
    composition (daf) of the feedstock.
    """

    # Get mass fractions for ultimate analysis data
    # Get mass fractions of biomass composition from chemical analysis data
    # yc = self.ult_cho[0] / 100
    # yh = self.ult_cho[1] / 100
    # ybc = self.chem_bc / 100

    # Determine optimized splitting parameters using default values for `x0`
    # where each parameter is bound within 0 to 1
    x0 = [0.6, 0.8, 0.8, 1, 1]
    bnds = ((0, 1), (0, 1), (0, 1), (0, 1), (0, 1))
    res = minimize(objfunc, x0, args=(yc, yh, ychem), method='L-BFGS-B', bounds=bnds)

    # Calculate biomass composition as dry ash-free basis (daf)
    bc = cm.biocomp(yc, yh, alpha=res.x[0], beta=res.x[1], gamma=res.x[2], delta=res.x[3], epsilon=res.x[4])
    cell, hemi, ligc, ligh, ligo, tann, tgl = bc['y_daf']

    # Optimized splitting parameters in order of [alpha, beta, gamma, delta, epsilon]
    splits = np.array([res.x[0], res.x[1], res.x[2], res.x[3], res.x[4]])

    return bc, splits
