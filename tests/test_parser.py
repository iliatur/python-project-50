import os

from gendiff.scripts.parser import parse_file


def test_parse_json():
    path = os.path.join("tests", "test_data", "file1.json")
    print(path)
    result = parse_file(path)

    assert result == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
    }


def test_parse_yaml():
    path = os.path.join("tests", "test_data", "file2.json")
    result = parse_file(path)
    assert result == {"timeout": 20, "verbose": True, "host": "hexlet.io"}