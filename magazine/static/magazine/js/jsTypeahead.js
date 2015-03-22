$(document).ready(function() {
    var authors = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        local: $.map({{typeahead_authors | safe}}, function(author) {return { name: author }; })
    });
    
    var titles = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('title'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        local: $.map({{typeahead_titles | safe}}, function(content) {return { title: content}; })
    });
    
    authors.initialize();
    titles.initialize();
    
    $('input.typeahead').typeahead({
        hint: true,
        highlight: true,
        minLength: 1
    },
    {
        name: 'Authors',
        highlight: true,
        displayKey: 'name',
        source: authors.ttAdapter(),
        templates: { header: '<h3 class="typeahead-datasets">Authors</h3>' }
    },
    {
        name: 'Titles',
        displayKey: 'title',
        source: titles.ttAdapter(),
        templates: { header: '<h3 class="typeahead-datasets">Titles</h3>' }
    });
});
