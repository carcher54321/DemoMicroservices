from flask import session
import requests


class SurgeryClient:
    base_url = 'http://localhost:5002/api/surgery'

    def get(self, ident):
        # get by ID in form
        form = {'id': ident}
        url = self.base_url + '/get'
        response = requests.request('GET', url, data=form)
        return response.json()

    def get_all(self):
        url = self.base_url + '/all'
        response = requests.request('GET', url)
        return response.json()

    def exists(self, code):
        url = self.base_url + '/' + code + '/exists'
        response = requests.request('GET', url)
        js = response.json()
        exists = js['result']
        if exists:
            return True, js['id']
        else:
            return False, 0

    def create(self, name, code, severity):
        # post with name, code severity in form
        form = {
            'name': name,
            'code': code,
            'severity': severity
        }
        url = self.base_url + '/create'
        response = requests.request('POST', url, data=form)
        return response.json()

    def update(self, ident, name, code, severity):
        # post w/name, code, severity in form
        form = {
            'id': ident,
            'name': name,
            'code': code,
            'severity': severity
        }
        url = self.base_url + '/update'
        response = requests.request('POST', url, data=form)
        return response.json()
