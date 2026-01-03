// Functions for creating the biomass composition graph with Plotly.

let graphExists = false;

function newGraph(yc, yh, rm1, rm2, rm3) {
  const trace1 = {
    x: [0.4444, 0.5921, 0.6977, 0.7634],
    y: [0.0617, 0.0395, 0.0543, 0.1116],
    name: "Biomass Region",
    mode: "markers+text",
    type: "scatter",
    text: ["cell", "tann", "ligc", "tgl"],
    textposition: ["top", "bottom", "bottom", "right"],
    fill: "toself",
  };

  const trace2 = {
    x: [0.4545, 0.5687, 0.6055],
    y: [0.0606, 0.0521, 0.0642],
    mode: "markers+text",
    type: "scatter",
    text: ["hemi", "ligo", "ligh"],
    textposition: ["bottom", "bottom", "top"],
    showlegend: false,
  };

  const trace3 = {
    x: [rm1[0], rm2[0], rm3[0], rm1[0]],
    y: [rm1[1], rm2[1], rm3[1], rm1[1]],
    name: "Reference Region",
    mode: "lines",
    type: "scatter",
    line: {
      color: "black",
      dash: "dot",
    },
  };

  const trace4 = {
    x: [yc],
    y: [yh],
    name: "Biomass",
    type: "scatter",
    mode: "markers",
    marker: {
      size: 8,
      symbol: "x",
    },
  };

  const layout = {
    font: {
      size: 13,
    },
    xaxis: {
      title: {
        text: "Carbon, daf basis [-]",
      },
    },
    yaxis: {
      title: {
        text: "Hydrogen, daf basis [-]",
      },
    },
    margin: {
      b: 40,
      l: 70,
      r: 0,
      t: 20,
    },
    legend: {
      x: 0.05,
      y: 0.99,
      xanchor: "left",
      yanchor: "top",
    },
  };

  const config = { responsive: true };

  Plotly.newPlot("graph", [trace1, trace2, trace3, trace4], layout, config);
}

function updateGraph(yc, yh, rm1, rm2, rm3) {
  const update = {
    x: [[rm1[0], rm2[0], rm3[0], rm1[0]], [yc]],
    y: [[rm1[1], rm2[1], rm3[1], rm1[1]], [yh]],
  };

  Plotly.restyle("graph", update, [2, 3]);
}

htmx.on("htmx:afterSwap", () => {
  const resultsDiv = document.getElementById("results");

  const yc = JSON.parse(resultsDiv.dataset.yc);
  const yh = JSON.parse(resultsDiv.dataset.yh);
  const rm1 = JSON.parse(resultsDiv.dataset.rm1);
  const rm2 = JSON.parse(resultsDiv.dataset.rm2);
  const rm3 = JSON.parse(resultsDiv.dataset.rm3);

  if (!graphExists) {
    console.log("Graph does not exist. Create new graph.");
    newGraph(yc, yh, rm1, rm2, rm3);
    graphExists = true;
  } else {
    console.log("Graph already exists. Update existing graph.");
    updateGraph(yc, yh, rm1, rm2, rm3);
  }
});
