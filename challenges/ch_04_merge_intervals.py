"""Challenge 04: Meeting & Range Interval Consolidation."""

def merge_intervals(intervals):
    if not intervals:
        return []
    # BUG: Forgets to sort intervals by start time
    merged = [intervals[0]]
    for current in intervals[1:]:
        prev_start, prev_end = merged[-1]
        cur_start, cur_end = current
        # BUG: Touching intervals (e.g. [1, 4] and [4, 5]) fail to merge due to strict inequality
        if cur_start < prev_end:
            merged[-1] = (prev_start, max(prev_end, cur_end))
        else:
            merged.append(current)
    return merged
