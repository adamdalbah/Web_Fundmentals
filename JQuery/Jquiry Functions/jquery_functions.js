$(document).ready (function(){
        $('.btn1').click(function(){
            $('p').hide();
        })
        $('.btn2').click(function(){
            $('p').show();
        })
        $('.btn3').click(function(){
            $('p').toggle();
        })
        $('.btn4').click(function(){
            $('p').slideUp();
        })
        $('.btn5').click(function(){
            $('p').slideDown();
        })
        $('.btn6').click(function(){
            $('p').slideToggle();
        })
        $('.btn7').click(function(){
            $('p').fadeIn();
        })
        $('.btn8').click(function(){
            $('p').fadeOut();
        })
        $('.btn9').click(function(){
            $('button').addClass('btn btn-primary');
        })
        $('.btn10').click(function(){
            $('p').before("<p>Coding Dojo</p>");
        })
        $('.btn11').click(function(){
            $('p').after("<p>After Dojo</p>")
        })
        $('.btn12').click(function(){
            $('p').append("<b> something up</b>")
        })
        $('.btn13').click(function(){
            $('p').html("Hello <b> world </b>!")
        })
        $('.btn14').click(function(){
            $('img').attr("border","5px solid red")
        })
        $('.btn15').click(function(){
            $("input:text").val("Hello its me Mario");
        })
        $('.btn16').click(function(){
            $('p').text("Mamamia")
        })
    })

    
