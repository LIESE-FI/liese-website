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
    $(function(){
        $(".navbar-placeholder").load("../main/navbar.html");
    });
    
    $(function(){
        $(".footer-placeholder").load("../main/footer.html");
    });
});
