from flask import jsonify


class HttpCode(object):
    ok = 200
    un_auth_error = 401
    params_error = 400
    server_error = 500


def restful_result(code, message="", data=None):
    return jsonify({
        "code": code,
        "message": message,
        "data": data
    })


def success():
    return restful_result(HttpCode.ok)


def unauth_error(message=""):
    return restful_result(HttpCode.un_auth_error, message=message, data={})


def params_error(message="", data=None):
    return restful_result(HttpCode.un_auth_error, message=message, data=data)


def server_error(message="服务起内部错误", data=None):
    return restful_result(HttpCode.un_auth_error, message=message, data=data)
