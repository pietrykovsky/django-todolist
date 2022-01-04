navbar = document.getElementById("main-navbar");

document.addEventListener("DOMContentLoaded", () => {
    window.addEventListener("scroll", () => {
        if(window.scrollY > 100) {
            navbar.classList.add('fixed-top');

            // add padding top to show content behind navbar
            navbarHeight = document.querySelector('.navbar').offsetHeight;
            document.body.style.paddingTop = navbarHeight + 'px';
        }
        else {
            navbar.classList.remove('fixed-top');

            //remove padding
            document.body.style.paddingTop = '0'; 
        }      
    });
});
