$(document).ready(function() {
    $('a > button').click(function() {
        $(this).parent().toggleClass('modify-text');
    });
});