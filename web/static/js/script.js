$(function() {
    
    var user_order = [];

    sortable('.js-sortable', {
            forcePlaceholderSize: true,
            placeholderClass: 'mb1 dark-bg',
            hoverClass: 'bg-maroon yellow'
        })


        
    sortable('.sortable')[0].addEventListener('sortupdate', function(e) {
            user_order = []
            e.detail.origin.items.forEach(element => {user_order.push(element.id)});
    });


    $("#button").click(function(){

        $.ajax({
            url: "/match",
            type: "POST",
            contentType: 'application/json',
            data: JSON.stringify({
                "user_order":user_order
              }),
            success: function(response) {
                $('#result').append(response)
            }
        });


    });



});