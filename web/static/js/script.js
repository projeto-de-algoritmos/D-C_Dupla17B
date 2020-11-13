$(function() {
    
    var user_order = [];

    sortable('.js-sortable', {
            forcePlaceholderSize: true,
            placeholderClass: 'mb1 litemdark ',
            hoverClass: 'bg-maroon yellow'
        })
        
    // sortable('.sortable')[0].addEventListener('sortupdate', function(e) {
    //         e.detail.origin.items.forEach(element => {user_order.push(element.id)});
    // });


    // $("#button").click(function(){

    //     $.ajax({
    //         url: "/match",
    //         type: "post",
    //         data: {"user_order": user_order},
    //         success: function(response) {
    //             console.log(response);
    //             // $("#result").html(response);
    //         }
    //     });
    // });



});