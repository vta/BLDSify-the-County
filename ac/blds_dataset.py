import json
import string
import time
import uuid

from amigocloud import AmigoCloud

class BLDSDataset:
    """ A class to manage AmigoCloud's BLDS dataset """

    dataset_url = '/users/{user_id}/projects/{project_id}/datasets/{dataset_id}'

    def __init__(self, project_id, dataset_id, token):
        self.ac = AmigoCloud(token=token)
        self.dataset = self.ac.get(self.dataset_url.format(user_id=1,
                                        project_id=project_id,
                                        dataset_id=dataset_id))
        self.table_name = self.dataset['table_name']
        self.response = self.ac.get(self.dataset['master'])
        self.master = self.response['master']

    def add_column(self, column_json):
        print("Add column: " + column_json["name"])
        add_column = {
            "type": "DDL",
            "entity": self.table_name,
            "action": "ADD COLUMN",
            "parent": self.master,
            "data": [
                {
                    "new": column_json
                }
            ]
        }
        response = self.ac.post(self.dataset['submit_change'],
                   {'change': json.dumps(add_column)})
        time.sleep(5) # to prevent Error: TOO MANY REQUESTS

    def create_schema(self):
        print("Create schema for " + self.table_name)
        columns = [
            # Required fields
            {
                "name": "permit_num",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "PermitNum",
                "type": "string"
            },
            {
                "name": "description",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "Description",
                "type": "string"
            },
            {
                "name": "applied_date",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "AppliedDate",
                "type": "string"
            },
            {
                "name": "issued_date",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "IssuedDate",
                "type": "string"
            },
            {
                "name": "completed_date",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "CompletedDate",
                "type": "string"
            },
            {
                "name": "status_current",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "StatusCurrent",
                "type": "string"
            },
            {
                "name": "original_address1",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "OriginalAddress1",
                "type": "string"
            },
            {
                "name": "original_address2",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "OriginalAddress2",
                "type": "string"
            },
            {
                "name": "original_city",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "OriginalCity",
                "type": "string"
            },
            {
                "name": "original_state",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "OriginalState",
                "type": "string"
            },
            {
                "name": "original_zip",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "OriginalZip",
                "type": "string"
            },
            # Recommended fields
            {
                "name": "jurisdiction",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "Jurisdiction",
                "type": "string"
            },
            {
                "name": "permit_class",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "PermitClass",
                "type": "string"
            },
            {
                "name": "permit_class_mapped",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "PermitClassMapped",
                "type": "string"
            },
            {
                "name": "status_current_mapped",
                "nullable": True,
                "default": None,
                "editable": True,
                "choices": [
                    {
                        "code": "Appeal",
                        "value": "Appeal"
                    },
                    {
                        "code": "Application Accepted",
                        "value": "Application Accepted"
                    },
                    {
                        "code": "Fees/Payment",
                        "value": "Fees/Payment"
                    },
                    {
                        "code": "In Review",
                        "value": "In Review"
                    },
                    {
                        "code": "Inspection Phase",
                        "value": "Inspection Phase"
                    },
                    {
                        "code": "Occupancy",
                        "value": "Occupancy"
                    },
                    {
                        "code": "Permit Cancelled",
                        "value": "Permit Cancelled"
                    },
                    {
                        "code": "Permit Finaled",
                        "value": "Permit Finaled"
                    },
                    {
                        "code": "Permit Finaled with Conditions",
                        "value": "Permit Finaled with Conditions"
                    },
                    {
                        "code": "Permit Issued",
                        "value": "Permit Issued"
                    }
                ],
                "visible": True,
                "alias": "StatusCurrentMapped",
                "type": "string"
            },
            {
                "name": "amigo_id",
                "nullable": False,
                "default": "GENERATE_UUID",
                "auto_populate": True,
                "max_length": 32,
                "type": "string"
            },
            {
                "name": "work_class",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "WorkClass",
                "type": "string"
            },
            {
                "name": "permit_type_mapped",
                "nullable": True,
                "default": None,
                "editable": True,
                "choices": [
                    {
                        "code": "Building",
                        "value": "Building"
                    },
                    {
                        "code": "Demolition",
                        "value": "Demolition"
                    },
                    {
                        "code": "Electrical",
                        "value": "Electrical"
                    },
                    {
                        "code": "Fence",
                        "value": "Fence"
                    },
                    {
                        "code": "Grading",
                        "value": "Grading"
                    },
                    {
                        "code": "Mechanical",
                        "value": "Mechanical"
                    },
                    {
                        "code": "Plumbing",
                        "value": "Plumbing"
                    },
                    {
                        "code": "Pool/Spa",
                        "value": "Pool/Spa"
                    },
                    {
                        "code": "Roof",
                        "value": "Roof"
                    }
                ],
                "visible": True,
                "alias": "PermitTypeMapped",
                "type": "string"
            },
            {
                "name": "permit_type",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "PermitType",
                "type": "string"
            },
            {
                "name": "work_class_mapped",
                "nullable": True,
                "default": None,
                "editable": True,
                "choices": [
                    {
                        "code": "Existing",
                        "value": "Existing"
                    },
                    {
                        "code": "New",
                        "value": "New"
                    }
                ],
                "visible": True,
                "alias": "WorkClassMapped",
                "type": "string"
            },
            {
                "name": "permit_type_desc",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "PermitTypeDesc",
                "type": "string"
            },
            {
                "name": "est_project_cost",
                "nullable": True,
                "default": None,
                "max_value": None,
                "min_value": None,
                "editable": True,
                "visible": True,
                "alias": "EstProjectCost",
                "type": "float"
            },
            {
                "name": "status_date",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "StatusDate",
                "type": "string"
            },
            {
                "name": "contractor_trade",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorTrade",
                "type": "string"
            },
            {
                "name": "latitude",
                "nullable": True,
                "default": None,
                "max_value": None,
                "min_value": None,
                "editable": True,
                "visible": True,
                "alias": "Latitude",
                "type": "float"
            },
            {
                "name": "longitude",
                "nullable": True,
                "default": None,
                "max_value": None,
                "min_value": None,
                "editable": True,
                "visible": True,
                "alias": "Longitude",
                "type": "float"
            },
            {
                "name": "pin",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "PIN",
                "type": "string"
            },
            {
                "name": "housing_units",
                "nullable": True,
                "default": None,
                "max_value": None,
                "min_value": None,
                "editable": True,
                "visible": True,
                "alias": "HousingUnits",
                "type": "integer"
            },
            {
                "name": "total_sqft",
                "nullable": True,
                "default": None,
                "max_value": None,
                "min_value": None,
                "editable": True,
                "visible": True,
                "alias": "TotalSqFt",
                "type": "float"
            },
            {
                "name": "contractor_state_lic",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorStateLic",
                "type": "string"
            },
            {
                "name": "link",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "Link",
                "type": "string"
            },
            {
                "name": "contractor_trade_mapped",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorTradeMapped",
                "type": "string"
            },
            {
                "name": "contractor_lic_num",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorLicNum",
                "type": "string"
            },
            {
                "name": "contractor_company_name",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorCompanyName",
                "type": "string"
            },
            # Optional fields
            {
                "name": "proposed_use",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ProposedUse",
                "type": "string"
            },
            {
                "name": "added_sqft",
                "nullable": True,
                "default": None,
                "max_value": None,
                "min_value": None,
                "editable": True,
                "visible": True,
                "alias": "AddedSqFt",
                "type": "float"
            },
            {
                "name": "removed_sqft",
                "nullable": True,
                "default": None,
                "max_value": None,
                "min_value": None,
                "editable": True,
                "visible": True,
                "alias": "RemovedSqFt",
                "type": "float"
            },
            {
                "name": "master_permit_num",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "MasterPermitNum",
                "type": "string"
            },
            {
                "name": "expires_date",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ExpiresDate",
                "type": "string"
            },
            {
                "name": "co_issued_date",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "COIssuedDate",
                "type": "string"
            },
            {
                "name": "hold_date",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "HoldDate",
                "type": "string"
            },
            {
                "name": "void_date",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "VoidDate",
                "type": "string"
            },
            {
                "name": "project_name",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ProjectName",
                "type": "string"
            },
            {
                "name": "project_id",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ProjectID",
                "type": "string"
            },
            {
                "name": "total_finished_sqft",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "TotalFinishedSqFt",
                "type": "string"
            },
            {
                "name": "total_unfinished_sqft",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "TotalUnfinishedSqFt",
                "type": "string"
            },
            {
                "name": "total_heated_sqft",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "TotalHeatedSqFt",
                "type": "string"
            },
            {
                "name": "total_unheated_sqft",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "TotalUnHeatedSqFt",
                "type": "string"
            },
            {
                "name": "total_acc_sqft",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "TotalAccSqFt",
                "type": "string"
            },
            {
                "name": "total_sprinkled_sqft",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "TotalSprinkledSqFt",
                "type": "string"
            },
            {
                "name": "extra_fields",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ExtraFields",
                "type": "string"
            },
            {
                "name": "publisher",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "Publisher",
                "type": "string"
            },
            {
                "name": "fee",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "Fee",
                "type": "float"
            },
            {
                "name": "contractor_full_name",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorFullName",
                "type": "string"
            },
            {
                "name": "contractor_company_desc",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorCompanyDesc",
                "type": "string"
            },
            {
                "name": "contractor_phone",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorPhone",
                "type": "string"
            },
            {
                "name": "contractor_address1",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorAddress1",
                "type": "string"
            },
            {
                "name": "contractor_address2",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorAddress2",
                "type": "string"
            },
            {
                "name": "contractor_city",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorCity",
                "type": "string"
            },
            {
                "name": "contractor_state",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorState",
                "type": "string"
            },
            {
                "name": "contractor_zip",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorZip",
                "type": "string"
            },
            {
                "name": "contractor_email",
                "visible": True,
                "default": None,
                "nullable": True,
                "editable": True,
                "alias": "ContractorEmail",
                "type": "string"
            },
        ]
        for column in columns:
            self.add_column(column)

    def upload_records(self, records, city):
        insert_records = {
            "type": "DML",
            "entity": self.table_name,
            "action": "INSERT",
            "data": records
        }
        # print insert_record
        response = self.ac.post(self.dataset['submit_change'],
                       {'change': json.dumps(insert_records)})
        print("Upload " + str(len(records)) + " records to " + self.table_name)
        time.sleep(10)

    def get_record_obj(self, record, city):
        obj = dict()
        for field_name, value in record.iteritems():
            blds_filed = city.get_field(field_name)
            blds_value = city.get_value(value)
            if blds_filed:
                obj[blds_filed] = blds_value
        u = uuid.uuid1()
        new_obj = {"new": obj}
        new_obj["amigo_id"] = u.hex
        return new_obj

    def upload_permits(self, permits, city):
        records = []
        index = 0
        for key, value in permits.iteritems():
            for p in value:
                records.append(self.get_record_obj(p, city))
                index += 1
                if index >= 1000:
                    self.upload_records(records, city)
                    records[:] = []
                    index = 0
        # Upload the rest of the records
        self.upload_records(records, city)
