from .json import format_json
from .plain import format_plain
from .stylish import format_stylish


def get_formatter(format_name):
    match format_name:
        case 'stylish':
            return format_stylish
        case 'plain':
            return format_plain
        case 'json':
            return format_json
        case _:
            raise ValueError(f"Unsupported format: {format_name}")