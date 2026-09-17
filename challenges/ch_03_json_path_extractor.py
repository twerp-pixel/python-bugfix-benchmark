"""Challenge 03: Safe Nested JSON Path Extractor."""

def extract_json_path(data, path: str, default=None):
    if not path:
        return default
    keys = path.split(".")
    current = data
    for key in keys:
        try:
            if key.isdigit() and isinstance(current, list):
                current = current[int(key)]
            else:
                current = current.get(key)
            # BUG: Confuses falsy values (0, False, "") with missing keys
            if not current:
                return default
        except (AttributeError, IndexError, TypeError):
            return default
    return current
