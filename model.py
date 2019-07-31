from flask_login import UserMixin

class User(UserMixin):
    def __init__(self,  id, active=True):
        self.id = id
        self.active = active

    def get_id(self):
        return self.id

    @property
    def is_active(self):
        return self.active
