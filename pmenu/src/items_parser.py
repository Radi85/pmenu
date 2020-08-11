from os import environ, path as os_path
from platform import system as platform_system
from glob import glob
from subprocess import Popen

from settings import LINUX, MAC


class ItemsParser(object):
    APPS_DIRECTORY_MAPPER = {
        LINUX: [f'{path}/*' for path in environ.get('PATH').split(':')],
        MAC: [
            '/Applications/*.app',
            '/Applications/Utilities/*.app',
            '/System/Applications/*.app',
            '/System/Applications/Utilities/*.app'
        ]
    }
    ITEMS = {}

    def __init__(self, items=None):
        self.is_item_app = True
        if items:
            if not isinstance(items, list):
                items = [items]
            self.set_items(items)
            self.is_item_app = False
        else:
            self.set_apps()

    def get_search_directories(self):
        return self.APPS_DIRECTORY_MAPPER[platform_system()]

    def set_apps(self):
        for directory in self.get_search_directories():
            paths = glob(directory)
            for path in paths:
                if platform_system() == LINUX and not os_path.isfile(path):
                    continue
                app_name = os_path.basename(path)
                if platform_system() == MAC and '.app' in path:
                    app_name = app_name[:-4]
                self.ITEMS[app_name] = path

    def set_items(self, items):
        self.ITEMS = dict(zip(items, items))

    def filter_items(self, string):
        filtered_items = {
            item: path for item, path in self.ITEMS.items() if string.lower() in item.lower()
        }
        return filtered_items

    def output(self, item):
        if self.is_item_app:
            if platform_system() == MAC:
                app_path = self.ITEMS.get(item)
                if not app_path:
                    return
                Popen(f'open "{app_path}"', shell=True)
            else:
                Popen(item, shell=True)
        else:
            Popen(f'echo "{item}"', shell=True)
