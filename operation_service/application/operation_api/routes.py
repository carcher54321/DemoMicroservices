from . import operation_api_blueprint
from .. import db
from ..models import Operation
from flask import make_response, request, jsonify


@operation_api_blueprint.route('/all', methods=['GET'])
def get_all():
    items = []
    for row in Operation.query.all():
        items.append(row.to_json())
    return jsonify(items)


@operation_api_blueprint.route('/create', methods=['POST'])
def post_create():
    surgery = request.form['surgery']
    hospital = request.form['hospital']
    price = request.form['price']
    date = request.form['date']
    surgeon = request.form['surgeon']

    operation = Operation()
    operation.surgery = surgery
    operation.hospital = hospital
    operation.price = price
    operation.date = date
    operation.surgeon = surgeon

    db.session.add(operation)
    db.session.commit()

    response = operation.to_json()
    return response


@operation_api_blueprint.route('/process', methods=['POST'])
def process():
    pass
