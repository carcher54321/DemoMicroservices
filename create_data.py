import uuid
import random
import datetime
import string


def apply_uuid(l):
    out = {}
    for j in l:
        out[j] = uuid.uuid4()
    return out


def create_hospital(hospital, hospital_id):
    h_out = '\t{\n\t\t'
    h_out += '"type": "hospital",\n\t\t'
    h_out += '"hospital": "' + hospital + '",\n\t\t'
    zip_code = random.choice(range(501, 99951))
    h_out += '"zip": ' + str(zip_code) + ',\n\t\t'
    h_out += '"code": "' + str(hospital_id) + '"\n\t}'
    return h_out


def create_surgery(surgery, surgery_id):
    s_out = '\t{\n\t\t'
    s_out += '"type": "surgery",\n\t\t'
    s_out += '"surgery": "' + surgery + '",\n\t\t'
    s_out += '"severity_level": ' + str(random.choice(range(1, 10))) + ',\n\t\t'
    s_out += '"code": "' + str(surgery_id) + '"\n\t}'
    return s_out


class Create_data:
    def __init__(self, hospitals_list, surgeries_list, first_names_list, last_names_list):
        self.hospitals_list = hospitals_list
        self.surgeries_list = surgeries_list
        self.first_names_list = first_names_list
        self.last_names_list = last_names_list

    def create_operation(self, hospital_id, surgery_id):
        o_out = '\t{\n\t\t'
        o_out += '"type": "operation",\n\t\t'
        o_out += '"hospital_code": "' + str(hospital_id) + '",\n\t\t'
        o_out += '"surgery_code": "' + str(surgery_id) + '",\n\t\t'
        o_out += '"price": ' + str(random.choice(range(500, 10000))) + ',\n\t\t'
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        year = random.randint(2000, 2021)
        rand_date = datetime.date(year, month, day)
        o_out += '"date": "' + str(rand_date) + '",\n\t\t'
        surgeon_name = random.choice(self.first_names_list) + ' ' + random.choice(self.last_names_list)
        o_out += '"surgeon_name": "' + surgeon_name.title() + '"\n\t}'
        return o_out

    def main(self):
        h_list = ''
        for h, h_id in self.hospitals_list.items():
            h_list += '\n' + create_hospital(h, h_id) + ','

        s_list = ''
        for s, s_id in self.surgeries_list.items():
            s_list += '\n' + create_surgery(s, s_id) + ','

        o_list = ''
        for h, h_id in self.hospitals_list.items():
            for s, s_id in self.surgeries_list.items():
                o_list += '\n' + self.create_operation(h_id, s_id) + ','

        return '[' + h_list + s_list + o_list + ']'


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

    cd = Create_data(hospitals, surgeries, first_names, last_names)
    out = cd.main()
    try:
        # tries to create file, throws error if it already exists
        json_file = open('data/medical_data.json', 'x', encoding='utf-8')
        json_file.write(out)
        json_file.close()
    except FileExistsError:
        json_file = open('data/medical_data.json', 'w', encoding='utf-8')
        json_file.write(out)
        json_file.close()
