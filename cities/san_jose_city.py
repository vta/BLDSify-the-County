import city

class SanJoseCity(City):

    def __init__(self):
        self.fields = \
        [
            # City field      BLDS field
            ("permit_number", "permit_num"),
            ("work_code_description", ""),
            ("work_code", ""),
            ("apn", ""),
            ("year", ""),
            ("owner", ""),
            ("final_date", ""),
            ("issue_date", ""),
            ("approval_status", ""),
            ("sub_code", ""),
            ("contractor", ""),
            ("permit_flag", ""),
            ("location", ""),
            ("lot", ""),
            ("units", ""),
            ("permit_valuation", ""),
            ("type", ""),
            ("rsn", ""),
            ("sub_code_description", ""),
            ("square_feet", ""),
            ("tract", ""),
            ("pool", ""),
            ("reroof_valuation", ""),
            ("applicant", ""),
            ("sewer", ""),
            ("enterprise", ""),
            ("census_code", "")
        ]
        city = City("SanJose", self.fields)
