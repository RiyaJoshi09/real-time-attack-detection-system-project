import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '1234567899874563210')
    DEBUG = os.environ.get('DEBUG', 'True') == 'True'
    LOG_FILE_PATH = os.environ.get('LOG_FILE_PATH', 'logs/attack_logs.json')
    CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '*')
