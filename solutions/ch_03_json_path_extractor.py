"""Reference Solution: Safe Nested JSON Path Extractor."""

def extract_json_path(data, path: str, default=None):
    if not path or data is None:
        return default
    keys = path.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict):
            if key in current:
                current = current[key]
            else:
                return default
        elif isinstance(current, list):
            if key.isdigit():
                idx = int(key)
                if 0 <= idx < len(current):
                    current = current[idx]
                else:
                    return default
            else:
                return default
        else:
            return default
    return current
