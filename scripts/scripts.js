const toggler = document.querySelector("#toggler")
const toggle_Menu = document.querySelector(".nav-group-mobile")
const signUp = document.querySelector(".mob-active")
const logIn = document.querySelector(".mob-link")
<<<<<<< HEAD
=======
const holder = document.querySelector('.header-username')
const navDesk = document.querySelector('.nav-desktop')
>>>>>>> master


toggler.addEventListener("click", () => {
    toggler.classList.toggle("activated")
    toggle_Menu.classList.toggle("activatede")
})

document.querySelectorAll(".mob-link").forEach(n => n.addEventListener("click",()=> {
    toggler.classList.remove("activated")
    toggle_Menu.classList.remove("activatede")
<<<<<<< HEAD
}))
=======
}))

holder.addEventListener('click',()=> {
    navDesk.classList.toggle('nav-active')
})

document.querySelector(".link").forEach(n => n.addEventListener("click", () => {
    navDesk.classList.remove('nav-active')
}))


let input = document.querySelector(".file");
let button = document.querySelector(".button-1");
button.disabled = true;
input.addEventListener("change", stateHandle);

function stateHandle() {
    if(document.querySelector(".file").value === "") {
        button.disabled = true;
    } else {
        button.disabled = false;
    }
}


var inputs = document.querySelectorAll( '.file' );
Array.prototype.forEach.call( inputs, function( input )
{
	var label	 = input.nextElementSibling,
		labelVal = label.innerHTML;

	input.addEventListener( 'change', function( e )
	{
		var fileName = '';
		if( this.files && this.files.length > 1 )
			fileName = ( this.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', this.files.length );
		else
    fileName = e.target.value.split('\\').pop() ;

		if( fileName )
			label.querySelector( 'span' ).innerHTML = fileName;
		else
			label.innerHTML = labelVal;
	});
});
{{}}
>>>>>>> master
