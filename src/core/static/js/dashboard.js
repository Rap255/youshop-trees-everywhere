document.addEventListener('DOMContentLoaded', function () {
  const ctx = document.getElementById('treeChart').getContext('2d');

  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Oak', 'Maple', 'Pine', 'Other'],
      datasets: [{
        label: 'Tree Types',
        data: [12, 8, 5, 3],
        backgroundColor: [
          '#81c784',
          '#66bb6a',
          '#4caf50',
          '#388e3c'
        ],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'right'
        }
      }
    }
  });
});
