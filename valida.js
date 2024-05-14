$(document).ready(function() {
    $('#postulacionForm').on('submit', function(e) {
        e.preventDefault();  // Prevenir el envío automático para realizar la validación primero
        if (validarFormulario()) {
            this.submit();  // Si todas las validaciones son correctas, se envía el formulario
        }
    });

    $('#crearCarta').click(function() {
        if (validarFormulario()) {
            var cartaTexto = "Estimado equipo,\n\nMe gustaría postular para el trabajo de apoyo ambiental en Chiloé. Mi nombre es " + $('#nombre').val() +
                ", " + $('#genero').find(":selected").text() + " de " + $('#edad').val() + " años. Mi motivación para postular es: " + $('#motivacion').val() + "\n\nAtentamente,\n" + $('#nombre').val();
            $('#carta').val(cartaTexto);
        } else {
            alert('Por favor, corrija los errores en el formulario antes de generar la carta.');
        }
    });
});

function validarFormulario() {
    var valid = true;

    if ($('#rut').val().length < 9 || $('#rut').val().length > 10) {
        alert('El RUT debe tener entre 9 y 10 caracteres.');
        valid = false;
    }
    if ($('#nombre').val().length < 3 || $('#nombre').val().length > 20) {
        alert('El nombre debe tener entre 3 y 20 caracteres.');
        valid = false;
    }
    if ($('#apellidoPaterno').val().length < 3 || $('#apellidoPaterno').val().length > 20) {
        alert('El apellido paterno debe tener entre 3 y 20 caracteres.');
        valid = false;
    }
    if ($('#apellidoMaterno').val().length < 3 || $('#apellidoMaterno').val().length > 20) {
        alert('El apellido materno debe tener entre 3 y 20 caracteres.');
        valid = false;
    }
    if ($('#edad').val() < 18 || $('#edad').val() > 35) {
        alert('La edad debe estar entre 18 y 35 años.');
        valid = false;
    }
    if ($('#genero').val() === "") {
        alert('Seleccione un género de la lista.');
        valid = false;
    }
    if ($('#celular').val().length < 9 || $('#celular').val().length > 12) {
        alert('El celular debe tener entre 9 y 12 caracteres.');
        valid = false;
    }

    return valid;  // Retorna verdadero solo si todas las validaciones son correctas
}
