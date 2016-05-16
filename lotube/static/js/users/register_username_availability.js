(function($) {
    const USERNAME_FIELD = $('#id_username');
    const ERROR_FIELD = $('#id_username_error_field');
    const BASE_URL = '/api/v2/users?username=';

    function paint(error, val) {
        ERROR_FIELD.text(error ? val + ' is taken' : '');
    }

    function check_username(val) {
        $.get(BASE_URL + val, function(data) {
            paint(data.count > 0, val);
        });
    }

    var delay = (function(){
        var timer = 0;
        return function(callback, ms){
            clearTimeout (timer);
            timer = setTimeout(callback, ms);
        };
    })();

    USERNAME_FIELD.change(function() {
        delay(function() {
            if (USERNAME_FIELD.val().length > 3)
                check_username(USERNAME_FIELD.val())
        }, 500);
    });
})(jQuery);