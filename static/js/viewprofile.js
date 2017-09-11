$(document).ready(function () {

    $(".btn-pref .btn").click(function () {
        $(".btn-pref .btn").removeClass("btn-primary").addClass("btn-default");
        // $(".tab").addClass("active"); // instead of this do the below
        $(this).removeClass("btn-default").addClass("btn-primary");
    });
});

$(document).ready(function () {
    var profile = document.getElementById("tab1")
    var button = document.getElementById("edit-details-btn")
    var editprofileform = document.getElementsById("edit-profile-form")
    var backbutton = document.getElementById("edit-profile-back-btn")
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


$(document).ready(function () {

    $('#edit-details-btn').on('click', function() {
        $(this).hide();
    });

      //  $('div#tab1 #edit-profile-form').hide();
       // $('.tab-content #edit-profile-form').eq($(this).index()).show()

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