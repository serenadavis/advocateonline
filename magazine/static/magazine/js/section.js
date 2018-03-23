"use strict";

// Feature slider:

var LINK_SELECT_CLASS = "selected";
var DISPLAY_SELECT_CLASS = "selected";
var LINKING_ATTRIBUTE = "data-item-id";

$(document).ready(function() {
	$('.featured-item-links li').on('click', function(event) {
		var $target = $(this)
		var item_id = $target.attr(LINKING_ATTRIBUTE)
		$('.featured-item').removeClass(DISPLAY_SELECT_CLASS);
		$('.featured-item[' + LINKING_ATTRIBUTE + '=' + item_id + ']')
			.addClass(DISPLAY_SELECT_CLASS);
		$('.featured-item-links li').removeClass(LINK_SELECT_CLASS)
		$('.featured-item-links li[' + LINKING_ATTRIBUTE + '=' + item_id + ']').addClass(LINK_SELECT_CLASS)
	});
});