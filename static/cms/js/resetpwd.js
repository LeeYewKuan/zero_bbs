//整个页面加载完毕，才会去执行这个界面
$(function () {
    $("#submit").click(function (event) {
        event.preventDefault();

        var oldpwdElement = $("input[name=oldpwd]");
        var newpwdElement = $("input[name=newpwd]");
        var newpwd2Element = $("input[name=newpwd2]");

        var oldpwd = oldpwdElement.val();
        var newpwd = newpwdElement.val();
        var newpwd2 = newpwd2Element.val();

        zeroajax.post({
            'url': '/cms/resetpwd/',
            'data':{
                'oldpwd': oldpwd,
                'newpwd': newpwd,
                'newpwd2': newpwd2
            },
            'success': function (data) {
                console.log(data)
            },
            'fail': function (error) {
                console.log(error)
            }
        })
    })


})