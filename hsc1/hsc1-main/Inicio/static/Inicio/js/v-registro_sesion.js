var nombre = document.getElementById("Username");
var email = document.getElementById("email");
var contra1 = document.getElementById("contra");
var contra2 = document.getElementById("contra2");
var reg = document.getElementById("region");
var comuna = document.getElementById("comuna");

const form = document.getElementById("form1");
var mensaje = document.getElementById("warnings");

form.addEventListener("submit", e => {
    let mensajesMostrar = "";
    let entrar = false;

    // Expresiones regulares para validación
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
    let usuario1 = /^[a-zA-Z0-9\_\-]{4,16}$/;

    mensaje.innerHTML = "";  // Limpiar mensajes anteriores

    // Validación de nombre de usuario
    if (!usuario1.test(nombre.value)) {
        mensajesMostrar += 'El nombre de usuario no es válido. <br>';
        entrar = true;
    }

    // Validación de email
    if (!regexEmail.test(email.value)) {
        mensajesMostrar += 'El correo electrónico ingresado no es válido. <br>';
        entrar = true;
    }

    // Validación de región
    if (reg.value === "" || reg.value === "Selecciona una región") {
        mensajesMostrar += 'Seleccione una región. <br>';
        entrar = true;
    }

    // Validación de comuna
    if (comuna.value === "" || comuna.value === "Selecciona una Comuna") {
        mensajesMostrar += 'Seleccione una Comuna. <br>';
        entrar = true;
    }

    // Validación de contraseña
    if (contra1.value.length < 4 || contra1.value.length > 16) {
        mensajesMostrar += 'La contraseña no tiene el largo necesario. <br>';
        entrar = true;
    }

    // Validación de confirmación de contraseña
    if (contra1.value !== contra2.value) {
        mensajesMostrar += 'Las contraseñas no coinciden. <br>';
        entrar = true;
    }

    // Si hubo errores, mostrar los mensajes y prevenir el envío del formulario
    if (entrar) {
        mensaje.innerHTML = mensajesMostrar;
        e.preventDefault();
    } else {
        mensaje.innerHTML = "Enviado";  // Mostrar mensaje de éxito (opcional)
    }
});

$('#region').on('change', function () {
    var regionId = $(this).val();  // Obtener el valor de la región seleccionada
    var comunaSelect = $('#comuna');  // Elemento del selector de comunas
    
    // Limpiar la lista de comunas sólo si la región seleccionada no tiene datos.
    if (regionId) {
        $.ajax({
            url: '/get-comunas/' + regionId + '/',
            method: 'GET',
            success: function (data) {
                comunaSelect.empty();  // Limpiar las opciones de comuna
                comunaSelect.append('<option value="">Selecciona una Comuna</option>');  // Opción por defecto

                // Llenar las opciones de comuna con los datos obtenidos del servidor
                data.comunas.forEach(function (comuna) {
                    comunaSelect.append('<option value="' + comuna.idComuna + '">' + comuna.nombreCom + '</option>');
                });
            },
            error: function() {
                // En caso de error en la petición, se muestra un mensaje de error o se deja la lista vacía.
                comunaSelect.empty();
                comunaSelect.append('<option value="">No se pudo cargar las comunas</option>');
            }
        });
    } else {
        // Si no hay región seleccionada, reiniciar la lista de comunas
        comunaSelect.empty();
        comunaSelect.append('<option value="">Selecciona una Comuna</option>');
    }
});
