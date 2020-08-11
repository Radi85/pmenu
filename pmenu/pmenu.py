from argparse import ArgumentParser
from sys import stdin

from src.app import PMenu


if __name__ == '__main__':
    """
    shell_program | pmenu
    shell_program | xargs pmenu
    """
    parser = ArgumentParser(description='pmenu')
    parser.add_argument('-H', '--app_height', type=int, help='Total height of the application')
    parser.add_argument('-i', '--list_item_height', type=int, help='Item height')
    parser.add_argument('-n', '--list_max_items', type=int, help='Total number of items to be viewed in the list')
    parser.add_argument('-w', '--input_width', type=int, help='Width of search field')
    parser.add_argument('-l', '--list', action='store_true', help='Display the list vertically')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-sf', '--show_fonts', action='store_true', help='Show system fonts')
    group.add_argument('-ss', '--show_settings', action='store_true', help='Show parsed settings file')
    parser.add_argument('items', nargs='*')

    args = parser.parse_args()

    system_option = args.show_fonts or args.show_settings

    if not stdin.isatty() and not args.items and not system_option:
        input_stream = stdin.read()
        args.items = input_stream.splitlines()

    PMenu(
        app_height=args.app_height,
        input_width=args.input_width,
        vertical=args.list,
        list_max_items=args.list_max_items,
        list_item_height=args.list_item_height,
        stdin_items=args.items,
        show_system_fonts=args.show_fonts,
        show_parsed_settings=args.show_settings
    )
