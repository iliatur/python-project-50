
def stringify(value, depth):
    if not isinstance(value, dict):
        if value is None:
            return 'null'
        if isinstance(value, bool):
            return str(value).lower()
        return str(value)

    indent = " " * (depth + 4)
    lines = []
    for k, v in value.items():
        lines.append(f"{indent}{k}: {stringify(v, depth + 4)}")
    return "{\n" + "\n".join(lines) + "\n" + " " * depth + "}"


def format_stylish(diff_tree, depth=2):
    lines = []
    indent = " " * depth
    for node in diff_tree:
        key = node["key"]
        type_ = node["type"]

        match type_:
            case "added":
                lines.append(
                    f"{indent}+ {key}: {stringify(node['value'], 
                    depth + 2)}"
                )
            case "removed":
                lines.append(
                    f"{indent}- {key}: {stringify(node['value'],
                    depth + 2)}"
                )
            case "unchanged":
                lines.append(
                    f"{indent}  {key}: {stringify(node['value'],
                    depth + 2)}"
                )
            case "changed":
                lines.append(
                    f"{indent}- {key}: {stringify(node['old_value'],
                    depth + 2)}"
                )
                lines.append(
                    f"{indent}+ {key}: {stringify(node['new_value'],
                    depth + 2)}"
                )
            case "nested":
                children = format_stylish(node["children"], depth + 4)
                lines.append(f"{indent}  {key}: {children}")
    return "{\n" + "\n".join(lines) + "\n" + " " * (depth - 2) + "}"
