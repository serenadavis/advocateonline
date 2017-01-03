jQuery(document).ready(function ($) {
	var contentSections = $('.cd-section'),
		vNavigationItems = $('#cd-vertical-nav a');
	hNavigationItems = $('#cd-horizontal-nav a');
	pathLinks = $('.path a');

	var section = 1;
	var subsection = 0;

	vUpdateNavigation();

	//smooth scroll to the section
	vNavigationItems.on('click', function (event) {
		event.preventDefault();
		smoothScroll($(this.hash));
	});

	//smooth scroll to the section
	pathLinks.on('click', function (event) {
		event.preventDefault();
		smoothScroll($(this.hash));
	});

	// shift shown content horizontally
	hNavigationItems.on('click', function (event) {
		event.preventDefault();
		toggleHNavigation($(this));

	});
	

	// smooth scroll on scroll
	$(window).on('scroll', function(event) {
		vUpdateNavigation();
	});

	function vUpdateNavigation() {
		contentSections.each(function () {
			$this = $(this);
			var activeSection = $('#cd-vertical-nav a[href="#' + $this.attr('id') + '"]').data('number');
			if (($this.offset().top - $(window).height() / 2 < $(window).scrollTop()) && ($this.offset().top + $this.height() - $(window).height() / 2 > $(window).scrollTop())) {
				$this.addClass('visible');
				vNavigationItems.eq(activeSection).addClass('is-selected');
				section = activeSection;
			} else {
				$this.removeClass('visible');
				vNavigationItems.eq(activeSection).removeClass('is-selected');
			}
		});

		if (section > 0) {
			$('#cd-vertical-nav').removeClass("hidden");
			setHNavigation();
		} else {
			$('#cd-vertical-nav').addClass("hidden");
			subsection = 0;
			makeHVisible(0);
		}
	}

	function toggleHNavigation(link) {
		var id = link.attr('href');
		subsection = link.data('number');
		makeHVisible(subsection);
		link.addClass('is-selected');
	}

	function makeHVisible(subsection) {
		var subSections = $('.subsections li');
		subSections.each(function () {
			$this = $(this);
			if ($this.data('number') == subsection) {
				$this.addClass('is-visible');
			} else {
				$this.removeClass('is-visible');
			}
		});

		hNavigationItems.each(function () {
			$(this).removeClass('is-selected');
		});
	}

	function setHNavigation() {
		var current = "#subsection" + section.toString() + subsection.toString();
		
		var currentHNav = $('.visible #cd-horizontal-nav a');
		currentHNav.each(function () {
			$this = $(this);
			if ($this.attr('href') == current) {
				toggleHNavigation($this);
			}
		});
	}


	function smoothScroll(target) {
		$('body,html').animate(
			{ 'scrollTop': target.offset().top },
			600, vUpdateNavigation
		);
	}

	// function scrollHijacking(event) {
	// 	console.log("Scroll Hijacking!");
	// 	// on mouse scroll - check if animate section
	// 	if (event.originalEvent.detail < 0 || event.originalEvent.wheelDelta > 0) {
	// 		delta--;
	// 		(Math.abs(delta) >= scrollThreshold) && prevSection();
	// 	} else {
	// 		delta++;
	// 		(delta >= scrollThreshold) && nextSection();
	// 	}
	// 	return false;
	// }

	// function nextSection(event) {
	// 	console.log("Next Section!");
	// 	//go to previous section
	// 	typeof event !== 'undefined' && event.preventDefault();
	// 	var visibleSection = contentSections.filter('.visible');
	// 	if (visibleSection && visibleSection.next('.cd-section')) {
	// 		console.log(visibleSection.next('.cd-section'));
	// 		smoothScroll(visibleSection.next('.cd-section'));
	// 	}
	// }

	// function prevSection(event) {
	// 	console.log("Prev Section!");
	// 	//go to previous section
	// 	typeof event !== 'undefined' && event.preventDefault();
	// 	var visibleSection = contentSections.filter('.visible');
	// 	if (visibleSection && visibleSection.prev('.cd-section')) {
	// 		console.log(visibleSection.prev('.cd-section'));
	// 		smoothScroll(visibleSection.prev('.cd-section'));
	// 	}
	// }
});