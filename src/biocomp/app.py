"""Module for the Quart web application.

Run the Quart web app with
uv run quart --app src/biocomp2/app.py run
"""

from quart import Quart, render_template, request

import importlib.metadata

from .calc_biocomp import calc_biocomp

app = Quart(__name__)


@app.context_processor
def biocomp_version():
    return {"version": importlib.metadata.version("biocomp")}


@app.get("/")
async def index():
    return await render_template("index.html")


@app.get("/about")
async def about():
    return await render_template("about.html")


@app.get("/usage")
async def usage():
    return await render_template("usage.html")


@app.post("/params")
async def params():
    form = await request.form
    yc, yh, bc, splits = calc_biocomp(form)
    return await render_template("results.html", yc=yc, yh=yh, bc=bc, splits=splits)
