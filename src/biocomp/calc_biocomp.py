"""Module for biomass composition functions."""

import chemics as cm
from scipy.optimize import minimize


def calc_biocomp(form: dict[str, str]) -> tuple[float, float, dict, tuple]:
    """Calculate biomass composition using form inputs."""

    # Get parameters for calculating biomass composition
    yc = float(form["carbon"]) / 100
    yh = float(form["hydrogen"]) / 100
    yh2o = float(form["water"]) / 100
    yash = float(form["ash"]) / 100

    if "optimize" in form:
        ycell = float(form["cellulose"]) / 100
        yhemi = float(form["hemicellulose"]) / 100
        ylig = float(form["lignin"]) / 100
        ychem = (ycell, yhemi, ylig)
        bc, splits = calc_opt_biocomp(yc, yh, ychem, yh2o, yash)
    else:
        alpha = float(form["alpha"])
        beta = float(form["beta"])
        gamma = float(form["gamma"])
        delta = float(form["delta"])
        epsilon = float(form["epsilon"])

        bc = cm.biocomp(
            yc=yc,
            yh=yh,
            yh2o=yh2o,
            yash=yash,
            alpha=alpha,
            beta=beta,
            gamma=gamma,
            delta=delta,
            epsilon=epsilon,
        )

        splits = (alpha, beta, gamma, delta, epsilon)

    bc["y_rm1"] = bc["y_rm1"].tolist()
    bc["y_rm2"] = bc["y_rm2"].tolist()
    bc["y_rm3"] = bc["y_rm3"].tolist()

    return yc, yh, bc, splits


def _objfunc(x, yc, yh, ychem):
    """
    Objective function for determining the biomass composition splitting
    parameters by minimizing the difference between the estimated composition
    and the composition from chemical analysis data.

    Parameters
    ----------
    x : list
        Splitting parameter values as [α, β, γ, δ, ε]
    yc : float
        Mass fraction of carbon from ultimate analysis CHO basis
    yh : float
        Mass fraction of hydrogen from ultimate analysis CHO basis
    ychem : ndarray
        Mass fractions of chemical analysis data for [cellulose, hemicellulose, lignin]

    Returns
    -------
    float
        Value returned from ∑(y - z)² where y is cell, hemi, total lig
        estimated from biomass composition and z is cell, hemi, lig from
        chemical analysis data.

    Note
    ----
    Default splitting parameters are α = 0.6, β = 0.8, γ = 0.8, δ = 1, ε = 1.
    """
    alpha, beta, gamma, delta, epsilon = x
    ycell_data, yhemi_data, ylig_data = ychem

    bc = cm.biocomp(yc, yh, alpha=alpha, beta=beta, gamma=gamma, delta=delta, epsilon=epsilon)
    ycell, yhemi, yligc, yligh, yligo, _, _ = bc["y_daf"]
    ylig = yligc + yligh + yligo

    return (ycell - ycell_data) ** 2 + (yhemi - yhemi_data) ** 2 + (ylig - ylig_data) ** 2


def calc_opt_biocomp(yc, yh, ychem, yh2o, yash):
    """
    Calculate the optimized splitting parameters and associated biomass
    composition of the feedstock.

    Parameters
    ----------
    yc : float
        Mass fraction of carbon from ultimate analysis CHO basis
    yh : float
        Mass fraction of hydrogen from ultimate analysis CHO basis
    ychem : ndarray
        Mass fractions of chemical analysis data for [cellulose, hemicellulose, lignin]
    yh2o : float
        Mass fraction of water in biomass, as received basis [-]
    yash : float
        Mass fraction of ash in biomass, as received basis [-]

    Returns
    -------
    bc : dict
        Reference mixtures and biomass compositions on the basis of mole
        fractions (x) and mass fractions (y). See Chemics `biocomp()` docs
        for more information.
    splits : list
        Optimized splitting parameter values as [α, β, γ, δ, ε]
    """

    # Determine optimized splitting parameters using default values for `x0`
    # where each parameter is bound within 0 to 1
    x0 = [0.6, 0.8, 0.8, 1, 1]
    bnds = ((0, 1), (0, 1), (0, 1), (0, 1), (0, 1))
    res = minimize(_objfunc, x0, args=(yc, yh, ychem), method="L-BFGS-B", bounds=bnds)

    # Calculate biomass composition using optimized splitting parameters, water, and ash
    bc = cm.biocomp(
        yc,
        yh,
        yh2o=yh2o,
        yash=yash,
        alpha=res.x[0],
        beta=res.x[1],
        gamma=res.x[2],
        delta=res.x[3],
        epsilon=res.x[4],
    )

    # Optimized splitting parameters in order of [alpha, beta, gamma, delta, epsilon]
    splits = tuple([round(i, 2) for i in res.x])

    return bc, splits
