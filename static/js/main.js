//document.querySelector('.pisun').onclick = function() {
//    alert('Ouch! Stop poking me!'+ "\u{1F60D}" );
//}



$(document).ready(function(){
    $('.pisun').dblclick(function() {
        $('.pisun').hide();
        alert('Ouch! Stop poking me!'+ "\u{1F60D}" );
    });
});

