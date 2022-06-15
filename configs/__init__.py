import os
import inspect
from importlib import import_module


def get_config(config_name=None):
    """
    This method load multiple configurations if required. Pass configuration names
    separated by space or comma

        get_config('development') --> loads configuration from development.py file
        get_config('development production') -->
            loads configuration from development.json file and override these
            configurations from production.py file

    NOTE:
    Configuration json files are in gitignore to avoid configuration data in VCR.
    Use .example files to share the format or example of configuration files.
    """
    if not config_name:
        config_name = os.getenv('FLASK_CONFIG_MODULE', 'development')
    import_module(f'configs.{config_name.lower()}')
    envs = globals().get(config_name.lower(), None)
    configs = {}
    if envs:
        for key, value in envs.__dict__.items():
            if key.startswith('__') or key.startswith('_') or inspect.ismodule(value) or inspect.isfunction(value):
                continue
            if not value:
                continue
            os.environ.setdefault(key, value if not isinstance(value, bool) else str(value))
            if 'MONGODB_' in key:
                continue
            configs.update({key: value})

    configs.update({
        'MONGODB_SETTINGS': {
            'db': os.getenv('MONGODB_DB'),
            'host': os.getenv('MONGODB_HOST'),
            'port': int(os.getenv('MONGODB_PORT')),
            'username': os.getenv('MONGODB_USERNAME'),
            'password': os.getenv('MONGODB_PASSWORD'),
            "authentication_source": 'admin',
        }
    })

    return configs
