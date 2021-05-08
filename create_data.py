import uuid
import random
import datetime
import string
import json


def apply_uuid(l):
    out = {}
    for j in l:
        out[j] = uuid.uuid4()
    return out


def create_hospital(hospital, hospital_id):
    d = {
        'type': 'hospital',
        'name': hospital,
        'zip': str(random.choice(range(501, 99951))),
        'code': str(hospital_id)
    }
    return d


def create_surgery(surgery, surgery_id):
    d = {
        'type': 'surgery',
        'name': surgery,
        'severity': str(random.choice(range(1, 10))),
        'code': str(surgery_id)
    }
    return d


class CreateData:
    def __init__(self, hospitals_list, surgeries_list, first_names_list, last_names_list):
        self.hospitals_list = hospitals_list
        self.surgeries_list = surgeries_list
        self.first_names_list = first_names_list
        self.last_names_list = last_names_list

    def create_operation(self, hospital_id, surgery_id):
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        year = random.randint(2000, 2021)
        rand_date = datetime.date(year, month, day)
        surgeon_name = random.choice(self.first_names_list) + ' ' + random.choice(self.last_names_list)
        d = {
            'type': 'operation',
            'hospital': str(hospital_id),
            'surgery': str(surgery_id),
            'price': str(random.choice(range(500, 10000))),
            'date': rand_date,
            'surgeon': surgeon_name.title()
        }
        return d

    def main(self):
        lis = []
        for h, h_id in self.hospitals_list.items():
            lis.append(create_hospital(h, h_id))

        for s, s_id in self.surgeries_list.items():
            lis.append(create_surgery(s, s_id))

        for h, h_id in self.hospitals_list.items():
            for s, s_id in self.surgeries_list.items():
                lis.append(self.create_operation(h_id, s_id))

        return lis


if __name__ == "__main__":
    with open('data/first_names.all.txt', encoding='utf-8') as f:
        first_names = f.read().split('\n')

    with open('data/last_names.all.txt', encoding='utf-8') as f:
        last_names = f.read().split('\n')

    with open('data/hospitals.txt', encoding='utf-8') as f:
        data = f.read()
        hospitals = []
        for i in data.split('\n'):
            hospitals.append(i)
    hospitals = apply_uuid(hospitals)

    with open('data/surgeries.txt', encoding='utf-8') as f:
        data = f.read()
        surgeries = []
        for i in data.split('\n'):
            surgeries.append(i)
    surgeries = apply_uuid(surgeries)

    cd = CreateData(hospitals, surgeries, first_names, last_names)
    out = cd.main()
    with open('data/medical_data.json', 'w', encoding='utf8') as file:
        json.dump(out, file)
