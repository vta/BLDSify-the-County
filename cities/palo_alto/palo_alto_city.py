from cities.city import City


class PaloAltoCity(City):

    def __init__(self):
        self.fields = dict(
        [
            # Palo Alto City fields      BLDS fields
            ("Record ID",               "permit_num"),
            ("Description",             "description"),
            ("Job Value",               "fee"),
            ("APN",                     ""),
            ("ID",                      "pin"),
            ("Date Opened",             "completed_date"),
            ("Record Status Date",      "issued_date"),
            ("Last Updated",            "status_date"),
            ("Record Status",           "status_current"),
            ("Licence NBR",             ""),
            ("Business Name",           "contractor_company_name"),
            ("Address Full Line",       "original_address1"),
            ("Record Type",             "permit_type"),
            ("Record Module",           ""),
            ("Latitude",                "latitude"),
            ("Longitude",               "longitude")
        ])
        self.city = City("PaloAlto", self.fields)
