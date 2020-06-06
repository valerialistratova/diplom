var RateBook = function() {
    this.init();
};

RateBook.prototype = {

    rate: null,
    bookId: null,

    ratings: {
        neutral: 0,
        negative: -1,
        positive: 1
    },

    init: function() {
        $('div.buttons button').on('click', RateBook.prototype.addHandler);
    },

    addHandler: function(element) {
        for (var rating in rateBook.ratings) {
            if ($(element.currentTarget).hasClass(rating)) {
                rateBook.rate = rateBook.ratings[rating];
                break;
            }
        }

        rateBook.bookId = $(element.currentTarget).parent('div').attr('data-book-id');
        rateBook.save();

    },

    save: function() {
        $.post(Const.URL + 'save-rate', {book_id: this.bookId, rate: this.rate}, function() {

        });
    }

};

var rateBook = new RateBook();
