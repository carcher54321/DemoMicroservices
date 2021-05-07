import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cloudacademy:pfm_2020@host.docker.internal:3306/surgery_dev'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    pass
