import settings


class Styles(object):
    app = f'background-color:{settings.APP_BACKGROUND};'
    list_widget = f'''
        QListWidget::item:selected {{
            background: {settings.ACTIVE_BACKGROUND}; color: {settings.ACTIVE_TEXT_COLOR};
        }}
        QListWidget::item {{
            border: none; background: {settings.LIST_BACKGROUND}; color: {settings.LIST_TEXT_COLOR};
        }}'''
    line_edit = f'color: {settings.INPUT_TEXT_COLOR}; background: {settings.INPUT_BACKGROUND}'
