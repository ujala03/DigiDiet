function submitForm() {
    const fullName = document.getElementById('fullName').value;
    const age = document.getElementById('age').value;
    const mealPreference = document.getElementById('mealPreference').value;
    const height = document.getElementById('height').value;
    const weight = document.getElementById('weight').value;

    if (!fullName || !age || !mealPreference || !height || !weight) {
        alert("Please fill all fields.");
        return;
    }

    const data = {
        fullName,
        age,
        mealPreference,
        height,
        weight
    };

    console.log("User Data: ", data);
    alert("Profile saved successfully!");

    // You can send data to backend using fetch() if needed
    // fetch('/api/saveProfile', {
    //     method: 'POST',
    //     headers: { 'Content-Type': 'application/json' },
    //     body: JSON.stringify(data)
    // }).then(response => response.json()).then(data => console.log(data));
}