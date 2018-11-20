$(function () {
    $('#email_captcha').click(function (event) {
        event.preventDefault();

        email = $('input[name=email]').val();

        if (!email){
            zeroalert.alertInfoToast("邮箱不能为空!");
            return;
        }

        zeroajax.get({
            "url": "/cms/email_captcha/",
            "data": {
                "email": email
            },
            "success": function (data) {
                if(data["code"] == 200){
                    zeroalert.alertSuccessToast("验证码已发送到您邮箱，请查收！")
                } else {
                    zeroalert.alertInfo(data['message'])
                }
            },
            "fail": function (errors) {
                zeroalert.alertNetworkError()
            }
        })
    })
})