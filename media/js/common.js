/**
 * Created by peter on 2017/7/27.
 */
$(".animateTitle1").animatext({
    speed: 300,
    effect: 'flipInY',
    reverse: false
});
$(".demo1").animatext({
    speed: 150,
});
$(".demo2").animatext({speed: 150,
    effect: 'flipInX',
    infinite: true
});
$(".demo3").animatext({speed: 150,
    mode: "words",
    effect: 'swing',
    infinite: true
});
$(".demo4").animatext({speed: 150,
    effect: 'tada',
    reverse: true,
    infinite: true
});

$(".login").click(function () {
   location.href = '/login/'
});


$(".reg").click(function () {
   location.href = '/reg/'
});
