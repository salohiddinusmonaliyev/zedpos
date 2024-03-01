/*** TABLE OF CONTENTS
======================================================
    0 / general
    1 / menu toggle
    2 / dropdown
    3 / call the slick functions
    4 / all the  feather icons function
    6 / call  Lazy function
    7 /  call  Typed function
    8 /  call  StickySidebar function
    9 /  call perfect-scrollbar function
    =================================================== ***/
    $(function () {
        ("use strict");
    
            // ============================= menu toggle
            $(".menu-toggle-icon").on("click", function () {
                $(".mb-overlay").addClass("mb-visible");
            });
            $(".mb-overlay-bg , .close-mb-menu").on("click", function () {
                $(".mb-overlay").removeClass("mb-visible");
            });
    
                    // ============================= menu toggle
                    $(".add_to_cart_toggle").on("click", function () {
                        $(".add_to_cart_menu").toggleClass("block");
                    });
        
            // ================= dropdown
            $('.has-dropdown-m').on("click",function(e) {
                e.preventDefault();
              let $this = $(this);
            
              if ($this.next().hasClass('show')) {
                  $this.next().removeClass('show');
                  $this.next().slideUp(350);
              } else {
                  $this.parent().parent().find('li .dropdown-mobile').removeClass('show');
                  $this.parent().parent().find('li .dropdown-mobile').slideUp(350);
                  $this.next().toggleClass('show');
                  $this.next().slideToggle(350);
              }
          });
    
        // =============================  menu toggle
        $(".menu_icon").on("click", function () {
            $(".menu_elements").toggleClass("is_active");
            $(this).toggleClass("menu_icon_active");
    
        });
    
        // =============================  call  Typed function
        var typed = new Typed(".typed", {
            strings: ["hisob-kitobda adashmaysiz", "kirim-chiqimlarni bir joyda kuzatasiz", "sof foydangizni bilib olasiz"],
            typeSpeed: 55,
            backSpeed: 10,
            loop: true,
            loopCount: Infinity,
            backDelay: 1500,
            showCursor: true,
            offset: 0,
    
        });
    
        // ============================  call the slick functions
        $('.work-boxes-slick').slick({
            infinite: true,
            slidesToShow: 3,
            slidesToScroll: 1,
            dots: true,
            autoplay: true,
            autoplaySpeed: 2000,
            arrows: false,
            responsive: [{
                breakpoint: 950,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
                // You can unslick at a given breakpoint now by adding:
                // settings: "unslick"
                // instead of a settings object
            ]
    
        });
        $('.market_slick').slick({
            infinite: true,
            slidesToShow: 3,
            slidesToScroll: 1,
            dots: true,
            autoplay: true,
            autoplaySpeed: 2000,
            arrows: false,
            responsive: [{
                breakpoint: 950,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
                // You can unslick at a given breakpoint now by adding:
                // settings: "unslick"
                // instead of a settings object
            ]
    
        });
        $('.testi-boxes-slick').slick({
            infinite: true,
            slidesToShow: 3,
            slidesToScroll: 1,
            dots: true,
            autoplay: true,
            autoplaySpeed: 2000,
            arrows: false,
            responsive: [{
                breakpoint: 950,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
                // You can unslick at a given breakpoint now by adding:
                // settings: "unslick"
                // instead of a settings object
            ]
    
        });
        $('.blog-boxes-slick').slick({
            infinite: true,
            slidesToShow: 3,
            slidesToScroll: 1,
            dots: true,
            autoplay: true,
            autoplaySpeed: 2000,
            arrows: false,
            responsive: [{
                breakpoint: 950,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 760,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
                // You can unslick at a given breakpoint now by adding:
                // settings: "unslick"
                // instead of a settings object
            ]
    
        });
        $('.feautures-boxes-slick').slick({
            infinite: true,
            slidesToShow: 4,
            slidesToScroll: 1,
            dots: true,
            autoplay: true,
            autoplaySpeed: 2000,
            arrows: false,
            responsive: [{
                breakpoint: 950,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
                // You can unslick at a given breakpoint now by adding:
                // settings: "unslick"
                // instead of a settings object
            ]
    
        });
        $('.clients-slick').slick({
            infinite: true,
            slidesToShow: 1,
            slidesToScroll: 1,
            dots: true,
            autoplay: true,
            autoplaySpeed: 3000,
            arrows: false,
            responsive: [{
                breakpoint: 950,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
                // You can unslick at a given breakpoint now by adding:
                // settings: "unslick"
                // instead of a settings object
            ]
    
        });
    });
    
    $(".has-submenu").on({
        mouseenter: function () {
            $(".sub-nav", this).addClass("visible");
        },
        mouseleave: function () {
            $(".sub-nav", this).removeClass('visible');
        }
    });
    
    
    $(document).ready(function () {
        var count = 0;
        var counter = setInterval(function () {
            if (count < 101) {
                $('.count').text(count + '%');
                $('.loader').css('width', count + '%');
                count++;
            }
            else {
                clearInterval(counter);
            }
        }, 30);
    });
    
    
    // ============================  5/ call  perfect-scrollbar function
    
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
    
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    function makeTimer() {
    
        //		var endTime = new Date("29 April 2018 9:56:00 GMT+01:00");	
        var endTime = new Date("29 April 2020 9:56:00 GMT+01:00");
        endTime = (Date.parse(endTime) / 1000);
    
        var now = new Date();
        now = (Date.parse(now) / 1000);
    
        var timeLeft = endTime - now;
    
        var days = Math.floor(timeLeft / 86400);
        var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
        var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600)) / 60);
        var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));
    
        if (hours < "10") { hours = "0" + hours; }
        if (minutes < "10") { minutes = "0" + minutes; }
        if (seconds < "10") { seconds = "0" + seconds; }
    
        $("#days").html(days + "<span></span>");
        $("#hours").html(hours + "<span></span>");
        $("#minutes").html(minutes + "<span></span>");
        $("#seconds").html(seconds + "<span></span>");
    
    }
    
    setInterval(function () { makeTimer(); }, 1000);
    
    
    
            // ============================ 3/ call the slick functions
            $('.reviews_slick').slick({
                infinite: true,
                slidesToShow: 3,
                centerMode: true,
                slidesToScroll: 1,
                dots: true,
                autoplaySpeed: 2000,
                arrows: true,
                responsive: [{
                    breakpoint: 950,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 700,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                }
                    // You can unslick at a given breakpoint now by adding:
                    // settings: "unslick"
                    // instead of a settings object
                ]
    
            });