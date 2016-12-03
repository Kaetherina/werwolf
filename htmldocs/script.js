/**
 * Created by vrettos on 30.09.2016.
 */

$( "#encryption-form" ).submit(
    function( event ) {
    $.ajax({
        url: $('#encryption-form').attr('action'),
        data : $('#encryption-form').serialize(),
        method: 'post',
        success:
            function(pair){
            console.log(pair);
            $('#encrtext').append('<p>'+pair.encrText+'</p>')
        }
    });
    return false;
});
/*
function submitPlain(){
    $.ajax({
        url:    $('encryption-form').attr('action'),
        data :  $('#encryption-form').serialize(),
        method: 'post',
        success:
            function(pair){
                console.log(pair);
                $('#encrtext').append('<p>'+pair.encrText+'</p>')
            }
    });
}
*/
function listeHolen() {
    console.log('Hat geklappt');
    var table = '<table style="border: 2px ">';

    $.ajax({
        dataType: "json",
        url: "/api/encrypt",
        method: "get",
        success: function(arr) {
            arr.forEach(function(elem){
                console.log('elem: ', elem);
                table = table + '<tr><td class="plain">' +elem.plainText + '</td><td class="encrypted">' +elem.encrText + '</td></tr>'
            });
            table += '</table>';
            $('#list').empty();
            $('#list').append(table);

            //        setTimeout(function() {
            //          $('#liste').empty();
            //        }, 2000);

        }
    })}