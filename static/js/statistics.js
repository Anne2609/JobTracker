(() => {
  const dataElement = document.getElementById('chart-data');
  if (!dataElement || !window.Chart) return;
  const data = JSON.parse(dataElement.textContent);
  const colors = ['#6c48cf', '#a98be4', '#3f98d2', '#2baf83', '#d96b82', '#98a1b2'];
  const statusCanvas = document.getElementById('statusChart');
  const monthCanvas = document.getElementById('monthlyChart');
  if (statusCanvas) {
    new Chart(statusCanvas, {
      type: 'doughnut',
      data: {labels: data.statusLabels, datasets: [{data: data.statusCounts, backgroundColor: colors, borderWidth: 2}]},
      options: {responsive: true, maintainAspectRatio: false, plugins: {legend: {position: 'bottom'}}}
    });
  }
  if (monthCanvas) {
    new Chart(monthCanvas, {
      type: 'bar',
      data: {labels: data.monthLabels, datasets: [{label: 'Candidaturi', data: data.monthCounts, backgroundColor: '#6c48cf', borderRadius: 6}]},
      options: {responsive: true, maintainAspectRatio: false, scales: {y: {beginAtZero: true, ticks: {precision: 0}}}, plugins: {legend: {display: false}}}
    });
  }
})();
