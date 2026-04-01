(function ($) {
    "use strict";

    // Smooth scrolling to section
    $(".btn-scroll").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            
            $('html, body').animate({
                scrollTop: $(this.hash).offset().top - 45
            }, 1500, 'easeInOutExpo');
        }
    });

    
    // Typed Initiate
    if ($('.typed-text-output').length == 1) {
        var typed_strings = $('.typed-text').text();
        var typed = new Typed('.typed-text-output', {
            strings: typed_strings.split(', '),
            typeSpeed: 100,
            backSpeed: 20,
            smartBackspace: false,
            loop: true
        });
    }
    
    
    // Skills
    $('.skill').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, {offset: '80%'});


    // Portfolio isotope and filter
    var portfolioIsotope = $('.portfolio-container').isotope({
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });
    $('#portfolio-flters li').on('click', function () {
        $("#portfolio-flters li").removeClass('active');
        $(this).addClass('active');

        portfolioIsotope.isotope({filter: $(this).data('filter')});
    });


 
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    // Contact Form Handling with EmailJS
    $('#contact-form').on('submit', function(event) {
        event.preventDefault();
        
        const $submitBtn = $('#submit-btn');
        const $formStatus = $('#form-status');
        
        // Show loading state
        $submitBtn.prop('disabled', true).text('Sending...');
        $formStatus.html('<div class="alert alert-info">Sending your message...</div>');

        // These IDs from your EmailJS account
        const serviceID = 'service_l60r7at';
        const templateID = 'template_7t19cdc';

        emailjs.sendForm(serviceID, templateID, this)
            .then(() => {
                $submitBtn.prop('disabled', false).text('Send Message');
                $formStatus.html('<div class="alert alert-success">Message sent successfully! I will get back to you soon.</div>');
                $('#contact-form')[0].reset(); // Clear form
                
                // Clear success message after 5 seconds
                setTimeout(() => {
                    $formStatus.fadeOut('slow', function() {
                        $(this).html('').show();
                    });
                }, 5000);
            }, (err) => {
                $submitBtn.prop('disabled', false).text('Send Message');
                $formStatus.html('<div class="alert alert-danger">Oops! Something went wrong. Please try again.</div>');
                console.error('EmailJS Error:', err);
            });
    });
})(jQuery);



// Portfolio Video Hover Mechanics
$(document).ready(function() {
    $('.portfolio-card').each(function() {
        var card = $(this);
        var video = card.find('.portfolio-hover-video').get(0);
        
        if(video) {
            card.on('mouseenter', function() {
                var playPromise = video.play();
                if (playPromise !== undefined) {
                    playPromise.catch(function(error) {
                        // Auto-play prevented
                        console.log("Video autoplay prevented:", error);
                    });
                }
            });
            
            card.on('mouseleave', function() {
                video.pause();
                video.currentTime = 0; // Rewind the clip!
            });
        }
    });
});
