(function($) {

	"use strict";

	var win = $(window),
		ww = window.innerWidth,
		wh = window.innerHeight;



	/** play loader
	================================================== **/

	function play_loader() {
		setTimeout(function() {
			$('#header').find('.loader').fadeOut('slow', function() {
				$('#header').addClass('loaded');
			});
		}, 1000);
	}


	/** ajax
	================================================== **/

	function ajax_link() {
		var page;

		$('body').on('click', '.ajax-link', function() {
			page = $(this).attr('href');

			ajax(page);

			return false;
		});

		win.on('popstate', function() {
			page = location.href;

			ajax(page);
		});

		function ajax(page) {
			$('#header').find('.loader').fadeIn('slow');
			$('#header').removeClass('loaded open');

			toggle_nav(false);

			$.ajax({
				url: page,
				success: function(data) {
					var page_title = data.match(/<title>(.*?)<\/title>/);

					setTimeout(function() {
						if (location.href != page)
							history.pushState("", "", page);

						$('#wrapper').load(page + ' #inner', function() {
							win.trigger('load');
							document.title = page_title[1];

							$('html, body').animate({
								scrollTop: 0
							}, 100);
						});
					}, 1000);
				}
			});
		}
	}

	ajax_link();


	/** open/close nav
	================================================== **/

	$('.trigger').on('click', function() {
		if (!$('.site-nav').hasClass('visible')) {
			toggle_nav(true);
		} else {
			toggle_nav(false);
		}
	});

	$('#wrapper').on('click', function() {
		toggle_nav(false);
	});

	function toggle_nav(bool) {
		if (bool == true) {
			$('#header').addClass('open');
			$('#wrapper').addClass('overlay');
			$('body').addClass('no-scroll');
			setTimeout(function() {
				$('.site-nav').addClass('visible');
			}, 400);
		}

		if (bool == false) {
			$('.site-nav').removeClass('visible');
			setTimeout(function() {
				$('#header').removeClass('open');
				$('#wrapper').removeClass('overlay');
				$('.menu li').find('ul').slideUp(200);
			}, 200);
			setTimeout(function() {
				$('body').removeClass('no-scroll');
			}, 400);
		}
	}

	$('.menu li:has(ul)').find('a').on('click', function() {
		var parent = $(this).parent(),
			submenu = $(this).next('ul');

		if (submenu.is(':visible')) {
			parent.find('ul').slideUp(200);
		}

		if (submenu.is(':hidden')) {
			parent.siblings().find('ul').slideUp(200);
			submenu.slideDown(200);
		}

		if (parent.children('ul').length == 0) {
			return true;
		} else {
			return false;
		}
	});


	/** background images
	================================================== **/

	function image_bg() {
		$('.iBG').each(function() {
			var image = $(this).data('img');

			$(this).css({
				'background-image': 'url(' + image + ')',
				'background-size': 'cover',
				'background-position': '50% 50%',
				'background-repeat': 'no-repeat'
			});
		});
	}


	/** hero heights
	================================================== **/

	function hero_heights() {
		if ($('.hero').hasClass('small')) {
			var height = wh * 0.6;
			$('.hero').css('height', height + 'px');
		} else if ($('.hero').hasClass('medium')) {
			var height = wh * 0.7;
			$('.hero').css('height', height + 'px');
		} else {
			$('.hero').css('height', wh + 'px');
		}
	}


	/** windows
	================================================== **/

	win.on('load', function() {
		play_loader();

		image_bg();
		hero_heights();
	});

	win.on('resize', function() {
		ww = window.innerWidth;
		wh = window.innerHeight;

		hero_heights();
	});

})(jQuery);
