import pytest
from ch_09_markdown_table_parser import parse_markdown_table

def test_standard_table():
    md = """
    | Name | Role |
    |---|---|
    | Linus | Kernel |
    | Guido | Python |
    """
    rows = parse_markdown_table(md)
    assert len(rows) == 2
    assert rows[0]["Name"] == "Linus"
    assert rows[1]["Role"] == "Python"

@pytest.mark.edge_case
def test_edge_escaped_pipes():
    md = """
    | Expression | Description |
    |---|---|
    | a \\|\\| b | Logical OR |
    """
    rows = parse_markdown_table(md)
    assert len(rows) == 1
    assert rows[0]["Expression"] == "a || b"
    assert rows[0]["Description"] == "Logical OR"
