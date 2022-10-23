from flask import jsonify


def res_data_invalid(error):
    response = jsonify({"message": error})
    return response


def res_sucess(data):
    return jsonify({"message": "sucess", "data": data})
