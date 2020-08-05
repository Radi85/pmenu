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
        username = self.get_username()
        if platform.system() == MAC:
            self.target_files.append(f'/Users/{username}/{self.settings_file}')
            self.target_files.append(f'/Users/{username}/.config/{self.settings_file}')
            self.target_files.append(f'{app_dir}/{self.settings_file}')
            self.target_files.append(self.settings_file)

    @staticmethod
    def get_username():
        return os.environ.get('USER') or os.environ.get('USERNAME')

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


user_settings = Parser().read_settings()
