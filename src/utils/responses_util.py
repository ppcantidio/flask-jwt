from flask import jsonify


def res_data_invalid(error):
    response = jsonify({"message": error})
    return response
