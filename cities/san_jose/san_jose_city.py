from cities.city import City

"""
SanJoseCity class defines a dictionary for field mapping
"""

class SanJoseCity(City):

    def __init__(self):
        self.fields = dict(
        [
            # San Jose City fields      BLDS fields
            ("permit_number",           "permit_num"),
            ("work_code_description",   "description"),
            ("work_code",               ""),
            ("apn",                     ""),
            ("year",                    ""),
            ("owner",                   ""),
            ("final_date",              "completed_date"),
            ("issue_date",              "issued_date"),
            ("approval_status",         "status_current"),
            ("sub_code",                ""),
            ("contractor",              "contractor_company_name"),
            ("permit_flag",             ""),
            ("location",                "original_address1"),
            ("lot",                     ""),
            ("units",                   "housing_units"),
            ("permit_valuation",        ""),
            ("type",                    "permit_type_desc"),
            ("rsn",                     "pin"),
            ("sub_code_description",    "permit_class"),
            ("square_feet",             "total_sqft"),
            ("tract",                   ""),
            ("pool",                    ""),
            ("reroof_valuation",        ""),
            ("applicant",               "contractor_full_name"),
            ("sewer",                   ""),
            ("enterprise",              ""),
            ("census_code",             "")
        ])
        self.city = City("SanJose", self.fields)
