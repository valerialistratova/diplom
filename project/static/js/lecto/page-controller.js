var Const = {
    URL: ''
};

var PageController = function() {
    this.init();
};

PageController.prototype = {

    request: null,

    pageSelector: '#page-container',

    buttonSelector: '.button-icon',

    loaderSelector: '#loading',

    defaultPage: 'history',

    init: function() {

        this.updatePage(document.URL);

        $(window).on('hashchange', function(e) {
            PageController.prototype.updatePage(e.originalEvent.newURL);
        });
    },

    updatePage: function(newURL) {
        this.request = this.getRequestedAction(newURL);

        if (!this.request) {
            this.request = this.defaultPage;
        }

        this.retrieveHtml();

        this.highlightButton();

    },

    updateCounters: function() {
        $.post(Const.URL + 'get-counters', {}, function(data) {
            $('.button-icon.recommendation div').text(data.recommended);
            $('.button-icon.history div').text(data.history);
            $('.button-icon.bookmarks div').text(data.bookmarks);
        });
    },

    getRequestedAction: function(url) {
        var urlParts = url.split('#');

        if (urlParts.length == 2) {
            return urlParts[1];
        } else {
            return false;
        }
    },

    highlightButton: function() {
        $(this.buttonSelector).removeClass('active');
        $(this.buttonSelector + '.' + this.request).addClass('active');
    },

    retrieveHtml: function() {

        $(this.pageSelector + ' div').hide();
        $(this.loaderSelector).removeClass('hidden');


        $.ajax({
            type: 'POST',
            url: Const.URL + this.request,
            success: function(data) {
                $(PageController.prototype.pageSelector).html('');
                $(PageController.prototype.pageSelector).append(data);

                $(PageController.prototype.loaderSelector).addClass('hidden');
            }
        });
    }

};

$(window).ready(function() {
    var pageController = new PageController();
});