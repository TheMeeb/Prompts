document.getElementById('signupForm')?.addEventListener('submit', function(e) {
    const password = document.getElementById('password').value;
    const confirm = document.querySelector('input[name="confirm"]').value;
    if (password !== confirm) {
        alert('Passwords do not match!');
        e.preventDefault();
    }
});
