$(document).ready(function () {
    $(".btn_click").click(function () {
        var source = $("input[name='source']:checked").map(function () {
            return this.value;
        }).get().join(', ');
        alert("My favourite programming languages are: " + programming);
    });
});