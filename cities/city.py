
class City:

    def __init__(self, name, fields):
        self.city_name = name
        self.fields = dict(fields)

    def get_field(self, field_name):
        if field_name in self.fields:
            return self.fields[field_name]
        else:
            return None

    def get_value(self, value):
        return value
