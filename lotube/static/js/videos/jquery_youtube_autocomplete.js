(function($) {
    var API_KEY = "AIzaSyCHl8hhcCJ8SgcjQqEKwvXBdLmTxSER_8M";
    var BASE_URL = "http://suggestqueries.google.com/complete/search?hl=en" +
        "&ds=yt&client=youtube&hjson=t&cp=1&key="+API_KEY+
        "&format=5&alt=json&callback=?";

    $( "#search" ).autocomplete({
        source: function (request, response) {
            $.ajax({
                url: BASE_URL,
                dataType: "jsonp",
                data: {
                    q: request.term
                },
                success: function (data) {
                    results = data[1].map(function (current) {
                        return current[0];
                    });
                    response(results);
                }
            });
        },
        minLength: 3,
        select: function (event, ui) {
            var self = $(this);
            $(this).val(this.value);
            setTimeout(function() {
                self.closest($('form')).submit();
            }, 100); // doesn't work on Chrome without a timer
        }
    });
})(jQuery);