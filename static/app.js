function renderScenarioChart(targetId, x, y) {
  if (!window.Plotly) return;
  Plotly.newPlot(targetId, [{
    x, y, mode: 'lines+markers', type: 'scatter',
    line: { color: '#0f62fe', width: 2 }, marker: { color: '#0f62fe' }
  }], {
    title: 'Illustrative process performance',
    margin: { t: 45, r: 20, b: 45, l: 50 },
    xaxis: { title: 'Observation' },
    yaxis: { title: 'Cycle time / performance' },
    paper_bgcolor: '#ffffff', plot_bgcolor: '#ffffff'
  }, { responsive: true, displayModeBar: false });
}
