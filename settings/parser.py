import os
import platform
import sys
from configparser import ConfigParser

LINUX = 'Linux'
MAC = 'Darwin'


class Parser(object):
    target_files = []
    settings_file = '.pmenu.ini'

    def __init__(self):
        exe = sys.executable
        app_dir = os.path.dirname(exe)
        home_dir = os.path.expanduser('~')
        self.target_files.append(f'{home_dir}/{self.settings_file}')
        self.target_files.append(f'{home_dir}/.config/{self.settings_file}')
        self.target_files.append(f'{app_dir}/{self.settings_file}')
        self.target_files.append(self.settings_file)

    def get_settings_file(self):
        for target in self.target_files:
            if os.path.exists(target):
                return target
        return None

    def read_settings(self):
        settings = {}
        file = self.get_settings_file()
        if not file:
            return settings

        config = ConfigParser()
        config.read(file)
        for section in config.sections():
            for key in config[section]:
                settings[f'{section.upper()}_{key.upper()}'] = config[section][key]

        return settings


parser = Parser()
user_settings = parser.read_settings()
PARSED_SETTINGS_FILE = parser.get_settings_file()
