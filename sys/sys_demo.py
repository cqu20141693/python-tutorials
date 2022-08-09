import imp
import logging
import os
import sys

from c_os.os_demo import CONFIG_PATH_ENV_VAR

logger = logging.getLogger(__name__)

if CONFIG_PATH_ENV_VAR in os.environ:

    cfg_path = os.environ[CONFIG_PATH_ENV_VAR]
    try:
        print(sys.modules)
        module = sys.modules[__name__]
        print(module)
        override_conf = imp.load_source("superset_config", cfg_path)
        for key in dir(override_conf):
            if key.isupper():
                setattr(module, key, getattr(override_conf, key))

        print(f"Loaded your LOCAL configuration at [{cfg_path}]")
        print(module)
    except Exception:
        logger.exception(
            "Failed to import config for %s=%s", CONFIG_PATH_ENV_VAR, cfg_path
        )
        raise
