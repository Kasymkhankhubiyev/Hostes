
class User:
    def __init__(self, login=None, access=None, uid=None):
        self.uid = uid
        self.login = login
        self.access = access

    def get_uid(self):
        return self.uid

    def get_login(self):
        return self.login

    def get_access(self):
        return self.access