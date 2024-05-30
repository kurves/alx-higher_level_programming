$(document).ready(function() {
    $('#btn_translate').click(function() {
        const langCode = $('#language_code').val();
        if (langCode) {
            $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function(data) {
                $('#hello').text(data.hello);
            }).fail(function() {
                $('#hello').text('Translation not available.');
            });
        } else {
            $('#hello').text('Please enter a language code.');
        }
    });
});
