$(document).ready(function(){
    // Cuando se hace clic en un botón de la barra de navegación
    $(".nav-link").click(function(event){
        console.log("click en nav-link");
        var target = $(this).attr("href"); 
        console.log(target);
        // Ocultar todos los divs con clase page
        $(".page").fadeOut(500);
        // Mostrar el div con id igual al href del botón
        $(target).fadeIn(500);
    });
});
document.querySelectorAll('a[href^="index.html"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();

                // Aplicar la clase fade-out a la sección main-page
                $('.main-page').fadeOut(500);

                // Esperar a que termine la animación antes de navegar
                setTimeout(() => {
                    window.location.href = this.getAttribute('href');
                }, 500); // Tiempo de la animación
            });
        });