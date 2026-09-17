"""Reference Solution: Dependency Graph Topological Resolver."""

class CycleDetectedError(Exception):
    pass

def topological_sort(graph):
    result = []
    visited = set()
    rec_stack = set()

    def dfs(node):
        if node in rec_stack:
            raise CycleDetectedError(f"Cycle detected at node {node}")
        if node in visited:
            return
        rec_stack.add(node)
        for dep in graph.get(node, []):
            dfs(dep)
        rec_stack.remove(node)
        visited.add(node)
        result.append(node)

    for node in sorted(graph.keys()):
        if node not in visited:
            dfs(node)
    return result
