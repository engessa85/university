let registerModal = document.getElementById("modal-register");
let registerbutton = document.getElementById("register-button");

registerModal.style.display = "none"

registerbutton.onclick = () => {
    registerModal.style.display = "block";
};

// Close the modal when clicking anywhere outside of it
window.addEventListener("click", function(event) {
    if (event.target !== registerModal && event.target !== registerbutton) {
        registerModal.style.display = "none";
    }
});




let loginModal = document.getElementById("modal-login");
let loginbutton = document.getElementById("login-button");

loginModal.style.display = "none"

loginbutton.onclick = () => {
    loginModal.style.display = "block";
};

// Close the modal when clicking anywhere outside of it
window.addEventListener("click", function(event) {
    if (event.target !== loginModal && event.target !== loginbutton) {
        loginModal.style.display = "none";
    }
});