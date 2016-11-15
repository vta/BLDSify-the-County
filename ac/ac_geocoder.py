import geocoder
from amigocloud import AmigoCloud

class Geocoder:

    dataset_url = '/users/{user_id}/projects/{project_id}/datasets/{dataset_id}'

    def __init__(self, city_name, project_id, dataset_id, token):
        self.city_name = city_name
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.ac = AmigoCloud(token=token)
        self.dataset = self.ac.get(self.dataset_url.format(user_id=1,
                                        project_id=project_id,
                                        dataset_id=dataset_id))
        self.table_name = self.dataset['table_name']
        self.response = self.ac.get(self.dataset['master'])
        self.master = self.response['master']

    def query_page(self, limit, offset):

        sql_url = '/users/{user_id}/projects/{project_id}/sql'.format(
            user_id=1, project_id=self.project_id
        )

        address_field = 'original_address1'
        query = 'SELECT amigo_id,{address_field} FROM {table} WHERE wkb_geometry IS NULL'.format(table=self.table_name, address_field=address_field)
        # total_rows = dataset['feature_count']
        rows = []

        # while len(rows) < total_rows:
        response = self.ac.get(sql_url, {'query': query, 'offset': offset,
                                    'limit': limit, 'state': self.master,
                                    'dataset_id': self.dataset_id})

        if not offset:  # i.e. If first request
            print('The schema of the result is:')
            print(response['columns'])

        fetched_rows = len(response['data'])
        offset += fetched_rows
        rows += response['data']
        return rows


    def geocode(self):
        offset = 0
        limit = 5
        done = False;
        while not done:
            rows = self.query_page(limit, offset)
            offset += len(rows)
            for row in rows:
                address = row['original_address1'] + u' ' + self.city_name + u', CA'
                g = geocoder.google(address)
                print(str(g.latlng) + ': ' + address)
            done = True
