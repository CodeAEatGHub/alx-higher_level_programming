//Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('input#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('input#language_code').val() }), function (data) {
      $('div#hello').html(data.hello);
    });
  });
});