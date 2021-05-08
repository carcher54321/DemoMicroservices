from . import hospital_api_blueprint
from .. import db
from ..models import Hospital
from flask import make_response, request, jsonify


@hospital_api_blueprint.route('/all', methods=['GET'])
def get_all():
    items = []
    for row in Hospital.query.all():
        items.append(row.to_json())
    return jsonify(items)


@hospital_api_blueprint.route('/create', methods=['POST'])
def post_create():
    name = request.form['name']
    zip_c = request.form['zip']
    code = request.form['code']

    hospital = Hospital()
    hospital.name = name
    hospital.zip = zip_c
    hospital.code = code

    db.session.add(hospital)
    db.session.commit()

    response = jsonify({'message': 'Hospital added', 'result': hospital.to_json()})
    return response


@hospital_api_blueprint.route('/<code>/exists', methods=['GET'])
def hospital_exists(code):
    item = Hospital.query.filter_by(code=code).first()
    if item is not None:
        response = jsonify({'result': True, 'id': item.id})
    else:
        response = make_response(jsonify({'result': False, 'message': 'No hospital with that code'}), 404)
    return response


@hospital_api_blueprint.route('/get', methods=['GET'])
def get_hospital():
    item = Hospital.query.filter_by(id=request.form['id']).first()
    if item is not None:
        response = jsonify({'result': item.to_json()})
    else:
        response = make_response(jsonify({'message': 'No hospital found'}), 404)
    return response


@hospital_api_blueprint.route('/update', methods=['POST'])
def update_hospital():
    item = Hospital.query.filter_by(id=request.form['id']).first()
    if item is not None:
        item.name = request.form['name']
        item.zip = request.form['zip']
        item.code = request.form['code']
        db.session.add(item)
        db.session.commit()
        response = jsonify({'message': 'Updated hospital', 'result': item.to_json()})
    else:
        response = make_response(jsonify({'message': 'No hospital to update'}), 404)
    return response


@hospital_api_blueprint.route('/batch-create', methods=['POST'])
def batch_create():
    items = request.get_json()
    num = 0
    for obj in items:
        hospital = Hospital()
        hospital.name = obj['name']
        hospital.zip = obj['zip']
        hospital.code = obj['code']
        db.session.add(hospital)
        num += 1
    db.session.commit()
    return jsonify({'message': f'Created {num} Hospitals'})
