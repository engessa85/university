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






let studentLogIn = document.getElementById("student--login")

let univLogIn = document.getElementById("univ--login")

// Get the modal
var modal = document.getElementById("modal");



// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
studentLogIn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
