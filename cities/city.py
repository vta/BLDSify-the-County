
class City:

    def __init__(self, name, fields):
        self.city_name = name
        self.fields = dict(fields)

    def field_match(self, field_name):
        return self.fields[field_name]