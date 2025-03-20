const fileInput = document.getElementById('fileInput');
const imagePreview = document.getElementById('imagePreview');
const resultsSection = document.getElementById('results');

// Image preview when selected
fileInput.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        const img = imagePreview.querySelector('img');
        imagePreview.querySelector('span').classList.add('hidden');
        img.classList.remove('hidden');

        reader.onload = function (e) {
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});

// Simulated Food Analysis
function analyzeFood() {
    const file = fileInput.files[0];
    if (!file) {
        alert('Please select an image first!');
        return;
    }

    // Simulating food analysis result (you can replace this with real API response)
    document.getElementById('calories').innerText = '712';
    document.getElementById('protein').innerText = '25g';
    document.getElementById('carbs').innerText = '33g';
    document.getElementById('fiber').innerText = '2g';

    // Show result section
    resultsSection.classList.remove('hidden');
}