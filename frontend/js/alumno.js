const user = JSON.parse(localStorage.getItem("usuario"));
if (!user || user.rol !== "alumno") location.href = "login.html";

const nombreEl = document.getElementById("nombreUsuario");
if (nombreEl) nombreEl.textContent = user.nombre;

const lista = document.getElementById("listaMaterias");
if (lista && user.materias) {
  user.materias.forEach(materia => {
    const li = document.createElement("li");
    li.textContent = materia;
    lista.appendChild(li);
  });
}
