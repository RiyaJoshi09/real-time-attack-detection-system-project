import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    DEBUG = os.environ.get('DEBUG', 'True') == 'True'
    LOG_FILE_PATH = os.environ.get('LOG_FILE_PATH', 'logs/attack_logs.json')
    CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '*')
