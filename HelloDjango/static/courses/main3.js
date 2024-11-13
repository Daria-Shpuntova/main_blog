 $(document).ready(function() {
    $('#commentForm').submit(function(event) {
    event.preventDefault();
    $.ajax({
        url: $(this).attr('action'),
        type: $(this).attr('method'),
        data: $(this).serialize(),
        success: function() {
                $('#comments').load(window.location.href + " #comments" );
                $("#commentForm").trigger('reset');
            },
        error: function() {
            alert('Что-то пошло не так');
        }
        });
    });
 })