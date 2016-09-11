class Model(object):

    def __init__(self):
        pass

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def entity(self):
        return self._entity

    @entity.setter
    def entity(self, value):
        self.entity = value

