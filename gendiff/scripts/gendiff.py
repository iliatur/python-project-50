import argparse

from gendiff.diff import build_diff_tree
from gendiff.formatters import get_formatter
from gendiff.parser import parse_file


def generate_diff(path1, path2, formatter='stylish'):
    data1 = parse_file(path1)
    data2 = parse_file(path2)
    
    diff_tree = build_diff_tree(data1, data2)
    formatter = get_formatter(formatter)
    return formatter(diff_tree)


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        usage="%(prog)s [-h] [-f FORMAT] first_file second_file",
        description="Compares two configuration files and shows a difference.",
    )

    parser.add_argument("first_file", nargs="+")
    parser.add_argument("second_file", nargs="+")

    parser.add_argument(
        "-f", "--format", 
        nargs="?", 
        default='stylish', 
        help="set format of output"
    )
    args = parser.parse_args()

    path1 = args.first_file[0]
    path2 = args.second_file[0]
    formatter = args.format
    
    result = generate_diff(path1, path2, formatter)
    print(result)
