
$(document).ready(function () {

    var details = document.getElementById("details");
    var form = document.getElementById("edit-profile-form");
    var answer_form = document.getElementById("edit-personality-form");
    var answer_details = document.getElementById("answer_details");
    var details_form = $( "#details-form");

    // hide forms initially
    $(form).hide();
    $(answer_form).hide()


    // code to show/hide profile form in tab 1
    $('#edit-details-btn').on('click', function() {
        $("#edit-profile-form").fadeIn();
        $(details).hide();
    });

    $('#edit-profile-back-btn').on('click', function() {
        $(form).hide();
        $("#details").fadeIn();
    });

    // code to show/hide personality form in tab 2
    $('#edit-answers-btn').on('click', function() {
        $("#edit-personality-form").fadeIn();
        $(answer_details).hide();
    });

    $('#edit-answer-back-btn').on('click', function() {
        $(answer_form).hide();
        $("#answer_details").fadeIn();
    });


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