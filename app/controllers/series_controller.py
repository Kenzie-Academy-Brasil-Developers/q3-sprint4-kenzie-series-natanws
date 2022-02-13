from http import HTTPStatus
from flask import jsonify
from app.models.series_model import Series

def create():
    try:
        data = Series.create_series()
    except:
        return {"message": "Série já está cadastrada."}, HTTPStatus.CONFLICT

    return jsonify({"data": data}), HTTPStatus.CREATED

def series():
    data = Series.get_all_series()

    return jsonify({"data": data}), HTTPStatus.OK

def select_by_id(serie_id):
    try:
        data = Series.get_series_by_id(serie_id)
    except:
        Series.create_table()
        return {"error": "Not Found"}, HTTPStatus.NOT_FOUND

    return jsonify({"data": data}), HTTPStatus.OK