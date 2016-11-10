
class City:

    def __init__(self, name, fields):
        self.city_name = name
        self.fields = dict(fields)

    def get_field(self, field_name):
        return self.fields[field_name]

    def get_value(self, value):
        return value
