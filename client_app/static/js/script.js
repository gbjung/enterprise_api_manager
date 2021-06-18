let apiLibraryLink = document.querySelector("#api-library");
let dropdownMenu = document.querySelector(".dropdown-menu");
let body = document.querySelector("body");

apiLibraryLink.addEventListener("click", function() {
    dropdownMenu.classList.toggle("hide");
})

// body.addEventListener("click", function() {
//     dropdownMenu.classList.add("hide");
// })
