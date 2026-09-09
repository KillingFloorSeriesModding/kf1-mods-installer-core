import os
import sys
import pathlib

from platformdirs import user_config_dir, user_cache_dir

from kf1_mods_installer_core import  constants


if getattr(sys, 'frozen', False):
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir  = os.path.dirname(os.path.abspath(__file__))


config_dir = user_config_dir(appname=constants.APP_TITLE, appauthor=constants.APP_AUTHOR, ensure_exists=True)

cache_dir = pathlib.Path(user_cache_dir(appname=constants.APP_TITLE, appauthor=constants.APP_AUTHOR, ensure_exists=True))

SETTINGS_FILE = os.path.join(config_dir, "settings.toml")
