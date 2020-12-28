from sys import maxsize

class Configurations_Project:
    def __init__(self, id=None,name=None, status=None, view=None, description=None):
        self.name = name
        self.status = status
        self.view = view
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s,%s" % (self.id, self.name, self.description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name \
               and self.description == other.description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
