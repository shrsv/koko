var frm = $('#main');
frm.submit(function (ev) {
    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: frm.serialize(),
        success: function (data) {
            wrapped_data = "<h2>Possible Tags</h2>" + data;
            $("#result").html(wrapped_data);
        }
    });

    ev.preventDefault();
});

$(document).ajaxStart(function() {
  $('#loading').show();
}).ajaxStop(function() {
  $('#loading').hide();
});

$("#header").hover(
    function() {
        $("#header small").html("Koko is a gorilla and she has a <a href='http://en.wikipedia.org/wiki/Koko_(gorilla)' target='_new'>wikipedia</a> page.");
    },
    function() {
        $("#header small").text("extract possible tags for any text");
    }
);
