from settings.parser import user_settings


# APP settings
APP_HEIGHT = user_settings.get('APP_HEIGHT', 22)
try:
    APP_HEIGHT = int(APP_HEIGHT)
except ValueError:
    APP_HEIGHT = 22
APP_BACKGROUND = user_settings.get('APP_BACKGROUND', 'rgb(17, 17, 17)')
APP_TRANSPARENT = user_settings.get('APP_TRANSPARENT', 'TRUE').upper() == 'TRUE'


# input settings
INPUT_WIDTH = user_settings.get('INPUT_WIDTH', 400)
try:
    INPUT_WIDTH = int(INPUT_WIDTH)
except ValueError:
    INPUT_WIDTH = 400

INPUT_BACKGROUND = user_settings.get('INPUT_BACKGROUND', 'rgb(17, 17, 17)')
INPUT_TEXT_COLOR = user_settings.get('INPUT_COLOR', 'rgb(188, 188, 188)')


# list widget settings
LIST_BACKGROUND = user_settings.get('LIST_BACKGROUND', 'rgb(17, 17, 17)')
LIST_TEXT_COLOR = user_settings.get('LIST_COLOR', 'rgb(188, 188, 188)')
LIST_MAX_ITEMS = user_settings.get('LIST_MAX_ITEMS', 10)
try:
    LIST_MAX_ITEMS = int(LIST_MAX_ITEMS)
except ValueError:
    LIST_MAX_ITEMS = 5

LIST_ITEM_HEIGHT = user_settings.get('LIST_ITEM_HEIGHT', 22)
try:
    LIST_ITEM_HEIGHT = int(LIST_ITEM_HEIGHT)
except ValueError:
    LIST_ITEM_HEIGHT = 22

LIST_VERTICAL = user_settings.get('LIST_VERTICAL', 'FALSE').upper() == 'TRUE'


# active item settings
ACTIVE_BACKGROUND = user_settings.get('ACTIVE_BACKGROUND', 'rgb(17, 76, 110)')
ACTIVE_TEXT_COLOR = user_settings.get('ACTIVE_COLOR', 'rgb(188, 188, 188)')


# font settings
FONT_FAMILY = user_settings.get('FONT_FAMILY', 'SF Mono')
FONT_SIZE = user_settings.get('FONT_SIZE', 13)
try:
    FONT_SIZE = int(FONT_SIZE)
except ValueError:
    FONT_SIZE = 12

FONT_BOLD = user_settings.get('FONT_BOLD', 'FALSE').upper() == 'TRUE'
FONT_ITALIC = user_settings.get('FONT_ITALIC', 'FALSE').upper() == 'TRUE'
