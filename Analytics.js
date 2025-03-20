// Simulated Nutritional Data fetched from cloud backend
const nutritionData = {
    calories: 2200,
    protein: 75,
    fats: 65,
    fibres: 30,
    carbs: 280
};

// Update Card Values
document.getElementById('caloriesValue').innerText = nutritionData.calories;
document.getElementById('proteinValue').innerText = nutritionData.protein;
document.getElementById('fatsValue').innerText = nutritionData.fats;
document.getElementById('fibresValue').innerText = nutritionData.fibres;
document.getElementById('carbsValue').innerText = nutritionData.carbs;

// Chart.js to display nutritional data
const ctx = document.getElementById('nutritionChart').getContext('2d');
const nutritionChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Calories (kcal)', 'Protein (g)', 'Fats (g)', 'Fibres (g)', 'Carbs (g)'],
        datasets: [{
            label: 'Daily Intake',
            data: [
                nutritionData.calories,
                nutritionData.protein,
                nutritionData.fats,
                nutritionData.fibres,
                nutritionData.carbs
            ],
            backgroundColor: [
                'rgba(229, 57, 53, 0.8)',
                'rgba(67, 160, 71, 0.8)',
                'rgba(251, 192, 45, 0.8)',
                'rgba(102, 187, 106, 0.8)',
                'rgba(30, 136, 229, 0.8)'
            ],
            borderColor: [
                'rgba(229, 57, 53, 1)',
                'rgba(67, 160, 71, 1)',
                'rgba(251, 192, 45, 1)',
                'rgba(102, 187, 106, 1)',
                'rgba(30, 136, 229, 1)'
            ],
            borderWidth: 1
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
