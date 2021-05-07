from flask import session
import requests


class HospitalClient:
    base_url = 'http://chospital-service:5001/api/hospital'

    def get_all(self):
        url = self.base_url + '/all'
        response = requests.request('GET', url)
        return response.json()

    def create(self, name, zip_c, code):
        # post with name, zip_c, and code in form
        form = {
            'name': name,
            'zip': zip_c,
            'code': code
        }
        url = self.base_url + '/create'
        response = requests.request('POST', url, data=form)
        return response.json()

    def exists(self, code):
        url = self.base_url + code + '/exists'
        response = requests.request('GET', url)
        js = response.json()
        exists = js['result']
        if exists:
            return True, js['id']
        else:
            return False, 0

    def get(self, ident):
        # get by ID in form
        form = {'id': ident}
        url = self.base_url + '/get'
        response = requests.request('GET', url, data=form)
        return response.json()

    def update(self, name, zip_c, code):
        # post w/name, zip_c, and code in form
        form = {
            'name': name,
            'zip': zip_c,
            'code': code
        }
        url = self.base_url + '/update'
        response = requests.request('POST', url, data=form)
        return response
