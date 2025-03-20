function login() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (!email || !password) {
        alert("Please enter both email and password.");
        return;
    }

    //  For demo, we are accepting any email/password (later connect to backend)
    // Save login status
    localStorage.setItem('isLoggedIn', 'true');
    localStorage.setItem('userEmail', email); // Optional: Store email for personalized greeting

    alert("Login Successful!");

    //  Redirect to dashboard
    window.location.href = 'dashboard.html'; // Adjust if dashboard page has different name
}
