"""Reference Solution: Markdown Table Robust Parser."""
import re

def parse_markdown_table(table_str: str) -> list:
    lines = [line.strip() for line in table_str.strip().split("\n") if line.strip()]
    if len(lines) < 3:
        return []

    def split_cells(line: str) -> list:
        tokens = re.split(r'(?<!\\)\|', line)
        if tokens and tokens[0] == "":
            tokens.pop(0)
        if tokens and tokens[-1] == "":
            tokens.pop()
        return [t.replace("\\|", "|").strip() for t in tokens]

    headers = split_cells(lines[0])
    rows = []
    for line in lines[2:]:
        cells = split_cells(line)
        if len(cells) < len(headers):
            cells += [""] * (len(headers) - len(cells))
        rows.append(dict(zip(headers, cells[:len(headers)])))
    return rows
