function toggleNav() {
  const navLinks = document.getElementById("nav-links");
  navLinks.classList.toggle("show");
}

setTimeout(() => {
  document.querySelectorAll(".alert").forEach((alert) => {
    alert.classList.add("fade-out"); // trigger fade-out
    setTimeout(() => {
      alert.style.display = "none"; // hide completely after fade
    }, 1000); // match transition duration
  });
}, 4000); // start fading after 4s, gone by 5s

// Optional JS: auto-dismiss flash messages after 5 seconds
setTimeout(() => {
  document.querySelectorAll(".flash-message").forEach((msg) => {
    msg.style.display = "none";
  });
}, 5000);
