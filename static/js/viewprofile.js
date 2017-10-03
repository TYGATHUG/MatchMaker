
$(document).ready(function () {

    var details = document.getElementById("details");
    var form = document.getElementById("edit-profile-form");
    var answer_form = document.getElementById("edit-personality-form");
    var answer_details = document.getElementById("answer_details");
    var details_form = $("#details-form");

    // hide forms initially
    $(form).hide();
    $(answer_form).hide();


    // code to show/hide profile form in tab 1
    $('#edit-details-btn').on('click', function() {
        $("#edit-profile-form").fadeIn();
        $(details).hide();
        $("#edit-details-btn").hide();
        $("#deactivate-profile-btn").hide();
    });

    $('#edit-profile-back-btn').on('click', function() {
        $(form).hide();
        $("#details").fadeIn();
        $("#edit-details-btn").fadeIn();
        $("#deactivate-profile-btn").fadeIn();
    });

    // code to show/hide personality form in tab 2
    $('#edit-answers-btn').on('click', function() {
        $("#edit-personality-form").fadeIn();
        $(answer_details).hide();
        $("#edit-answers-btn").hide();
    });

    $('#edit-answer-back-btn').on('click', function() {
        $(answer_form).hide();
        $("#answer_details").fadeIn();
        $("#edit-answers-btn").fadeIn();
    });

    // code to run when profile is deactivated


    // // use AJAX to send data to Flask back-end with jQuery
    // $('#deactivate-profile-btn').on('click', function() {
    //         $.ajax({
    //             url: "{{ url_for('deactivate_user') }}",
    //             method: "POST",
    //             data: {
    //                 data:$
    //             }
    //         })
    // });

    // show original details if user is exiting form by clicking on a tab
    $("#stars").on('click', function(){
       $(form).hide();
       $("#details").fadeIn();
    });

    $("#favorites").on('click', function(){
       $(answer_form).hide();
       $("#answer_details").fadeIn();
    });

    $("form").submit(function(e) {

        details_form.validate();

        if (!details_form.valid()) {
            alert("form not valid!");
        } else {
            alert("it's valid!");
        }
        }

    );


       //
       // $('div#tab1 #edit-profile-form').hide();
       // $('.tab-content #edit-profile-form').eq($(this).index()).show()

    // var element = document.getElementById("details");
    //
    // element.style.visibility = "hidden";
});

function show_alert() {
  if(confirm("Do you really want to do this?"))
    document.forms[0].submit();
  else
    return false;
}

$(document).ready(function () {

    $(".btn-pref .btn").click(function () {
        $(".btn-pref .btn").removeClass("btn-primary").addClass("btn-default");
        // $(".tab").addClass("active"); // instead of this do the below
        $(this).removeClass("btn-default").addClass("btn-primary");
    });
});

$(document).ready(function () {
    var profile = document.getElementById("tab1");
    var button = document.getElementById("edit-details-btn");
    var editprofileform = document.getElementById("edit-profile-form");
    var backbutton = document.getElementById("edit-profile-back-btn");
    var visibleDivId = null;

    // button.onclick = function(){
    //   alert("HELLO");
    // };
    // when you click this button, do this function
    // button.onclick = function () {
    //     alert("HELLO");
    //     // if(content.className == "tab-pane fade in active"){
    //     //     // show profile details
    //     // } else {
    //     //     // show edit profile form
    //     // }
    // }


});



// $("#edit-profile-form").hide()
//
// $('#edit-details-btn').click(function(){
//     if ($(this).attr("class") == "btn btn-default edit")
//     {
//         $("#edit-profile-form").show()
//     }
//
// });

// Content Area
function openTab(evt, pageName) {
    var i, tablinks;

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    evt.currentTarget.className += " active";
}

// view another user's profile
function view_profile(clicked_user){
    console.log(clicked_user)
}

function test(current_user, viewed_user){
    console.log(current_user)
    console.log(viewed_user)
}


$(document).ready(function () {
(function () {
    var Message;
    Message = function (arg) {
        this.text = arg.text, this.message_side = arg.message_side;

        // function to print/draw the message out to the box
        this.draw = function (_this) {
            return function () {
                var $message;
                $message = $($('.message_template').clone().html());
                $message.addClass(_this.message_side).find('.text').html(_this.text);
                $('.messages').append($message);
                return setTimeout(function () {
                    return $message.addClass('appeared');
                }, 0);
            };
        }(this);
        return this;
    };

    $(function () {
        var getMessageText, message_side, sendMessage;
        message_side = 'right';
        getMessageText = function () {
            var $message_input;
            $message_input = $('.message_input');
            return $message_input.val();
        };

        //function to send the actual message
        sendMessage = function (text) {
            var $messages, message;
            if (text.trim() === '') {
                return;
            }

            //this part mentions what side to print the message from
            //who is sending this message?
            $('.message_input').val('');
            $messages = $('.messages');
            message_side = message_side === 'left' ? 'right' : 'left';
            message = new Message({
                text: text,
                message_side: message_side
            });
            message.draw();
            return $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
        };

        //send the message either through clicking or pressing "enter/return"
        $('.send_message').click(function (e) {
            return sendMessage(getMessageText());
        });
        $('.message_input').keyup(function (e) {
            if (e.which === 13) {
                return sendMessage(getMessageText());
            }
        });
        // function to send message to server
        // sendMessage('Hello Philip! :)');

    });
}.call(this));
});

