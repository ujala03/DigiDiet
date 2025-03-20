const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());
app.use(express.static('public')); // Serve static files

// Dummy user profile API
app.get('/api/profile', (req, res) => {
    res.json({
        name: "John Doe",
        age: 30,
        height: "170 cm",
        weight: "70 kg",
        condition: "Diabetic"
    });
});

// Dummy food log API
app.get('/api/food-log', (req, res) => {
    res.json([
        { food: "Rice", calories: 200 },
        { food: "Chicken", calories: 300 },
        { food: "Salad", calories: 150 }
    ]);
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
