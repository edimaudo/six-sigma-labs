(function () {
  const root = document.documentElement;
  const scaleSelect = document.getElementById('type-scale');
  const themeToggle = document.getElementById('theme-toggle');

  function setScale(scale) {
    root.dataset.typeScale = scale;
    localStorage.setItem('ssol-type-scale', scale);
    if (scaleSelect) scaleSelect.value = scale;
  }

  function setTheme(theme) {
    root.dataset.theme = theme;
    localStorage.setItem('ssol-theme', theme);
    if (themeToggle) {
      const isDark = theme === 'dark';
      themeToggle.textContent = isDark ? 'Dark mode' : 'Light mode';
      themeToggle.setAttribute('aria-label', isDark ? 'Current theme: dark. Switch to light mode' : 'Current theme: light. Switch to dark mode');
      themeToggle.setAttribute('aria-pressed', String(isDark));
    }
  }

  if (scaleSelect) {
    scaleSelect.value = root.dataset.typeScale || 'medium';
    scaleSelect.addEventListener('change', (event) => setScale(event.target.value));
  }

  if (themeToggle) {
    setTheme(root.dataset.theme || 'dark');
    themeToggle.addEventListener('click', () => {
      setTheme(root.dataset.theme === 'dark' ? 'light' : 'dark');
    });
  }

  window.renderScenarioChart = function (targetId, x, y) {
    if (!window.Plotly) return;
    const styles = getComputedStyle(root);
    const bg = styles.getPropertyValue('--paper').trim();
    const fg = styles.getPropertyValue('--ink').trim();
    const grid = styles.getPropertyValue('--rule').trim();
    const blue = styles.getPropertyValue('--blue').trim();
    Plotly.purge(targetId);
    Plotly.newPlot(targetId, [{
      x, y, mode: 'lines+markers', type: 'scatter',
      line: { color: blue, width: 2 }, marker: { color: blue }
    }], {
      title: 'Illustrative process performance',
      margin: { t: 45, r: 20, b: 45, l: 50 },
      xaxis: { title: 'Observation', color: fg, gridcolor: grid },
      yaxis: { title: 'Cycle time / performance', color: fg, gridcolor: grid },
      font: { color: fg, family: 'Georgia, Times New Roman, serif' },
      paper_bgcolor: bg, plot_bgcolor: bg
    }, { responsive: true, displayModeBar: false });
  };
})();
