
import os
from pathlib import Path


homedir = str(Path.home())
basedir = os.path.join(homedir, ".analysisweb")


class UserConfig(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'analysisweb.db')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or \
                    os.path.join(basedir, 'uploaded')
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    SYMPATHY_EXEC = os.path.join(basedir, os.path.pardir, 'sympathy', 'run_sympathy.bash')
    SERVER_URL = "http://127.0.0.1:5000/"