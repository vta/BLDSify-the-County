from ac.ac_geocoder import Geocoder
from ac.blds_dataset import BLDSDataset

from cities.palo_alto.palo_alto_city import PaloAltoCity

from cities.palo_alto.convert_to_dict import get_palo_alto_permits
from cities.san_jose.convert_to_dict import get_san_jose_permits
from cities.san_jose.san_jose_city import SanJoseCity
import sys, getopt

def main(argv):
    city_name=''
    project_id = ''
    dataset_id = ''
    api_token = ''
    do_geocode = False
    try:
        opts, args = getopt.getopt(argv,"hgc:p:d:t:",["city=","projectid=","datasetid=","token"])
    except getopt.GetoptError:
        print('run.py -c <city> -p <project_id> -d <dataset_id> -t <API Token>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('run.py -c <city> -p <project_id> -d <dataset_id> -t <API Token>')
            sys.exit()
        elif opt in ("-g"):
            do_geocode = True
        elif opt in ("-c", "--city"):
            city_name = arg
        elif opt in ("-p", "--projectid"):
            project_id = arg
        elif opt in ("-d", "--datasetid"):
            dataset_id = arg
        elif opt in ("-t", "--token"):
            api_token = arg

    if do_geocode and city_name and project_id and dataset_id and api_token:
        g = Geocoder(city_name, project_id, dataset_id, api_token)
        g.geocode()
    elif city_name == "San Jose" and project_id and dataset_id and api_token:
        print("Process " + city_name)
        permits = get_san_jose_permits()
        dataset = BLDSDataset(project_id, dataset_id, api_token)
        dataset.create_schema()
        sj = SanJoseCity()
        dataset.upload_permits(permits, sj)
    elif city_name == "Palo Alto" and project_id and dataset_id and api_token:
        print("Process " + city_name)
        permits = get_palo_alto_permits()
        dataset = BLDSDataset(project_id, dataset_id, api_token)
        dataset.create_schema()
        pa = PaloAltoCity()
        dataset.upload_permits(permits, pa)
    else:
        print('Project id: ' + project_id)
        print('Dataset id: ' + dataset_id)
        print("City: " + city_name)
        if not api_token:
            print("API Token is missing")

if __name__ == "__main__":
   main(sys.argv[1:])


