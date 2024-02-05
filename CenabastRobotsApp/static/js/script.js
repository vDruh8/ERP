var botones = Array.from(
document.querySelectorAll(".btn")
);
var contenidos = Array.from(
document.querySelectorAll(".hidden")
);

botones.forEach(function (boton) {
boton.addEventListener("click", function () {
    var index = parseInt(boton.getAttribute("data-index"));

    contenidos.forEach(function (element) {
    element.style.display = "none";
    });

    contenidos[index].style.display = "flex";
    contenidos[index].style.justifyContent = "center";
});
});



function Menu(e) {
  let list = document.querySelector("ul");
  e.name === "menu"
    ? ((e.name = "close"),
      list.classList.add("top-[80px]"),
      list.classList.add("opacity-100"))
    : ((e.name = "menu"),
      list.classList.remove("top-[80px]"),
      list.classList.remove("opacity-100"));
}