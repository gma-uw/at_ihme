import sys
import os
if 1:
    if '/Users/gma/Projects/IHME/GIT/ihme_at.git' in sys.path:
        sys.path.remove('/Users/gma/Projects/IHME/GIT/ihme_at.git')
    sys.path = [os.path.abspath('./src')] + sys.path 

from cascade_at.executor.configure_inputs import main as main1
from cascade_at.executor.dismod_db import main as main2

mvid_info = [{'mvid': 475526, 'location_id': 1, 'sex_id': 3, 'json_file': '475526_settings-world.json'},
             {'mvid': 475527, 'location_id': 96, 'sex_id': 3, 'json_file': '475527_settings-SLatinAmerica.json'},
             {'mvid': 475533, 'location_id': 1, 'sex_id': 3, 'json_file': '475533_settings-world.json'},
             {'mvid': 475588, 'location_id': 1, 'sex_id': 3, 'json_file': '475588_settings-world-RE.json'},
             {'mvid': 475588, 'location_id': 102, 'sex_id': 3, 'json_file': '475588_settings-USA-RE.json'},
             {'mvid': 475588, 'location_id': 523, 'sex_id': 3, 'json_file': '475588_settings-Alabama.json'},
             {'mvid': 475718, 'location_id': 70, 'sex_id': 3, 'json_file': '475718_settings-Australasia.json'},
             {'mvid': 475746, 'location_id': 64, 'sex_id': 3, 'json_file': '475746_settings-HighIncome.json'},
             {'mvid': 475746, 'location_id': 1, 'sex_id': 3, 'json_file': '475746_settings-world.json'}]


if __name__ == '__main__':
    for _mvid_ in mvid_info:
        mvid, loc_id, sex_id, json_file = [_mvid_[k] for k in ['mvid', 'location_id', 'sex_id', 'json_file']]
        cmd1 = f'configure_inputs {mvid} --json-file /Users/gma/ihme/epi/at_cascade/data/{json_file} --test-dir /tmp'
        cmd2 = f'dismod_db --model-version-id {mvid} --parent-location-id {loc_id} --sex-id {sex_id} --fill --test-dir /tmp'
        print (cmd1)
        main1(cmd1.split())
        print (cmd2)
        main2(cmd2.split())
