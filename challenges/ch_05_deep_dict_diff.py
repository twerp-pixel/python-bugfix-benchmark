"""Challenge 05: Recursive Deep Dictionary Diff Engine."""

def deep_diff(d1, d2):
    diff = {"added": {}, "removed": {}, "modified": {}}
    for k in d1:
        if k not in d2:
            diff["removed"][k] = d1[k]
        elif d1[k] != d2[k]:
            # BUG: Recurses even when one of the values is not a dictionary
            if isinstance(d1[k], dict) or isinstance(d2[k], dict):
                nested = deep_diff(d1[k], d2[k])
                diff["modified"][k] = nested
            else:
                diff["modified"][k] = {"old": d1[k], "new": d2[k]}
    # BUG: Fails to detect new keys present in d2 but absent in d1
    return diff
