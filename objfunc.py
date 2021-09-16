import chemics as cm


def objfunc(x, yc, yh, ychem):
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
    ycell, yhemi, yligc, yligh, yligo, _, _ = bc['y_daf']
    ylig = yligc + yligh + yligo

    return (ycell - ycell_data)**2 + (yhemi - yhemi_data)**2 + (ylig - ylig_data)**2
