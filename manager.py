from project import app
from flask_script import Manager
import os

app.config.from_object(os.environ['APP_SETTINGS'])
manager = Manager(app)

if __name__ == '__main__':
    manager.run()