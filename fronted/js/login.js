
document.addEventListener("DOMContentLoaded", () => {
  const rfid = localStorage.getItem("rfid_temp");
  if (rfid) {
    document.getElementById("matricula").value = rfid;
    localStorage.removeItem("rfid_temp");
  }
});

document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault();
  const matricula = document.getElementById("matricula").value;
  const password = document.getElementById("password").value;
  const user = usuariosSimulados.find(u => u.matricula === matricula && u.password === password);
  if (user) {
    localStorage.setItem("usuario", JSON.stringify(user));
    if (user.rol === "profesor") {
      window.location.href = "profesor.html";
    } else {
      window.location.href = "alumno.html";
    }
  } else {
    document.getElementById("error").textContent = "Credenciales incorrectas.";
  }
});
