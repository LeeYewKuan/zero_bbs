$(function () {
  $('#submit').click(function (event) {
      event.preventDefault()
      let emailE = $("input[name=email]");
      let captchaE = $("input[name=captcha]");

      let email = emailE.val();
      let captcha = captchaE.val();

      zeroajax.post({
          'url': "/cms/resetemail/",
          'data':{
              "email": email,
              "captcha": captcha
          },
          'success': function (data) {
             if (data['code'] == 200){
                 zeroalert.alertSuccessToast("邮箱修改成功")
             } else {
                 zeroalert.alertInfo(data['message'])
             }
          },
          'fail': function (errors) {
              zeroalert.alertNetworkError()
          }
      })
  })
})