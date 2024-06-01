/* global $ */

$(document).ready(function () {
  function fetchHello () {
    const langCode = $('#language_code').val();
    if (langCode) {
      $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`, function (data) {
        $('#hello').text(data.hello);
      }).fail(function () {
        $('#hello').text('Translation not available.');
      });
    } else {
      $('#hello').text('Please enter a language code.');
    }
  }

  $('#btn_translate').click(fetchHello);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchHello();
    }
  });
});
