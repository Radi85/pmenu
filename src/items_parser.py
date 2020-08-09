import os
import platform
import glob
import subprocess

import settings


class ItemsParser(object):
    APPS_DIRECTORY_MAPPER = {
        settings.LINUX: [],  # TODO
        settings.MAC: [
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
        elif platform.system() == settings.MAC:
            self.set_mac_apps()

    def get_search_directories(self):
        return self.APPS_DIRECTORY_MAPPER[platform.system()]

    def set_mac_apps(self):
        for directory in self.get_search_directories():
            paths = glob.glob(directory)
            for path in paths:
                if '.app' in path:
                    self.ITEMS[os.path.basename(path)[:-4]] = path

    def set_items(self, items):
        self.ITEMS = dict(zip(items, items))

    def filter_items(self, string):
        filtered_items = {
            item: path for item, path in self.ITEMS.items() if string.lower() in item.lower()
        }
        return filtered_items

    def output(self, item):
        if self.is_item_app:
            program_path = self.ITEMS.get(item)
            if not program_path:
                return
            subprocess.Popen(f'open "{program_path}"', shell=True)
        else:
            subprocess.Popen(f'echo "{item}"', shell=True)
