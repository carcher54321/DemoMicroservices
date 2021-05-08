import uuid
import random
import datetime
import json


def load_txt(filename):
    with open(filename, encoding='utf-8') as f:
        return f.read().split('\n')


def apply_uuid(l):
    out = {}
    for j in l:
        out[j] = uuid.uuid4()
    return out


def create_hospital(hospital, hospital_id):
    return {'type': 'hospital',
            'name': hospital,
            'zip': random.choice(range(501, 99951)),
            'code': str(hospital_id)}


def create_surgery(surgery, surgery_id):
    return {'type': 'surgery',
            'name': surgery,
            'severity': random.choice(range(1, 10)),
            'code': str(surgery_id)}


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
        return {'type': 'operation',
                'hospital': str(hospital_id),
                'surgery': str(surgery_id),
                'price': random.choice(range(500, 10000)),
                'date': rand_date.isoformat(),
                'surgeon': surgeon_name.title()}

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
    first_names = load_txt('data/first_names.all.txt')
    last_names = load_txt('data/last_names.all.txt')
    hospitals = apply_uuid(load_txt('data/hospitals.txt'))
    surgeries = apply_uuid(load_txt('data/surgeries.txt'))

    cd = CreateData(hospitals, surgeries, first_names, last_names)
    out = cd.main()

    try:
        # tries to create file, throws error if it already exists
        json_file = open('data/medical_data.json', 'x', encoding='utf-8')
        json.dump(out, json_file, indent=4)
        json_file.close()
    except FileExistsError:
        json_file = open('data/medical_data.json', 'w', encoding='utf-8')
        json.dump(out, json_file, indent=4)
        json_file.close()
