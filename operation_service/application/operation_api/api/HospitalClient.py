from flask import session
import requests


class HospitalClient:
    base_url = 'http://chospital-service:5001'
