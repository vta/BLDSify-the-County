import os

from amigocloud.blds_dataset import BLDSDataset
from cities.san_jose_city import SanJoseCity
from tasks import convert_to_dict

def run_pipeline():
    pipeline = [
        convert_to_dict
    ]
    
    for task in pipeline:
        result = task.run()
        
    print(result)
        
run_pipeline()

