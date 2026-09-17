"""Challenge 09: Markdown Table Robust Parser."""

def parse_markdown_table(table_str: str) -> list:
    lines = [line.strip() for line in table_str.strip().split("\n") if line.strip()]
    if len(lines) < 2:
        return []
    # BUG: Naive split on "|" breaks when cells contain escaped pipes `\|`
    headers = [col.strip() for col in lines[0].split("|")[1:-1]]
    rows = []
    for line in lines[2:]:
        cols = [col.strip() for col in line.split("|")[1:-1]]
        row_dict = dict(zip(headers, cols))
        rows.append(row_dict)
    return rows
