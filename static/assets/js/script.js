/*
Author       : Dreamguys
Template Name: POS - Bootstrap Admin Template
*/


$(document).ready(function(){

	// Variables declarations
	var $wrapper = $('.main-wrapper');
	var $slimScrolls = $('.slimscroll');
	var $pageWrapper = $('.page-wrapper');
	feather.replace();

	// Page Content Height Resize
	$(window).resize(function () {
		if ($('.page-wrapper').length > 0) {
			var height = $(window).height();
			$(".page-wrapper").css("min-height", height);
		}
	});

	// Mobile menu sidebar overlay
	$('body').append('<div class="sidebar-overlay"></div>');
	$(document).on('click', '#mobile_btn', function() {
		$wrapper.toggleClass('slide-nav');
		$('.sidebar-overlay').toggleClass('opened');
		$('html').addClass('menu-opened');
		$('#task_window').removeClass('opened');
		return false;
	});

	$(".sidebar-overlay").on("click", function () {
		$('html').removeClass('menu-opened');
		$(this).removeClass('opened');
		$wrapper.removeClass('slide-nav');
		$('.sidebar-overlay').removeClass('opened');
		$('#task_window').removeClass('opened');
	});

	// Logo Hide Btn

	$(document).on("click",".hideset",function () {
		$(this).parent().parent().parent().hide();
	});

	$(document).on("click",".delete-set",function () {
		$(this).parent().parent().hide();
	});

	// Owl Carousel
	if($('.product-slide').length > 0 ){
		$('.product-slide').owlCarousel({
			items: 1,
			margin: 30,
			dots : false,
			nav: true,
			loop: false,
			responsiveClass:true,
			responsive: {
				0: {
					items: 1
				},
				800 : {
					items: 1
				},
				1170: {
					items: 1
				}
			}
		});
	}

	//Home popular
	if($('.owl-product').length > 0 ){
		var owl = $('.owl-product');
			owl.owlCarousel({
			margin: 10,
			dots : false,
			nav: true,
			loop: false,
			touchDrag:false,
			mouseDrag  : false,
			responsive: {
				0: {
					items: 2
				},
				768 : {
					items: 4
				},
				1170: {
					items: 8
				}
			}
		});
	}
	// Datatable
	if($('.datanew').length > 0) {
		$('.datanew').DataTable({
			"bFilter": true,
			"sDom": 'fBtlpi',
			'pagingType': 'numbers',
			"ordering": true,
			"language": {
				search: ' ',
				sLengthMenu: '_MENU_',
				searchPlaceholder: "Search...",
				info: "_START_ - _END_ of _TOTAL_ items",
			 },
			initComplete: (settings, json)=>{
				$('.dataTables_filter').appendTo('#tableSearch');
				$('.dataTables_filter').appendTo('.search-input');
			},
		});
	}

	// image file upload image
	function readURL(input) {
		if (input.files && input.files[0]) {
			var reader = new FileReader();

			reader.onload = function (e) {
				$('#blah').attr('src', e.target.result);
			}

			reader.readAsDataURL(input.files[0]);
		}
	}

	$("#imgInp").change(function(){
		readURL(this);
	});


	if($('.datatable').length > 0) {
		$('.datatable').DataTable({
			"bFilter": false
		});
	}
	// Loader
	setTimeout(function () {
		$('#global-loader');
		setTimeout(function () {
			$("#global-loader").fadeOut("slow");
		}, 100);
	}, 500);

	// Datetimepicker
	if($('.datetimepicker').length > 0 ){
		$('.datetimepicker').datetimepicker({
			format: 'DD-MM-YYYY',
			icons: {
				up: "fas fa-angle-up",
				down: "fas fa-angle-down",
				next: 'fas fa-angle-right',
				previous: 'fas fa-angle-left'
			}
		});
	}

	// toggle-password
	if($('.toggle-password').length > 0) {
		$(document).on('click', '.toggle-password', function() {
			$(this).toggleClass("fa-eye fa-eye-slash");
			var input = $(".pass-input");
			if (input.attr("type") == "password") {
				input.attr("type", "text");
			} else {
				input.attr("type", "password");
			}
		});
	}
	if($('.toggle-passwords').length > 0) {
		$(document).on('click', '.toggle-passwords', function() {
			$(this).toggleClass("fa-eye fa-eye-slash");
			var input = $(".pass-inputs");
			if (input.attr("type") == "password") {
				input.attr("type", "text");
			} else {
				input.attr("type", "password");
			}
		});
	}
	if($('.toggle-passworda').length > 0) {
		$(document).on('click', '.toggle-passworda', function() {
			$(this).toggleClass("fa-eye fa-eye-slash");
			var input = $(".pass-inputs");
			if (input.attr("type") == "password") {
				input.attr("type", "text");
			} else {
				input.attr("type", "password");
			}
		});
	}

	// Select 2
	if ($('.select').length > 0) {
		$('.select').select2({
			minimumResultsForSearch: -1,
			width: '100%'
		});
	}

	// Counter
	if($('.counter').length > 0) {
		$('.counter').counterUp({
			delay: 20,
			time: 2000
		});
	}
	if($('#timer-countdown').length > 0) {
		$( '#timer-countdown' ).countdown( {
			from: 180, // 3 minutes (3*60)
			to: 0, // stop at zero
			movingUnit: 1000, // 1000 for 1 second increment/decrements
			timerEnd: undefined,
			outputPattern: '$day Day $hour : $minute : $second',
			autostart: true
		});
	}

	if($('#timer-countup').length > 0) {
		$( '#timer-countup' ).countdown( {
			from: 0,
			to: 180
		});
	}

	if($('#timer-countinbetween').length > 0) {
		$( '#timer-countinbetween' ).countdown( {
			from: 30,
			to: 20
		});
	}

	if($('#timer-countercallback').length > 0) {
		$( '#timer-countercallback' ).countdown( {
			from: 10,
			to: 0,
			timerEnd: function() {
				this.css( { 'text-decoration':'line-through' } ).animate( { 'opacity':.5 }, 500 );
			}
		});
	}

	if($('#timer-outputpattern').length > 0) {
		$( '#timer-outputpattern' ).countdown( {
			outputPattern: '$day Days $hour Hour $minute Min $second Sec..',
			from: 60 * 60 * 24 * 3
		});
	}

	// Summernote

	if($('#summernote').length > 0) {
		$('#summernote').summernote({
		height: 300,                 // set editor height
		minHeight: null,             // set minimum height of editor
		maxHeight: null,             // set maximum height of editor
		focus: true                  // set focus to editable area after initializing summernote
		});
	}



	// Sidebar Slimscroll
	if($slimScrolls.length > 0) {
		$slimScrolls.slimScroll({
			height: 'auto',
			width: '100%',
			position: 'right',
			size: '7px',
			color: '#ccc',
			wheelStep: 10,
			touchScrollStep: 100
		});
		var wHeight = $(window).height() - 60;
		$slimScrolls.height(wHeight);
		$('.sidebar .slimScrollDiv').height(wHeight);
		$(window).resize(function() {
			var rHeight = $(window).height() - 60;
			$slimScrolls.height(rHeight);
			$('.sidebar .slimScrollDiv').height(rHeight);
		});
	}

	// Sidebar
	var Sidemenu = function() {
		this.$menuItem = $('#sidebar-menu a');
	};

	function init() {
		var $this = Sidemenu;
		$('#sidebar-menu a').on('click', function(e) {
			if($(this).parent().hasClass('submenu')) {
				e.preventDefault();
			}
			if(!$(this).hasClass('subdrop')) {
				// $('ul', $(this).parents('ul:first')).slideUp(250);
				$('a', $(this).parents('ul:first')).removeClass('subdrop');
				$(this).next('ul').slideDown(350);
				$(this).addClass('subdrop');
			} else if($(this).hasClass('subdrop')) {
				$(this).removeClass('subdrop');
				$(this).next('ul').slideUp(350);
			}
		});
		$('#sidebar-menu ul li.submenu a.active').parents('li:last').children('a:first').addClass('active').trigger('click');
	}

	// Sidebar Initiate
	init();
	$(document).on('mouseover', function(e) {
        e.stopPropagation();
        if ($('body').hasClass('mini-sidebar') && $('#toggle_btn').is(':visible')) {
            var targ = $(e.target).closest('.sidebar, .header-left').length;
            if (targ) {
                $('body').addClass('expand-menu');
                $('.subdrop + ul').slideDown();
            } else {
                $('body').removeClass('expand-menu');
                $('.subdrop + ul').slideUp();
            }
            return false;
        }
    });

	//toggle_btn
	$(document).on('click', '#toggle_btn', function() {
		if ($('body').hasClass('mini-sidebar')) {
			$('body').removeClass('mini-sidebar');
			$(this).addClass('active');
			$('.subdrop + ul');
			localStorage.setItem('screenModeNightTokenState', 'night');
			setTimeout(function() {
				$("body").removeClass("mini-sidebar");
				$(".header-left").addClass("active");
			}, 100);
		} else {
			$('body').addClass('mini-sidebar');
			$(this).removeClass('active');
			$('.subdrop + ul');
			localStorage.removeItem('screenModeNightTokenState', 'night');
			setTimeout(function() {
				$("body").addClass("mini-sidebar");
				$(".header-left").removeClass("active");
			}, 100);
		}
		return false;
	});


	if (localStorage.getItem('screenModeNightTokenState') == 'night') {
		setTimeout(function() {
			$("body").removeClass("mini-sidebar");
			$(".header-left").addClass("active");
		}, 100);
	}

	$('.submenus').on('click', function(){
		$('body').addClass('sidebarrightmenu');
	});

	$('#searchdiv').on('click', function(){
		$('.searchinputs').addClass('show');
	});
	$('.search-addon span').on('click', function(){
		$('.searchinputs').removeClass('show');
	});
	$(document).on('click', '#filter_search', function() {
		$('#filter_inputs').slideToggle("slow");
	});
	$(document).on('click', '#filter_search1', function() {
		$('#filter_inputs1').slideToggle("slow");
	});
	$(document).on('click', '#filter_search2', function() {
		$('#filter_inputs2').slideToggle("slow");
	});
	$(document).on('click', '#filter_search', function() {
		$('#filter_search').toggleClass("setclose");
	});
	$(document).on("click",".productset",function () {
		$(this).toggleClass("active");
	});



	//Increment Decrement value
	$('.inc.button').click(function(){
	    var $this = $(this),
	        $input = $this.prev('input'),
	        $parent = $input.closest('div'),
	        newValue = parseInt($input.val())+1;
	    $parent.find('.inc').addClass('a'+newValue);
	    $input.val(newValue);
	    newValue += newValue;
	});
	$('.dec.button').click(function(){
	    var $this = $(this),
	        $input = $this.next('input'),
	        $parent = $input.closest('div'),
	        newValue = parseInt($input.val())-1;
	    console.log($parent);
	    $parent.find('.inc').addClass('a'+newValue);
	    $input.val(newValue);
	    newValue += newValue;
	});

	if($('.custom-file-container').length > 0) {
		//First upload
		var firstUpload = new FileUploadWithPreview('myFirstImage')
		//Second upload
		var secondUpload = new FileUploadWithPreview('mySecondImage')
	}

	$('.counters').each(function() {
		var $this = $(this),
			countTo = $this.attr('data-count');
		$({ countNum: $this.text()}).animate({
			countNum: countTo
		},
		{
			duration: 2000,
			easing:'linear',
			step: function() {
			$this.text(Math.floor(this.countNum));
			},
			complete: function() {
			$this.text(this.countNum);
			}

		});

	});


	// toggle-password
	if($('.toggle-password').length > 0) {
		$(document).on('click', '.toggle-password', function() {
			$(this).toggleClass("fa-eye fa-eye");
			var input = $(".pass-input");
			if (input.attr("type") == "text") {
				input.attr("type", "text");
			} else {
				input.attr("type", "password");
			}
		});
	}


	if($('.win-maximize').length > 0) {
		$('.win-maximize').on('click', function(e){
			if (!document.fullscreenElement) {
				document.documentElement.requestFullscreen();
			} else {
				if (document.exitFullscreen) {
					document.exitFullscreen();
				}
			}
		})
	}


	$(document).on('click', '#check_all', function() {
		$('.checkmail').click();
		return false;
	});
	if($('.checkmail').length > 0) {
		$('.checkmail').each(function() {
			$(this).on('click', function() {
				if($(this).closest('tr').hasClass('checked')) {
					$(this).closest('tr').removeClass('checked');
				} else {
					$(this).closest('tr').addClass('checked');
				}
			});
		});
	}

	// Popover
	if($('.popover-list').length > 0) {
		var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
		var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
		return new bootstrap.Popover(popoverTriggerEl)
		})
	}

	// Clipboard
	if($('.clipboard').length > 0) {
		var clipboard = new Clipboard('.btn');
	}

	// Chat
	var chatAppTarget = $('.chat-window');
	(function() {
		if ($(window).width() > 991)
			chatAppTarget.removeClass('chat-slide');

		$(document).on("click",".chat-window .chat-users-list a.media",function () {
			if ($(window).width() <= 991) {
				chatAppTarget.addClass('chat-slide');
			}
			return false;
		});
		$(document).on("click","#back_user_list",function () {
			if ($(window).width() <= 991) {
				chatAppTarget.removeClass('chat-slide');
			}
			return false;
		});
	})();

	// Mail important

	$(document).on('click', '.mail-important', function() {
		$(this).find('i.fa').toggleClass('fa-star').toggleClass('fa-star-o');
	});


	var selectAllItems = "#select-all";
	var checkboxItem = ":checkbox";
	$(selectAllItems).click(function() {

		if (this.checked) {
		$(checkboxItem).each(function() {
			this.checked = true;
		});
		} else {
		$(checkboxItem).each(function() {
			this.checked = false;
		});
		}

	});

	// Tooltip
	if($('[data-bs-toggle="tooltip"]').length > 0) {
		var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
		var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
			return new bootstrap.Tooltip(tooltipTriggerEl)
		})
	}


    $("body").append(right_side_views);

	// Sidebar Visible

	$('.open-layout').on("click", function (s) {
		s.preventDefault();
		$('.sidebar-layout').addClass('show-layout');
		$('.sidebar-settings').removeClass('show-settings');
	});
	$('.btn-closed').on("click", function (s) {
		s.preventDefault();
		$('.sidebar-layout').removeClass('show-layout');
	});
	$('.open-settings').on("click", function (s) {
		s.preventDefault();
		$('.sidebar-settings').addClass('show-settings');
		$('.sidebar-layout').removeClass('show-layout');
	});

	$('.btn-closed').on("click", function (s) {
		s.preventDefault();
		$('.sidebar-settings').removeClass('show-settings');
	});

	$('.open-siderbar').on("click", function (s) {
		s.preventDefault();
		$('.siderbar-view').addClass('show-sidebar');
	});

	$('.btn-closed').on("click", function (s) {
		s.preventDefault();
		$('.siderbar-view').removeClass('show-sidebar');
	});

	if($('.toggle-switch').length > 0) {
		const toggleSwitch = document.querySelector('.toggle-switch input[type="checkbox"]');
		const currentTheme = localStorage.getItem('theme');
		var app = document.getElementsByTagName("BODY")[0];

		if (currentTheme) {
			app.setAttribute('data-theme', currentTheme);

			if (currentTheme === 'dark') {
				toggleSwitch.checked = true;
			}
		}

		function switchTheme(e) {
			if (e.target.checked) {
				app.setAttribute('data-theme', 'dark');
				localStorage.setItem('theme', 'dark');
			}
			else {
				app.setAttribute('data-theme', 'light');
				localStorage.setItem('theme', 'light');
			}
		}

		toggleSwitch.addEventListener('change', switchTheme, false);
	}

	if(window.location.hash == "#LightMode"){
		localStorage.setItem('theme', 'dark');
	}
	else {
		if(window.location.hash == "#DarkMode"){
			localStorage.setItem('theme', 'light');
		}
	}


	$('ul.tabs li').click(function(){
		var $this = $(this);
		var $theTab = $(this).attr('id');
		console.log($theTab);
		if($this.hasClass('active')){
		  // do nothing
		} else{
		  $this.closest('.tabs_wrapper').find('ul.tabs li, .tabs_container .tab_content').removeClass('active');
		  $('.tabs_container .tab_content[data-tab="'+$theTab+'"], ul.tabs li[id="'+$theTab+'"]').addClass('active');
		}

	});



