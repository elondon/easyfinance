class Model(object):
    def __init__(self, entity):
        self._entity = entity

    @property
    def entity(self):
        return self._entity

