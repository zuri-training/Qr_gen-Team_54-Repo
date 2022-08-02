const toggler = document.querySelector("#toggler")
const toggle_Menu = document.querySelector(".nav-group-mobile")
const signUp = document.querySelector(".mob-active")
const logIn = document.querySelector(".mob-link")


toggler.addEventListener("click", () => {
    toggler.classList.toggle("activated")
    toggle_Menu.classList.toggle("activatede")
})

document.querySelectorAll(".mob-link").forEach(n => n.addEventListener("click",()=> {
    toggler.classList.remove("activated")
    toggle_Menu.classList.remove("activatede")
}))