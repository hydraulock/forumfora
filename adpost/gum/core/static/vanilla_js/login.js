
    // Get references to the form and input fields
    const form = document.querySelector('form');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');

    // Function to check and apply the 'is-invalid' class based on error message
    function handleValidation() {
        const errorMessageElement = document.querySelector('.alert-danger');
        if (errorMessageElement) {
            const errorMessage = errorMessageElement.textContent.trim();

            if (errorMessage.includes('Email incorrect')) {
                emailInput.classList.add('is-invalid');
            } else if (errorMessage.includes('Mot de passe incorrect')) {
                passwordInput.classList.add('is-invalid');
            }
        }
    }

    // Add an event listener to the form for form submission
    form.addEventListener('submit', (event) => {
        handleValidation();
        if (form.querySelector('.is-invalid')) {
            event.preventDefault(); // Prevent form submission if there are invalid fields
        }
    });

    // Call the handleValidation function initially
    handleValidation();

    // Add event listeners to remove the 'is-invalid' class when the user starts typing
    emailInput.addEventListener('input', () => {
        emailInput.classList.remove('is-invalid');
    });

    passwordInput.addEventListener('input', () => {
        passwordInput.classList.remove('is-invalid');
    });

