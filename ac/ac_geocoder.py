import geocoder
import shapely
from amigocloud import AmigoCloud
from shapely import geos
import time
from ac.blds_dataset import BLDSDataset
from shapely.geometry import Point

"""
Geocoder class:
    - Queries the AmigoCloud BLDS dataset
    - Using Google geocoder it resolves the addresses from the field src_address_field_name='original_address1' into
     geometry, street address, city, state, zipcode
    - Updates BLDS dataset with resolved data

    Page size is 100 records.

    To setup GOOGLE API key for Google geocoder, set an environment variable:
    export GOOGLE_API_KEY='...'
"""
class Geocoder:

    dataset_url = '/users/{user_id}/projects/{project_id}/datasets/{dataset_id}'
    src_address_field_name = 'original_address1'
    page_size = 100

    def __init__(self, city_name, project_id, dataset_id, token):
        self.city_name = city_name
        self.dataset = BLDSDataset(project_id, dataset_id, token)

    def geocode(self):

        query = 'SELECT amigo_id,{address_field} FROM {table} WHERE wkb_geometry IS NULL'.format(
            table=self.dataset.table_name,
            address_field=self.src_address_field_name)

        shapely.geos.WKBWriter(geos.lgeos, include_srid=True)
        records = []
        offset = 0
        done = False;
        while not done:
            rows = self.dataset.query_page(query, self.page_size, offset)
            offset += len(rows)
            for row in rows:
                address = row[self.src_address_field_name]
                g = geocoder.google(address)
                if g.status is 'OK' and g.city and self.city_name in g.city:
                    wkt = 'SRID=4326;' + g.wkt
                    new_address = str(g.street_number) + ' ' + str(g.street)
                    if g.subpremise is not None:
                        new_address += ' ' + str(g.subpremise)
                    record = {
                        "original_address1": new_address,
                        "original_city": g.city,
                        "original_state": g.state,
                        "original_zip": g.postal,
                        "wkb_geometry":  wkt,
                        "amigo_id": row['amigo_id']
                    }
                    print(str(g.latlng) + ': ' + str(record))
                    records.append(record)
            self.dataset.update_records(records)
            records[:] = []
            if len(rows) == 0:
                done = True
            else:
                time.sleep(2)
