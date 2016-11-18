"""
City class is a base class for the cities.
Particular city implementation need to define self.fields dictionary that maps the field names
from a city dataset to BLDS standard

 - get_value() function can be used for complicated field aggregations
"""
class City:

    def __init__(self, name, fields):
        self.city_name = name
        self.fields = dict(fields)

    def get_field(self, field_name):
        if field_name in self.fields:
            return self.fields[field_name]
        else:
            return None

    def get_value(self, field_name, value, record):
        return value
