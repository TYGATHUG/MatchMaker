$(document).ready(function() {

	// Header Scroll
	$(window).on('scroll', function() {
		var scroll = $(window).scrollTop();

		if (scroll >= 0) {
			$('#header').addClass('fixed');
		} else {
			$('#header').removeClass('fixed');
		}
	});

	// Fancybox
	$('.work-box').fancybox();

	// Flexslider
	$('.flexslider').flexslider({
		animation: "fade",
		directionNav: false,
	});

	// Page Scroll
	var sections = $('section')
		nav = $('nav[role="navigation"]');

	$(window).on('scroll', function () {
	  	var cur_pos = $(this).scrollTop();
	  	sections.each(function() {
	    	var top = $(this).offset().top - 76
	        	bottom = top + $(this).outerHeight();
	    	if (cur_pos >= top && cur_pos <= bottom) {
	      		nav.find('a').removeClass('active');
	      		nav.find('a[href="#'+$(this).attr('id')+'"]').addClass('active');
	    	}
	  	});
	});
	nav.find('a').on('click', function () {
	  	var $el = $(this)
	    	id = $el.attr('href');
		$('html, body').animate({
			scrollTop: $(id).offset().top - 75
		}, 500);
	  return false;
	});

	// Mobile Navigation
	$('.nav-toggle').on('click', function() {
		$(this).toggleClass('close-nav');
		nav.toggleClass('open');
		return false;
	});
	nav.find('a').on('click', function() {
		$('.nav-toggle').toggleClass('close-nav');
		nav.toggleClass('open');
	});

	// Arrow Scroll
	var $root = $('html, body');
	$('#down-arrow').on('click', 'img', function(event) {
		$('html, body').animate({
        	scrollTop: $('#welcome-content').offset().top
    	}, 500);

        return false;
	});


	// Form Modals
	function loadModalAnimation() {

		// Variables to check if element exists
		var login_register_form_check = document.body.contains(document.getElementById("register-modal"));
		var profile_form_check = document.body.contains(document.getElementById("profile-form-modal-1"));

        if (login_register_form_check == true) {

            // login / register forms
            var rmodal = document.getElementById('register-modal'); // Get the modal
            var rbtn = document.getElementById('register-btn'); // Get the button that opens the modal
            var rspan = document.getElementById('register-close'); // Get the <span> element that closes the modal

            var lmodal = document.getElementById('login-modal');
            var lbtn = document.getElementById('login-btn');
            var lspan = document.getElementById('login-close');

            // When the user clicks on the button, open the modal
            rbtn.onclick = function () {
                lmodal.style.display = "none";
                rmodal.style.display = "block";

                $(rmodal)
                    .css('opacity', 0)
                    .slideDown('slow')
                    .animate(
                        {opacity: 1},
                        {queue: false, duration: 'fast'}
                    );
            }
            lbtn.onclick = function () {
                rmodal.style.display = "none";
                lmodal.style.display = "block";

                $(lmodal)
                    .css('opacity', 0)
                    .slideDown('slow')
                    .animate(
                        {opacity: 1},
                        {queue: false, duration: 'fast'}
                    );
            }

            // When the user clicks on <span> (x), close the modal
            rspan.onclick = function () {
                $(rmodal).fadeOut('fast');
            }
            lspan.onclick = function () {
                $(lmodal).fadeOut('fast');
            }

            // When the user clicks anywhere outside of the modal, close it
            window.onclick = function (event) {
                if (event.target == rmodal) {
                    $(rmodal).fadeOut('fast');
                }
                if (event.target == lmodal) {
                    $(lmodal).fadeOut('fast');
                }
            }
		}


        if (profile_form_check == true) {

            // profile form
            var nextmodal = document.getElementById('profile-form-modal-1');
            var nextbtn = document.getElementById('profile-next-btn');
            var nextbtn2 = document.getElementById('profile-next-btn-2');

            var backmodal = document.getElementById('profile-form-modal-2');
            var backbtn = document.getElementById('profile-back-btn');

            nextbtn.onclick = function () {
                nextmodal.style.display = "none";
                backmodal.style.display = "block";
                backmodal.style.zIndex = 99;

                $(backmodal)
                    .css('opacity', 0)
                    .animate(
                        {opacity: 1},
                        {queue: false, duration: 'fast'}
                    );
            }

            nextbtn2.onclick = function () {
                nextmodal.style.display = "none";
                backmodal.style.display = "block";
                backmodal.style.zIndex = 99;

                $(backmodal)
                    .css('opacity', 0)
                    .slideDown('slow')
                    .animate(
                        {opacity: 1},
                        {queue: false, duration: 'fast'}
                    );
            }

            backbtn.onclick = function () {
                backmodal.style.display = "none";
                nextmodal.style.display = "block";

                $(nextmodal)
                    .css('opacity', 0)
                    .animate(
                        {opacity: 1},
                        {queue: false, duration: 'fast'}
                    );
            }
        }
    };
	$(window).onload=loadModalAnimation();

});