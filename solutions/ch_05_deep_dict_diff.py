"""Reference Solution: Recursive Deep Dictionary Diff Engine."""

def deep_diff(d1, d2):
    diff = {"added": {}, "removed": {}, "modified": {}}
    all_keys = set(d1.keys()).union(set(d2.keys()))
    for k in all_keys:
        if k not in d1:
            diff["added"][k] = d2[k]
        elif k not in d2:
            diff["removed"][k] = d1[k]
        elif d1[k] != d2[k]:
            if isinstance(d1[k], dict) and isinstance(d2[k], dict):
                nested = deep_diff(d1[k], d2[k])
                if nested["added"] or nested["removed"] or nested["modified"]:
                    diff["modified"][k] = nested
            else:
                diff["modified"][k] = {"old": d1[k], "new": d2[k]}
    return diff
