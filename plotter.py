from bokeh.models import Label, PolyAnnotation
from bokeh.plotting import figure


def plot_biocomp(yc, yh, yrm1, yrm2, yrm3):
    """
    Plot the biomass composition using Bokeh.

    Parameters
    ----------
    yc : float
        Mass fraction of carbon in biomass, dry ash free basis [-].
    yh : float
         Mass fraction of hydrogen in biomass, dry ash free basis [-].
    yrm1 : list
        Mass fractions [C, H, O] of reference mixture RM1.
    yrm2 : list
        Mass fractions [C, H, O] of reference mixture RM2.
    yrm3 : list
        Mass fractions [C, H, O] of reference mixture RM3.

    Returns
    -------
    p : bokeh.Figure
        A Bokeh plotting figure.
    """
    p = figure(
        x_axis_label='Carbon mass fraction, daf basis [-]',
        y_axis_label='Hydrogen mass fraction, daf basis [-]',
        max_height=400,
        height_policy='max')

    p.triangle(yc, yh, color='blueviolet', size=10, legend_label='biomass')

    p.square(yrm1[0], yrm1[1], color='goldenrod', size=8, legend_label='rm1')
    p.square(yrm2[0], yrm2[1], color='limegreen', size=8, legend_label='rm2')
    p.square(yrm3[0], yrm3[1], color='indianred', size=8, legend_label='rm3')

    p.line(
        [yrm1[0], yrm2[0], yrm3[0], yrm1[0]],
        [yrm1[1], yrm2[1], yrm3[1], yrm1[1]],
        color='black',
        line_width=2,
        line_dash='dotted')

    p.circle(0.4444, 0.0617, size=8)
    cell = Label(x=0.4444, y=0.0617, x_offset=-10, y_offset=6, text='cell')
    p.add_layout(cell)

    p.circle(0.4545, 0.0606, size=8)
    hemi = Label(x=0.4545, y=0.0606, x_offset=-14, y_offset=-20, text='hemi')
    p.add_layout(hemi)

    p.circle(0.6977, 0.0543, size=8)
    ligc = Label(x=0.6977, y=0.0543, x_offset=-14, y_offset=-20, text='ligc')
    p.add_layout(ligc)

    p.circle(0.6055, 0.0642, size=8)
    ligh = Label(x=0.6055, y=0.0642, x_offset=-14, y_offset=6, text='ligh')
    p.add_layout(ligh)

    p.circle(0.5687, 0.0521, size=8)
    ligo = Label(x=0.5687, y=0.0521, x_offset=-14, y_offset=-20, text='ligo')
    p.add_layout(ligo)

    p.circle(0.5921, 0.0395, size=8)
    tann = Label(x=0.5921, y=0.0395, x_offset=-14, y_offset=-20, text='tann')
    p.add_layout(tann)

    p.circle(0.7634, 0.1116, size=8)
    tgl = Label(x=0.7634, y=0.1116, x_offset=-8, y_offset=-20, text='tgl')
    p.add_layout(tgl)

    polygon = PolyAnnotation(
        fill_color='gray',
        fill_alpha=0.2,
        xs=[0.4444, 0.5921, 0.6977, 0.7634],
        ys=[0.0617, 0.0395, 0.0543, 0.1116])
    p.add_layout(polygon)

    p.legend.location = 'top_left'

    return p
