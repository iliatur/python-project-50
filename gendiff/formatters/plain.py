
def stringify_plain(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, list):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return str(value)
    return f"'{value}'"


def format_plain(diff_tree, path=""):
    lines = []

    for node in diff_tree:
        key = node["key"]
        type_ = node["type"]
        property_path = f"{path}.{key}" if path else key

        match type_:
            case "added":
                value = stringify_plain(node["value"])
                lines.append(
                    f"Property '{property_path}' was added with value: {value}"
                )
            case "removed":
                
                lines.append(f"Property '{property_path}' was removed")
            case "changed":
                old = stringify_plain(node["old_value"])
                new = stringify_plain(node["new_value"])
                lines.append(
                    f"Property '{property_path}' was updated. From {old} to {new}"  # noqa: E501
                )
            case "nested":
                lines.append(format_plain(node["children"], property_path))
            case "unchanged":
                continue
    return "\n".join(lines)
