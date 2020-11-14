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


    $("#register").click(function(){

        var user_name = $("#user-name").val();

        $.ajax({
            url: "/record_user_preference",
            type: "POST",
            contentType: 'application/json',
            data: JSON.stringify({
                "user_name":user_name,
                "user_order":user_order
              })
        });


    });

    $("#find-partner").click(function(){
        var user_name = $("#user-name").val();
        $.ajax({
            url: "/get_best_matches",
            type: "POST",
            contentType: 'application/json',
            data: JSON.stringify({
                "user_name":user_name,
                "user_order":user_order
              }),
            success: function(response) {
                $('#result').append(response)
            }
        });


    });


});