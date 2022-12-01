from flask import jsonify


def res_data_invalid(error):
    response = jsonify({"message": error})
    return response


def res_sucess(resource, message, data=[]):
    return jsonify({"status": "sucess", "message": message, "data": data})
