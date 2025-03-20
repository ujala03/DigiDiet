const fileInput = document.getElementById('fileInput');
const imagePreview = document.getElementById('imagePreview');

// Preview the image when selected
fileInput.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        imagePreview.querySelector('span').classList.add('hidden');
        const img = imagePreview.querySelector('img');
        img.classList.remove('hidden');

        reader.addEventListener('load', function () {
            img.setAttribute('src', this.result);
        });

        reader.readAsDataURL(file);
    }
});

// Placeholder function for image upload
function uploadImage() {
    const file = fileInput.files[0];
    if (!file) {
        alert('Please select an image first!');
        return;
    }

    alert('Image ready to upload for analysis (Demo)');
    console.log('File to be uploaded:', file);

    // Example API integration placeholder
    // const formData = new FormData();
    // formData.append('foodImage', file);
    // fetch('/api/upload', {
    //     method: 'POST',
    //     body: formData
    // }).then(res => res.json()).then(data => console.log(data));
}