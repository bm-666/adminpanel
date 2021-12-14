let form = document.forms.dateform;

$("#date").on('change', function () {
    const mydate = new Date($(this).val());
    const date_parse = `${mydate.getDate()}.${mydate.getMonth()}.${mydate.getFullYear()}`;
    const token = document.getElementsByName('csrfmiddlewaretoken')[0].value
    $.ajax({
        type: "POST",
        url: "date_parse",
        //dataType: "json",
        data: {
            "date_parser": String(mydate),
            "csrfmiddlewaretoken": token
        },
        success: function () {
            console.log(arguments[0].date_parse, arguments[0].raiting, arguments[0].count_comments);
            document.getElementById("date_parse").textContent = arguments[0].date_parse;
            document.getElementById("rating").textContent = arguments[0].raiting;
            document.getElementById("count_comments").textContent = arguments[0].count_comments;
        }
    })
})