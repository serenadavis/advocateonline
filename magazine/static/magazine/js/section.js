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


// Archive

function make_archive_item(a) {
	var by = a.contributors.join(" ")
    var message = section() == "art" ? "See More >>" : "Continue Reading >>";
    var photo = a.photo ? `<a href="/content/${a.id}"><img src="${a.photo}" /></a>` : "";
	return $(
	  `<li class="archive-item">
      <span class="item-title"><a href="/content/${a.id}">${a.title}</a></span>
      <span class="item-author"><a href="/content/${a.id}">By ${by}</a></span>
      <span class="title-underline"></span>
      <div class="item-sample">${photo}${a.body}</div>
      <div class="shadow"></div>
      <div class="item-continue-reading"><a href="/content/${a.id}">${message}</a></div>
  	  </li>`
  	);
}

function fetch_articles(section, num, issue, cb) {
	issue = issue || ""
	var url = `/explore_archives?section=${section}&num=${num}&issue=${issue}`;
	$.getJSON(url, cb)
}

function section() {
	var parts = document.URL.split('/')
	var a = parts.pop()
	var b = parts.pop()
	return a == "" ? b : a
}

function issue() {
	var selected = $('.select-issue-dropdown').val()
	return selected == "all" ? undefined : selected
}

function fetch_and_insert_archive_items(section, num, issue, replace = false) {
	fetch_articles(section, num, issue, function(data) {
		var replace_cb = replace;
		if(replace_cb) {
			$('.archive').html("");
		}
		for (var i = data.result.length - 1; i >= 0; i--) {
			var a = make_archive_item(data.result[i])
			$('.archive').append(a);
		}
	})
}

function load_more_items(replace = false) {
	fetch_and_insert_archive_items(section(), 9, issue(), replace);
}

function update_archive_style() {
	if(issue() == undefined) {
		$('.load-more,.load-more-underline').addClass("all");
	} else {
		$('.load-more,.load-more-underline').removeClass("all");
	}
}

$(document).ready(function() {
	load_more_items()
	update_archive_style();
	$('.load-more').click(() => load_more_items());
	$('.select-issue-dropdown').change(function() {
		load_more_items(true);
		update_archive_style();
	});
});

