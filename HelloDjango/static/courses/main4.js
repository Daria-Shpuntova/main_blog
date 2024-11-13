$('.openmodal_free').click(function (e) {
         e.preventDefault();
         $('.modal_free').addClass('opened');
    });
$('.closemodal').click(function (e) {
         e.preventDefault();
         $('.modal_free').removeClass('opened');
    });


$(document).ready(function() {
    $('#fullform').submit(function(event) {
    event.preventDefault();
    $.ajax({
        url: $(this).attr('action'),
        type: $(this).attr('method'),
        data: $(this).serialize(),
        success: function() {
            $('.openmodal_full').click(function (e) {
                e.preventDefault();
                $('.modal_full').addClass('opened');
                });
            $('.closemodal').click(function (e) {
                e.preventDefault();
                $('.modal_full').removeClass('opened');
                });
            },
        error: function() {
            alert('Что-то пошло не так');
       }
       });
   });
})


$('.openmodal_full').click(function (e) {
                e.preventDefault();
                $('.modal_full').addClass('opened');
                });
            $('.closemodal').click(function (e) {
                e.preventDefault();
                $('.modal_full').removeClass('opened');
                });