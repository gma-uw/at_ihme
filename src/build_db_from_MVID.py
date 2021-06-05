import sys
import os
if 1:
    if '/Users/gma/Projects/IHME/GIT/ihme_at.git' in sys.path:
        sys.path.remove('/Users/gma/Projects/IHME/GIT/ihme_at.git')
    sys.path = [os.path.abspath('./src')] + sys.path 

from cascade_at.dismod.api.dismod_io import DismodIO

from cascade_at.executor.configure_inputs import main as main1
from cascade_at.executor.dismod_db import main as main2

from cascade_at.executor.dismod_db import dismod_db
from cascade_at.executor.dismod_db import ARG_LIST as ARG_LIST2


mvid_info = [
    # {'mvid': 475526, 'location_id': 1, 'sex_id': 3, 'json_file': '475526_settings-world.json'},
    # {'mvid': 475527, 'location_id': 96, 'sex_id': 3, 'json_file': '475527_settings-SLatinAmerica.json'},
    # {'mvid': 475533, 'location_id': 1, 'sex_id': 3, 'json_file': '475533_settings-world.json'},
    # {'mvid': 475718, 'location_id': 70, 'sex_id': 3, 'json_file': '475718_settings-Australasia.json'},
    # {'mvid': 475746, 'location_id': 64, 'sex_id': 3, 'json_file': '475746_settings-HighIncome.json'},
    # {'mvid': 475746, 'location_id': 1, 'sex_id': 3, 'json_file': '475746_settings-world.json'}
    # {'mvid': 475588, 'location_id': 1, 'sex_id': 3, 'json_file': '475588_settings-world-RE.json'},
    # {'mvid': 475588, 'location_id': 102, 'sex_id': 3, 'json_file': '475588_settings-USA-RE.json'},
    {'mvid': 475588, 'location_id': 523, 'sex_id': 3, 'json_file': '475588_settings-Alabama.json'},
]

if __name__ == '__main__':
    for _mvid_ in mvid_info:
        mvid, loc_id, sex_id, json_file = [_mvid_[k] for k in ['mvid', 'location_id', 'sex_id', 'json_file']]
        cmd1 = f'configure_inputs {mvid} --configure --json-file /Users/gma/ihme/epi/at_cascade/data/{json_file}' # --test-dir /Users/gma/ihme/'
        cmd2 = f'dismod_db --model-version-id {mvid} --parent-location-id {loc_id} --sex-id {sex_id} --fill' # --test-dir /Users/gma/ihme/'

        if 0:
            print (cmd1)
            main1(cmd1.split())

        if 0:
            print (cmd2)
            main2(cmd2.split())

        if 0:
            import dill
            with open(f'/Users/gma/ihme/epi/at_cascade/data/{mvid}/inputs/inputs.p', 'rb') as stream:
                p = dill.load(stream)
        args = ARG_LIST2.parse_args(cmd2.split()[1:])

        path = dismod_db(
            model_version_id=args.model_version_id,
            parent_location_id=args.parent_location_id,
            sex_id=args.sex_id,
            dm_commands=args.dm_commands,
            dm_options=args.dm_options,
            fill=args.fill,
            prior_samples=args.prior_samples,
            prior_parent=args.prior_parent,
            prior_sex=args.prior_sex,
            prior_mulcov_model_version_id=args.prior_mulcov,
            test_dir=args.test_dir,
            save_fit=args.save_fit,
            save_prior=args.save_prior,
        )
        db = DismodIO(path)
