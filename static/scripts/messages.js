var colors = [
    "#F4743B",
    "#FFB100",
    "#4ecdc4",
    "#edddd4",
    "#b58db6",
    "#ff9b85",
    "#adc178",
    "#acd8aa",
    "#c9ada1"
]
$(document).ready(function() {
    var m = new MersenneTwister();
    $('.username').each(function(index) {
        // $(this).css("color", colors[index % colors.length]) 
        // $(this).css("color", colors[Math.floor(Math.random() * colors.length)])
        $(this).css("color", colors[Math.floor(m.random() * colors.length)])
    });
    setTimeout(
        function() {
            $("html, body").animate({
                scrollTop: $(
                    'html, body').get(0).scrollHeight
            }, 1000);
        }, 500);
});