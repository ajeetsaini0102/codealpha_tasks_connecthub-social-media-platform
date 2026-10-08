const togglePassword = document.getElementById("togglePassword");
const password = document.getElementById("password");

const toggleConfirmPassword = document.getElementById("toggleConfirmPassword");
const confirmPassword = document.getElementById("confirm_password");

const registerForm = document.getElementById("registerForm");
const passwordMessage = document.getElementById("passwordMessage");


togglePassword.addEventListener("click", function () {

    if (password.type === "password") {
        password.type = "text";
        togglePassword.textContent = "Hide";
    } else {
        password.type = "password";
        togglePassword.textContent = "Show";
    }

});


toggleConfirmPassword.addEventListener("click", function () {

    if (confirmPassword.type === "password") {
        confirmPassword.type = "text";
        toggleConfirmPassword.textContent = "Hide";
    } else {
        confirmPassword.type = "password";
        toggleConfirmPassword.textContent = "Show";
    }

});


registerForm.addEventListener("submit", function (event) {

    if (password.value !== confirmPassword.value) {

        event.preventDefault();

        passwordMessage.textContent = "Passwords do not match.";

    } else {

        passwordMessage.textContent = "";

    }

});