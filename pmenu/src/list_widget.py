from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QListWidgetItem, QListWidget

import settings
from src.styles import Styles


class Font(QFont):
    def __init__(self):
        super().__init__()
        family = settings.FONT_FAMILY
        if family not in QFontDatabase().families():
            family = self.defaultFamily()
        self.setFamily(family)
        self.setPixelSize(settings.FONT_SIZE)
        self.setBold(settings.FONT_BOLD)
        self.setItalic(settings.FONT_ITALIC)


class ListWidget(QListWidget):
    def __init__(self, **kwargs):
        super().__init__()
        self.font = Font()
        self.setStyleSheet(Styles.list_widget)
        self.item_spacing = 2
        self.setSpacing(self.item_spacing)
        self.verticalScrollBar().setDisabled(True)
        self.horizontalScrollBar().setDisabled(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.width = kwargs.get('width')
        self.height = kwargs.get('height')
        self.show_max_items = kwargs.get('show_max_items')
        self.item_height = kwargs.get('item_height')
        self.show_vertical = False
        self.item_size = QSize(self.width, self.item_height)

    def set_vertical_widget(self):
        self.setFixedWidth(self.width)
        self.setFixedHeight(0)
        self.show_vertical = True

    def set_horizontal_widget(self):
        self.setFlow(QListWidget.LeftToRight)
        self.setFixedHeight(self.height)
        self.show_vertical = False

    def update_items(self, items):
        self.clear()
        for item_str in items:
            item = QListWidgetItem(item_str)
            item.setFont(self.font)
            if self.show_vertical:
                item.setSizeHint(self.item_size)
            self.addItem(item)
        self.setCurrentRow(0)
        if self.show_vertical:
            self.update_vertical_widget_height()

    def update_vertical_widget_height(self):
        count = self.count()
        self.height = self.show_max_items * (self.item_height + 2 * self.item_spacing)
        if count < self.show_max_items:
            self.height = count * (self.item_height + 2 * self.item_spacing)
        self.setFixedHeight(self.height + self.item_spacing)
