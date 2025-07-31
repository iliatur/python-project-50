import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        usage="%(prog)s [-h] [-f FORMAT] first_file second_file",
        description="Compares two configuration files and shows a difference.",
    )
        
    parser.add_argument('first_file')
    parser.add_argument('second_file')
