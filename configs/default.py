import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET = "X+aFzMgQVV0nR8BiB#h}v6E8}XTOw(gzN`(Eu4}=S3Z:Cnal!O_UGj$/YqS8@re"
ENV = "development"
DEBUG = True
CSRF_ENABLED = False
BUNDLE_ERRORS = False
MONGODB_DB = os.getenv('MONGODB_DB')
MONGODB_HOST = os.getenv('MONGODB_HOST')
MONGODB_PORT = os.getenv('MONGODB_PORT')
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
