$(document).ready(
function(){
    $('button').attr('disabled',true);
    $('input:file').change(
        function(){
            if ($(this).val()){
                $('#submitButton').removeAttr('disabled'); 
            }
            else {
                $('#submitButton').attr('disabled',true);
            }
        });
});
