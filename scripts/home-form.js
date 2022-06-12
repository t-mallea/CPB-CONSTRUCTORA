$(function(){
    var $registerForm = $("#frmContact");
    if($registerForm.length){
        $registerForm.validate({
            rules:{
                txtNombreCompleto:{
                    required: true
                },
                txtRut: {
                    required: true
                },
                txtTelefono: {
                    required: true
                },
                txtEmail: {
                    required: false
                }
            }
        })
    }
})




