// Mobile navigation
const menuBtn = document.getElementById("menuBtn");
const navLinks = document.getElementById("navLinks");

menuBtn.addEventListener("click", function () {
    navLinks.classList.toggle("active");
});


// Start Studying button
const startBtn = document.getElementById("startBtn");

startBtn.addEventListener("click", function () {
    document.getElementById("tasks").scrollIntoView({
        behavior: "smooth"
    });
});


// Task completion
const checkboxes = document.querySelectorAll(".task-checkbox");

checkboxes.forEach(function (checkbox) {

    checkbox.addEventListener("change", function () {

        const taskText = this.nextElementSibling;

        if (this.checked) {
            taskText.style.textDecoration = "line-through";
            taskText.style.opacity = "0.6";
        } else {
            taskText.style.textDecoration = "none";
            taskText.style.opacity = "1";
        }

    });

});