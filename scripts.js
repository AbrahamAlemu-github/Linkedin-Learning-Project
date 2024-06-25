async function checkCode() {
    const codeInput = document.getElementById('code-input').value;
    const feedback = document.getElementById('feedback');
    const instructions = "Write a Basic Java Program";  // Adjust as needed

    const response = await fetch('/evaluate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code: codeInput, instructions: instructions }),
    });

    const result = await response.json();
    feedback.textContent = `Score: ${result.score}\nFeedback: ${result.feedback}`;
    feedback.style.color = result.score >= 75 ? 'green' : 'red';
}

function validateLogin() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('error-message');
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.redirect) {
            window.location.href = data.redirect;
        } else {
            errorMessage.textContent = 'Invalid username or password';
        }
    })
    .catch(error => {
        errorMessage.textContent = 'Error: ' + error.message;
    });
}