$("body").append(customize_link);

$('.add-setting').on("click", function (e) {
	e.preventDefault();
	$('.preview-toggle.sidebar-settings').addClass('show-settings');
});
$('.sidebar-close').on("click", function (e) {
	e.preventDefault();
	$('.preview-toggle.sidebar-settings').removeClass('show-settings');
});
$('.navigation-add').on("click", function (e) {
	e.preventDefault();
	$('.nav-toggle.sidebar-settings').addClass('show-settings');
});
$('.sidebar-close').on("click", function (e) {
	e.preventDefault();
	$('.nav-toggle.sidebar-settings').removeClass('show-settings');
});

// DarkMode with LocalStorage
if($('#dark-mode-toggle').length > 0) {
	$("#dark-mode-toggle").children(".light-mode").addClass("active");
	let darkMode = localStorage.getItem('darkMode');

	const darkModeToggle = document.querySelector('#dark-mode-toggle');

	const enableDarkMode = () => {
		document.body.setAttribute('data-theme', 'dark');
		$("#dark-mode-toggle").children(".dark-mode").addClass("active");
		$("#dark-mode-toggle").children(".light-mode").removeClass("active");
		localStorage.setItem('darkMode', 'enabled');
	}

	const disableDarkMode = () => {
	  document.body.removeAttribute('data-theme', 'dark');
		$("#dark-mode-toggle").children(".dark-mode").removeClass("active");
		$("#dark-mode-toggle").children(".light-mode").addClass("active");
	  localStorage.setItem('darkMode', null);
	}

	if (darkMode === 'enabled') {
		enableDarkMode();
	}

	darkModeToggle.addEventListener('click', () => {
	  darkMode = localStorage.getItem('darkMode');

	  if (darkMode !== 'enabled') {
		enableDarkMode();
	  } else {
		disableDarkMode();
	  }
	});
}


});
function toggleFullscreen(elem) {
	elem = elem || document.documentElement;
	if (!document.fullscreenElement && !document.mozFullScreenElement &&
	  !document.webkitFullscreenElement && !document.msFullscreenElement) {
	  if (elem.requestFullscreen) {
		elem.requestFullscreen();
	  } else if (elem.msRequestFullscreen) {
		elem.msRequestFullscreen();
	  } else if (elem.mozRequestFullScreen) {
		elem.mozRequestFullScreen();
	  } else if (elem.webkitRequestFullscreen) {
		elem.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
	  }
	} else {
	  if (document.exitFullscreen) {
		document.exitFullscreen();
	  } else if (document.msExitFullscreen) {
		document.msExitFullscreen();
	  } else if (document.mozCancelFullScreen) {
		document.mozCancelFullScreen();
	  } else if (document.webkitExitFullscreen) {
		document.webkitExitFullscreen();
	  }
	}
  }

  document.getElementById('btnFullscreen').addEventListener('click', function() {
	toggleFullscreen();
  });






