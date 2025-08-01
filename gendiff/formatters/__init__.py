from .json import format_json


def get_formatter(format_name):
    match format_name:
        case 'json':
            return format_json
        case _:
            raise ValueError(f"Unsupported format: {format_name}")