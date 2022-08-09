

import os

print(os.environ)

CONFIG_PATH_ENV_VAR = "SUPERSET_CONFIG_PATH"
if CONFIG_PATH_ENV_VAR in os.environ:
    # Explicitly import config module that is not necessarily in pythonpath; useful
    # for case where app is being executed via pex.
    cfg_path = os.environ[CONFIG_PATH_ENV_VAR]
    print(cfg_path)
