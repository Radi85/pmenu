import sys

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout

import settings
from src.items_parser import ItemsParser
from src.list_widget import ListWidget
from src.styles import Styles


class PMenu(QWidget):
    def __init__(self, **kwargs):
        self.app = QApplication(sys.argv)
        self.window_height = kwargs.get('app_height') or settings.HEIGHT
        self.input_width = kwargs.get('input_width') or settings.INPUT_WIDTH
        self.show_vertical = kwargs.get('vertical', False)
        self.list_max_items = kwargs.get('list_max_items') or settings.LIST_MAX_ITEMS
        self.list_item_height = kwargs.get('list_item_height') or settings.LIST_ITEM_HEIGHT
        self.stdin_items = kwargs.get('stdin_items')
        self.line_edit = None
        self.list_widget = None
        self.cursor_position = 0
        super().__init__(flags=Qt.WindowFlags(Qt.Window | Qt.FramelessWindowHint))
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.app.installEventFilter(self)
        self.item_parser = ItemsParser(items=self.stdin_items)
        self.items = {}
        self.search_result = []
        self.full_width = self.app.desktop().screen().width()
        self.setGeometry(0, 0, self.full_width, self.window_height)
        self.setStyleSheet(Styles.app)
        self.layout = QVBoxLayout(self) if self.show_vertical else QHBoxLayout(self)
        self.setup()
        self.show()
        sys.exit(self.app.exec_())

    def setup(self):
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.line_edit = self.create_line_edit()
        self.layout.addWidget(self.line_edit, 0, Qt.AlignLeft)
        self.list_widget = ListWidget(
            width=self.input_width,
            height=self.window_height,
            show_max_items=self.list_max_items,
            item_height=self.list_item_height
        )
        if self.show_vertical:
            self.list_widget.set_vertical_widget()
        else:
            self.list_widget.set_horizontal_widget()
        self.list_widget.update_items([item for item in self.item_parser.ITEMS.keys()])
        self.layout.addWidget(self.list_widget)
        self.layout.setSpacing(0)
        self.line_edit.textChanged.connect(self.search)
        self.list_widget.itemClicked.connect(self.output_select_item)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonRelease:
            self.line_edit.setFocus()
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return and self.list_widget.currentItem():
                self.output_select_item(self.list_widget.currentItem())
                return True
            elif (event.key() == Qt.Key_Right or event.key() == Qt.Key_Down) and obj is self.line_edit:
                self.navigate_right_down()
            elif (event.key() == Qt.Key_Left or event.key() == Qt.Key_Up) and obj is self.line_edit:
                self.navigate_left_up()
            elif event.key() == Qt.Key_Escape:
                self.app.quit()
            self.line_edit.setCursorPosition(self.cursor_position)
        return super().eventFilter(obj, event)

    def search(self, value):
        self.cursor_position = len(value)
        self.items = self.item_parser.filter_items(value)
        if not value:
            self.items = {}
        self.list_widget.update_items([item for item in self.items.keys()])
        if self.show_vertical:
            self.setFixedHeight(self.list_widget.height + self.window_height)

    def output_select_item(self, item):
        self.item_parser.output(item.text())
        self.app.quit()

    def navigate_right_down(self):
        current_row = self.list_widget.currentRow()
        if current_row == self.list_widget.count() - 1:
            return
        self.list_widget.setCurrentRow(current_row + 1)

    def navigate_left_up(self):
        current_row = self.list_widget.currentRow()
        if current_row == 0:
            return
        self.list_widget.setCurrentRow(current_row - 1)

    def create_line_edit(self):
        line_edit = QLineEdit()
        line_edit.setCursorMoveStyle(Qt.VisualMoveStyle)
        line_edit.setStyleSheet(Styles.line_edit)
        line_edit.setFrame(False)
        line_edit.setAttribute(Qt.WA_MacShowFocusRect, 0)
        line_edit.setFixedWidth(self.input_width)
        line_edit.setFixedHeight(self.window_height)
        return line_edit


if __name__ == '__main__':
    PMenu()
