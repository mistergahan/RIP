(function($) {

	var win = $(window),
		ww = window.innerWidth,
		wh = window.innerHeight;

	var grid = {

		adjust: function() {
			var container = $('.gallery');

			for (var i = 0; i < container.length; i++) {
				// container
				var active_container = $(container[i]);

				// cols
				var cols = parseInt(active_container.data('cols'), 10);

				if (ww >= 1024) {
					if (!cols) cols = 3;
				} else if (ww > 800) {
					if (cols !== 1) cols = 2;
				} else {
					cols = 1;
				}

				// margin
				var margin = parseInt(active_container.data('margin'), 10);
				if (!margin) margin = 0;

				if (ww < 800) {
					if (margin > 10)
						margin = 10;
				}

				// set margin to the container
				active_container.css('padding', Math.floor(margin / 2));

				// height
				var height = parseFloat(active_container.data('height'));
				if (!height) height = 'auto';

				// double height
				var double_height = parseFloat(active_container.data('double-height'));
				if (!double_height) double_height = 2;

				// container width
				var container_width = active_container.width();

				// items
				var items = active_container.find('.entry'),
					items_width = Math.floor((container_width / cols) - margin),
					items_height = Math.floor(items_width * height),
					items_double_height = Math.floor(items_height * double_height),
					items_margin = Math.floor(margin / 2);

				items.each(function() {
					$(this).css('width', items_width);
					$(this).css('height', items_height);
					$(this).css('margin', items_margin);

					if ($(this).hasClass('h2') && ww > 800)
						$(this).css('height', items_double_height + margin);
					if ($(this).hasClass('w2') && ww > 800 && cols != 1)
						$(this).css('width', items_width * 2 + margin);
					if ($(this).hasClass('full')) {
						$(this).css('width', container_width - margin);
						if (height != 'auto')
							$(this).css('height', wh);
					}
				});

				// isotope
				active_container.isotope({
					itemSelector: '.entry',
					masonry: {
						columnWidth: items_width + margin
					}
				});

				// filter
				$('.filters li').on('click', function() {
					var filter = $(this).data('filter');

					$('.filters li').removeClass('active');
					$(this).addClass('active');

					active_container.isotope({
						filter: filter
					});
				});
			};
		}

	}

	win.on('load', function() {
		grid.adjust();
	});

	win.on('resize', function() {
		ww = window.innerWidth;
		wh = window.innerHeight;

		grid.adjust();
	});

})(jQuery);
