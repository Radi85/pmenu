import argparse
import sys

from src.pmenu import PMenu


if __name__ == '__main__':
    """
    shell_program | pmenu
    shell_program | xargs pmenu
    """
    parser = argparse.ArgumentParser(description='pmenu')
    parser.add_argument('-H', '--app_height', type=int, help='App height')
    parser.add_argument('-i', '--list_item_height', type=int, help='List item height')
    parser.add_argument('-n', '--list_max_items', type=int, help='Total number of view items')
    parser.add_argument('-w', '--input_width', type=int, help='Width of search field')
    parser.add_argument('-l', '--list', action='store_true', help='Show vertically as list')
    parser.add_argument('items', nargs='*')

    args = parser.parse_args()

    if not sys.stdin.isatty() and not args.items:
        input_stream = sys.stdin.read()
        args.items = input_stream.splitlines()

    PMenu(
        app_height=args.app_height,
        input_width=args.input_width,
        vertical=args.list,
        list_max_items=args.list_max_items,
        list_item_height=args.list_item_height,
        stdin_items=args.items
    )
