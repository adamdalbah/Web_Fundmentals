$(document).ready(function(){
    $('li').click(function(){
        $(this).hide();
    })
    $('button').click(function(){
        $('li').show();
    })

})