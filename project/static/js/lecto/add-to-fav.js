var AddToFav = function() {
    this.init();
};

AddToFav.prototype = {

    $element: null,
    isLiked: null,
    bookId: null,
    favedId: null,
    isBookmarksPage: $('#bookmarks-container').length > 0,

    init: function() {
        $('.favorite').each(function() {
            $(this).on('click', AddToFav.prototype.addHandler);
        });
    },

    save: function() {
        $.post(Const.URL + 'save-fav', {book_id: this.bookId, is_liked: this.isLiked, faved_id: this.favedId},
            function(data) {
                if (AddToFav.prototype.isBookmarksPage && !AddToFav.prototype.is_liked) {
                     AddToFav.prototype.removeUnliked();
                } else {
                    AddToFav.prototype.addFavedId(data.favedId);
                }
                PageController.prototype.updateCounters();
            }
        );
    },

    addFavedId: function(id) {
        AddToFav.prototype.$element.attr('data-faved-id', id);
    },

    removeUnliked: function() {
        this.$element.parents('div.recommend-item').slideUp('fast', function() {
            this.remove();
        });

    },

    addHandler: function(e) {

        AddToFav.prototype.$element = $(e.currentTarget);
        AddToFav.prototype.isLiked = !AddToFav.prototype.$element.hasClass('like');
        AddToFav.prototype.bookId = AddToFav.prototype.$element.attr('id').split('-')[2];
        AddToFav.prototype.favedId = AddToFav.prototype.$element.attr('data-faved-id');


        AddToFav.prototype.save();
    }

};

$('.recommendation-container').ready(function() {
    var addToFav = new AddToFav();
});