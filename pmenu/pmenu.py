import argparse
import sys

from src.app import PMenu


if __name__ == '__main__':
    """
    shell_program | pmenu
    shell_program | xargs pmenu
    """
    parser = argparse.ArgumentParser(description='pmenu')
    parser.add_argument('-H', '--app_height', type=int, help='Total height of the application')
    parser.add_argument('-i', '--list_item_height', type=int, help='Item height')
    parser.add_argument('-n', '--list_max_items', type=int, help='Total number of items to be viewed in the list')
    parser.add_argument('-w', '--input_width', type=int, help='Width of search field')
    parser.add_argument('-l', '--list', action='store_true', help='Show vertically as list')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--font', action='store_true', help='Show system fonts')
    group.add_argument('-s', '--settings', action='store_true', help='Show parsed settings file')
    parser.add_argument('items', nargs='*')

    args = parser.parse_args()

    system_option = args.font or args.settings

    if not sys.stdin.isatty() and not args.items and not system_option:
        input_stream = sys.stdin.read()
        args.items = input_stream.splitlines()

    PMenu(
        app_height=args.app_height,
        input_width=args.input_width,
        vertical=args.list,
        list_max_items=args.list_max_items,
        list_item_height=args.list_item_height,
        stdin_items=args.items,
        show_system_fonts=args.font,
        show_parsed_settings=args.settings
    )
