class Person:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def __str__(self):
        return "{}:{}".format(self._name, self._email)

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email
