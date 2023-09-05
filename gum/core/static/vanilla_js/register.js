
    // Get references to the form and input fields
    const form = document.querySelector('form');
    const emailInput = document.getElementById('email');
    const usernameInput = document.getElementById('username');
    const phoneInput = document.getElementById('phone');
    const passwordInput1 = document.getElementById('password1');
    const passwordInput2 = document.getElementById('password2');

    // Function to check and apply the 'is-invalid' class based on error message
    function handleValidation() {
        const errorMessageElement = document.querySelector('.alert-danger');
        if (errorMessageElement) {
            const errorMessage = errorMessageElement.textContent.trim();

            if (errorMessage.includes("L'Email choisi est déjà utilisé.")) {
                emailInput.classList.add('is-invalid');

            } else if (errorMessage.includes("Le nom d'utilisateur existe déjà.")) {
                usernameInput.classList.add('is-invalid');

            } else if (errorMessage.includes("Le numéro de téléphone existe déjà.")) {
                phoneInput.classList.add('is-invalid');

            } else if (errorMessage.includes("Les mots de passe ne correspondent pas.")) {
                passwordInput2.classList.add('is-invalid');
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

    passwordInput1.addEventListener('input', () => {
        passwordInput1.classList.remove('is-invalid');
    });

    usernameInput.addEventListener('input', () => {
        usernameInput.classList.remove('is-invalid');
    });

    passwordInput2.addEventListener('input', () => {
        passwordInput2.classList.remove('is-invalid');
    });

    phoneInput.addEventListener('input', () => {
        phoneInput.classList.remove('is-invalid');
    });






   $(document).ready(function() {
    // Get references to the password input fields
    const $password1Input = $('#password1');
    const $password2Input = $('#password2');
    const $invalidFeedback = $('#invalid-feedback');

    // Function to check password match
    function checkPasswordMatch() {
      const password1Value = $password1Input.val();
      const password2Value = $password2Input.val();

      // Check if the passwords match
      if (password1Value === password2Value) {
        // Remove the "invalid" class and hide the invalid feedback message
        $password2Input.removeClass('is-invalid');
        $password2Input.addClass('is-valid');
        $invalidFeedback.hide();
      } else {
        // Add the "invalid" class and show the invalid feedback message
        $password2Input.addClass('is-invalid');
        $invalidFeedback.show();
      }
    }

    // Add event listeners on both password fields to trigger the check
    $password1Input.on('input', checkPasswordMatch);
    $password2Input.on('input', checkPasswordMatch);
  });


function formatPhoneNumber() {
    const phoneInput = document.getElementById('phone');
    let phoneNumber = phoneInput.value.replace(/\D/g, ''); // Remove non-numeric characters

    // Ensure we don't exceed the maximum allowed length
    if (phoneNumber.length > 10) {
        phoneNumber = phoneNumber.slice(0, 10);
    }

    // Format the phone number as per the pattern "00 00 00 00 00"
    let formattedNumber = phoneNumber.replace(/(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})/, '$1 $2 $3 $4 $5');

    phoneInput.value = formattedNumber;
}
