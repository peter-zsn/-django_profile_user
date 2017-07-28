/**
 * Created by peter on 2017/7/27.
 */
$(function () {
   $('body').particleground({
       dotColor: '#5cbdaa',
       lineColor: '#5cbdaa'
   });
});

$('#submit_btn').click(function () {
    var username = $('#username').val();
    var password = $('#password').val();
    console.log(username);
    $.ajax({
        url: '/login/',
        type: 'post',
        data: { "username": username, "password": password },
        success: function(data) {
            alert(data);
            location.href = '/';
        }
    })
});

$("#back").click(function () {
    location.href = '/';
});