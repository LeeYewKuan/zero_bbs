'use static';

var zeroajax = {
    'get': function (args) {
        args['method'] = 'get';
        this.ajax(args);
    },
    'post': function (args) {
        args['method'] = 'post';
        this.ajax(args);
    },
    'ajax': function (args) {
        this._ajaxSetup();
        $.ajax(args)
    },
    '_ajaxSetup': function () {
        $.ajaxSetup({
            'beforeSend':function (xhr, settings) {
                if (!/^(GET|HEAD|OPETION|TRACT)$/i.test(settings.type) && !this.crossDomain){
                    var csrf_token = $('meta[name=csrf-token]').attr('content');
                    xhr.setRequestHeader('X-CSRFToken', csrf_token)
                }
            }
        })
    }
}