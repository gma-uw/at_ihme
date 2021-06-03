import sys
import os
if 1:
    if '/Users/gma/Projects/IHME/GIT/ihme_at.git' in sys.path:
        sys.path.remove('/Users/gma/Projects/IHME/GIT/ihme_at.git')
    sys.path = [os.path.abspath('./src')] + sys.path 

from cascade_at.executor.configure_inputs import main as main1
from cascade_at.executor.dismod_db import main as main2

if __name__ == '__main__':
    # json_cmd = '--json-file /Users/gma/ihme/epi/at_cascade/data/475588_settings-world.json'
    json_cmd = '--json-file /Users/gma/ihme/epi/at_cascade/data/475588_settings-Alabama.json'
    cmd = f'configure_inputs 475588 {json_cmd} --test-dir /tmp'
    print (cmd)
    argv = cmd.split()
    main1(argv)
    
    # cmd = 'dismod_db --model-version-id 475588 --parent-location-id 1 --sex-id 3 --fill --test-dir /tmp'
    cmd = 'dismod_db --model-version-id 475588 --parent-location-id 523 --sex-id 3 --fill --test-dir /tmp'
    print (cmd)
    argv = cmd.split()
    main2(argv)
