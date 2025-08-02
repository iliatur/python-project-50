import os

import pytest

from gendiff.scripts.gendiff import generate_diff


FIXTURES_DIR = "tests/test_data"


def load_test_data(name):
    path = os.path.join(FIXTURES_DIR, name)
    with open(path, 'r') as f:
        return f.read().strip() 


@pytest.mark.parametrize("file1, file2, formatter, expected_file", [
    ("recursive1.json", "recursive2.json", "stylish", "expected_stylish.txt"),
    ("recursive1.yaml", "recursive2.yaml", "stylish", "expected_stylish.txt"),
    ("recursive1.json", "recursive2.json", "plain", "expected_plain.txt"),
    ("recursive1.yaml", "recursive2.yaml", "plain", "expected_plain.txt"),
    ("recursive1.json", "recursive2.json", "json", "expected_json.txt"),
    ("recursive1.yaml", "recursive2.yaml", "json", "expected_json.txt"),
])
def test_generate_diff(file1, file2, formatter, expected_file):
    path1 = os.path.join(FIXTURES_DIR, file1)
    path2 = os.path.join(FIXTURES_DIR, file2)
    expected = load_test_data(expected_file)

    result = generate_diff(path1, path2, formatter=formatter)
    assert result == expected
