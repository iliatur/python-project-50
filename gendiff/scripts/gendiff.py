import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.print_help()