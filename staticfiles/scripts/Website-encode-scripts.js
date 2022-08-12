const toggler = document.querySelector("#toggler")
const toggle_Menu = document.querySelector(".nav-group-mobile")
const signUp = document.querySelector(".mob-active")
const logIn = document.querySelector(".mob-link")
const holder = document.querySelector('.header-username')
const navDesk = document.querySelector('.nav-desktop')


toggler.addEventListener("click", () => {
    toggler.classList.toggle("activated")
    toggle_Menu.classList.toggle("activatede")
})

document.querySelectorAll(".mob-link").forEach(n => n.addEventListener("click",()=> {
    toggler.classList.remove("activated")
    toggle_Menu.classList.remove("activatede")
}))

holder.addEventListener('click',()=> {
    navDesk.classList.toggle('nav-active')
})

document.querySelector(".link").forEach(n => n.addEventListener("click", () => {
    navDesk.classList.remove('nav-active')
}))


function createNewElement() {
  var txtNewInputBox = document.createElement('div');

  txtNewInputBox.innerHTML = "<input type='text' id='newInputBox' placeholder='E.g https://qrx.com/'>";

  document.getElementById("newElementId").appendChild(txtNewInputBox);
}
  

