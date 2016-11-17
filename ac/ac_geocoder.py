import geocoder
import shapely
from amigocloud import AmigoCloud
from shapely import geos
import time
from ac.blds_dataset import BLDSDataset
from shapely.geometry import Point

class Geocoder:

    dataset_url = '/users/{user_id}/projects/{project_id}/datasets/{dataset_id}'

    def __init__(self, city_name, project_id, dataset_id, token):
        self.city_name = city_name
        self.dataset = BLDSDataset(project_id, dataset_id, token)

    def geocode(self):

        query = 'SELECT amigo_id,{address_field} FROM {table} WHERE wkb_geometry IS NULL'.format(
            table=self.dataset.table_name,
            address_field='original_address1')

        shapely.geos.WKBWriter(geos.lgeos, include_srid=True)
        data = []
        offset = 0
        limit = 100
        done = False;
        while not done:
            rows = self.dataset.query_page(query, limit, offset)
            offset += len(rows)
            for row in rows:
                address = row['original_address1']# + u' ' + self.city_name + u', CA'
                g = geocoder.google(address)
                if g.status is 'OK':
                    print(str(g.latlng) + ': ' + address)
                    point = Point(g.lat, g.lng)
                    wkt = 'SRID=4326;' + g.wkt
                    r = {
                        "original_address1": str(g.street_number) + ' ' + str(g.street) + ' ' + str(g.subpremise),
                        "original_city": g.city,
                        "original_state": g.state,
                        "original_zip": g.postal,
                        "wkb_geometry":  wkt,
                        "amigo_id": row['amigo_id']
                    }
                    data.append(r)
            self.dataset.update_records(data)
            data[:] = []
            if len(rows) == 0:
                done = True
            else:
                time.sleep(2)
