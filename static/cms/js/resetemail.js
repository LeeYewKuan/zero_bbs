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
              console.log(data)
          },
          'fail': function (errors) {
              console.log("errors")
          }
      })
  })
})