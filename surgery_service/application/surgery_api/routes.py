from . import surgery_api_blueprint
from .. import db
from ..models import Surgery
from flask import make_response, request, jsonify


@surgery_api_blueprint.route('/all', methods=['GET'])
def all_surgeries():
    items = []
    for row in Surgery.query.all():
        items.append(row.to_json())

    response = jsonify(items)
    return response


@surgery_api_blueprint.route('/create', methods=['POST'])
def post_create():
    name = request.form['name']
    code = request.form['code']
    severity = request.form['severity']

    surgery = Surgery()
    surgery.name = name
    surgery.code = code
    surgery.severity = severity

    db.session.add(surgery)
    db.session.commit()

    response = jsonify({'message': 'Surgery Added', 'result': surgery.to_json()})
    return response


@surgery_api_blueprint.route('/<code>/exists', methods=['GET'])
def surgery_exists(code):
    item = Surgery.query.filter_by(code=code).first()
    if item is not None:
        response = jsonify({'result': True, 'id': item.id})
    else:
        response = make_response(jsonify({'result': False, 'message': 'Cannot find surgery'}), 404)
    return response


# get surgery by ID
@surgery_api_blueprint.route('/get', methods=['GET'])
def get_surgery():
    item = Surgery.query.filter_by(id=request.form['id']).first()
    if item is not None:
        response = jsonify({'message': 'Found surgery', 'result': item.to_json()})
    else:
        response = make_response(jsonify({'message': 'Surgery does not exist'}), 404)
    return response


@surgery_api_blueprint.route('/update', methods=['POST'])
def update_surgery():
    item = Surgery.query.filter_by(code=request.form['code']).first()
    if item is not None:
        item.severity = request.form['severity']
        item.name = request.form['name']
        db.session.add(item)
        db.session.commit()
        response = jsonify({'message': 'Surgery updated', 'result': item.to_json()})
    else:
        response = make_response(jsonify({'message': 'No surgery to update'}))
    return response
