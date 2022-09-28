import argparse
import pathlib
import sys

from . import __version__
from .treemod import directoryTree


def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print('The specified root directory doesnt exist')
        sys.exit()
    tree = directoryTree(root_dir)
    tree.generate()


def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog='tree',
        description='TreeMod, a diretory tree generator',
        epilog='Thanks For Using TreeMod!'
    )
    parser.version = f'TreeMod v{__version__}'
    parser.add_argument('-v', '--version', action='version')
    parser.add_argument(
        'root_dir',
        metavar='ROOT_DIR',
        nargs='?',
        default='.',
        help='Generate a full directory tree starerting at the ROOT_DIR',
    )
    return parser.parse_args()
