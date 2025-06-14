document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript Loaded");

    let rememberMeCheckbox = document.getElementById("remember-me");

    if (rememberMeCheckbox) {
        rememberMeCheckbox.addEventListener("change", function() {
            console.log("Remember me: " + this.checked);
        });
    }
});
