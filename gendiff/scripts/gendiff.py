import argparse


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
