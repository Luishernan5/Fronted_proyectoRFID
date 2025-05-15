
const user = JSON.parse(localStorage.getItem("usuario"));
if (!user || user.rol !== "alumno") location.href = "login.html";

document.getElementById("nombreUsuario").textContent = user.nombre;
const lista = document.getElementById("listaMaterias");
user.materias.forEach(materia => {
  const li = document.createElement("li");
  li.textContent = materia;
  lista.appendChild(li);
});

function verPase() {
  window.location.href = "ver_pase.html";
}
