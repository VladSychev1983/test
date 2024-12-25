(function() {
let checkbox = document.getElementById("checkbox");
checkbox.addEventListener("change", () => {
let body = document.body;
body.classList.toggle("light-mode");
    })
}());