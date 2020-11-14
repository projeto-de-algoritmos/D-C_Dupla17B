$(function () {

    var user_order = [];

    sortable('.js-sortable', {
        forcePlaceholderSize: true,
        placeholderClass: 'mb1 dark-bg',
        hoverClass: 'bg-maroon yellow'
    })



    sortable('.js-sortable')[0].addEventListener('sortupdate', function (e) {
        user_order = []
        e.detail.origin.items.forEach(element => { user_order.push(element.id) });
    });


    $("#register").click(function () {

        var user_name = $("#user-name").val();
        var user_contact = $("#user-contact").val();

        if (!user_name || !user_contact) {
            var failure = '<div id="failure" class="ml4 alert alert-danger"><p>Name and Contact Info cannot be empty</p></div>'
            $(failure).hide().prependTo('#genres').fadeIn();
            setTimeout(function () {
                $('#failure').fadeOut();
            }, 2600);
            return
        }

        if (user_order.length == 0) {
            sortable('.js-sortable', 'serialize')[0].items.forEach(element => { user_order.push(element.node.id) });
        }


        $.ajax({
            url: "/record_user_preference",
            type: "POST",
            contentType: 'application/json',
            data: JSON.stringify({
                "user_name": user_name,
                "user_order": user_order,
                "user_contact": user_contact
            }),
            success: function () {
                var success = '<div id="success" class="ml4 alert alert-success"><p>Preferences recorded!</p></div>'
                $(success).hide().prependTo('#genres').fadeIn();
                setTimeout(function () {
                    $('#success').fadeOut();
                }, 2600);
            }
        });


    });

    $("#find-partner").click(function () {
        var user_name = $("#user-name").val();
        $.ajax({
            url: "/get_best_matches",
            type: "POST",
            contentType: 'application/json',
            data: JSON.stringify({
                "user_name": user_name,
                "user_order": user_order
            }),
            success: function (response) {
                $('#result').append(response)
            }
        });


    });


});