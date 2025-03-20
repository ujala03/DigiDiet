const ctx = document.getElementById('nutritionChart').getContext('2d');
const nutritionChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Calories', 'Carbs', 'Proteins', 'Fats'],
        datasets: [{
            label: 'Today\'s Intake',
            data: [2000, 250, 70, 60], // Example data
            backgroundColor: ['#ff6384', '#36a2eb', '#ffcd56', '#4bc0c0']
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
