$("#bold").click(function () {
    $('#note').val($('#note').val() + '<b></b>');
});

$("#italic").click(function () {
    $('#note').val($('#note').val() + '<i></i>');
});

$("#underlined").click(function () {
    $('#note').val($('#note').val() + '<u></u>');
});

$("#deleted").click(function () {
    $('#note').val($('#note').val() + '<del></del>');
});

$("#pre").click(function () {
    $('#note').val($('#note').val() + '<pre></pre>');
});

$("#p").click(function () {
    $('#note').val($('#note').val() + '<p></p>');
});

$("#img").click(function () {
    let img = window.prompt("image");
    
    if((img != "") && (img != null)){
        $('#note').val($('#note').val() + '<img src="'+ img +'">');
    }
});

$("#li").click(function () {
    $('#note').val($('#note').val() + '<li><li/>');
});

$("#href").click(function () {
    let url = window.prompt("url");
    
    if((url != "") && (url != null)){
        $('#note').val($('#note').val() + '<a href="'+ url +'">'+ url +'</a>');
    }
});

$("#br").click(function () {
    $('#note').val($('#note').val() + '<br>');
});

$(document).ready(function(){
    $("button").click(function(){
        if (confirm("Are you sure ?") == true) {
            $.ajax({
                type: "DELETE",
                url: '/admin/note/' + this.id,
                success: function (data) {
                    if (data) {
                        location.reload();
                    }
                },
                error: function (error) {
                    console.debug(error);
                }
            });
        } 
    });
});