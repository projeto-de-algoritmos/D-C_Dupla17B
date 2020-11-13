$(function() {
    
    var user_order = [];

    sortable('.js-sortable', {
            forcePlaceholderSize: true,
            placeholderClass: 'mb1 bg-navy',
            hoverClass: 'bg-maroon yellow'
        })


        
    sortable('.sortable')[0].addEventListener('sortupdate', function(e) {
            e.detail.origin.items.forEach(element => {user_order.push(element.id)});
    });


    $("#button").click(function(){
        console.log("bb");

        $.ajax({
            url: "/match",
            type: "POST",
            // dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({
                "user_order":"Test Name"
              }),
            success: function(response) {
                $('#result').append(response)
            }
        });


    });



});