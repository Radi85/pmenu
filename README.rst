PMenu
######

A small search app written in Python. It somehow simulates dmenu.

Any list of items can be passed as argument and the app will graphically represent them and return the selected item.

By default if there is no list of items passed, the available apps on the system will be retrieved and selected app will be executed.

::

    $ pmenu -h
    usage: pmenu [-h] [-H APP_HEIGHT] [-i LIST_ITEM_HEIGHT] [-n LIST_MAX_ITEMS]
                 [-w INPUT_WIDTH] [-l] [-f | -s]
                 [items [items ...]]

    pmenu

    positional arguments:
      items

    optional arguments:
      -h, --help            show this help message and exit
      -H APP_HEIGHT, --app_height APP_HEIGHT
                            Total height of the application
      -i LIST_ITEM_HEIGHT, --list_item_height LIST_ITEM_HEIGHT
                            Item height
      -n LIST_MAX_ITEMS, --list_max_items LIST_MAX_ITEMS
                            Total number of items to be viewed in the list
      -w INPUT_WIDTH, --input_width INPUT_WIDTH
                            Width of search field
      -l, --list            Show vertically as list
      -f, --font            Show system fonts
      -s, --settings        Show parsed settings file






