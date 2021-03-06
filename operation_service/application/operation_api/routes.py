from . import operation_api_blueprint
from .. import db
from ..models import Operation
from flask import make_response, request, jsonify
from .api.SurgeryClient import SurgeryClient
from .api.HospitalClient import HospitalClient
surgery_client = SurgeryClient()
hospital_client = HospitalClient()


def create(surgery, hospital, price, date, surgeon):
    operation = Operation()
    operation.surgery = surgery
    operation.hospital = hospital
    operation.price = price
    operation.date = date
    operation.surgeon = surgeon

    db.session.add(operation)
    db.session.commit()
    return operation


def batch_create(lis):
    num = 0
    for obj in lis:
        operation = Operation()
        operation.surgery = obj['surgery']
        operation.hospital = obj['hospital']
        operation.price = obj['price']
        operation.date = obj['date']
        operation.surgeon = obj['surgeon']
        db.session.add(operation)
        num += 1
    db.session.commit()
    return 'Created Operation', num


def process_object(obj):
    try:
        tp = obj['type']
    except KeyError:
        return 'No type key', obj
    if tp == 'hospital':
        # get the data from the object
        try:
            code, name, zip_c = obj['code'], obj['name'], obj['zip']
        except KeyError:
            return 'Missing Key', obj
        # check if an object with a matching code exists, if so get its id
        exists, ident = hospital_client.exists(code)
        if exists:
            js = hospital_client.update(ident, name, zip_c, code)
        else:
            js = hospital_client.create(name, zip_c, code)
        return js['message'], js['result']
    elif tp == 'surgery':
        try:
            code, name, severity = obj['code'], obj['name'], obj['severity']
        except KeyError:
            return 'Missing Key', obj
        exists, ident = surgery_client.exists(code)
        if exists:
            js = surgery_client.update(ident, name, code, severity)
        else:
            js = surgery_client.create(name, code, severity)
        return js['message'], js['result']
    elif tp == 'operation':
        try:
            s_code, h_code, price, date, surgeon = obj['surgery'], obj['hospital'], obj['price'], \
                                                   obj['date'], obj['surgeon']
        except KeyError:
            return 'Missing Key', obj
        exists, s_id = surgery_client.exists(s_code)
        exists, h_id = hospital_client.exists(h_code)
        operation = create(s_id, h_id, price, date, surgeon)
        return 'Created operation', operation.to_json()
    else:
        return 'Error: Invalid object type', tp


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

    operation = create(surgery, hospital, price, date, surgeon)
    response = operation.to_json()
    return response


@operation_api_blueprint.route('/process', methods=['POST'])
def process():
    js = request.get_json()
    if type(js) is dict:
        msg, res = process_object(js)
        return jsonify({'message': msg, 'result': res})
    else:
        operations = [obj for obj in js if obj['type'] == 'operation']
        others = [obj for obj in js if obj['type'] != 'operation']
        rets = {}
        # batch create operations because there are many more of them
        msg, res = batch_create(operations)
        rets[msg] = res
        for obj in others:
            msg, res = process_object(obj)
            if msg in rets:
                rets[msg] += 1
            else:
                rets[msg] = 1
        return jsonify(rets)


@operation_api_blueprint.route('/get', methods=['GET'])
def get_operation():
    # get based on ID
    item = Operation.query.filter_by(id=request.form['id']).first()
    if item is not None:
        response = jsonify({'message': 'Found operation', 'result': item.to_json()})
    else:
        response = make_response(jsonify({'message': 'Could not find operation'}), 404)
    return response


@operation_api_blueprint.route('/batch-create', methods=['POST'])
def post_batch_create():
    lis = request.get_json()
    message, num = batch_create(lis)
    return jsonify({'message': f'Created {num} Operations'})
