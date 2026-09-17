"""Challenge 06: Dependency Graph Topological Resolver."""

class CycleDetectedError(Exception):
    pass

def topological_sort(graph):
    result = []
    visited = set()

    def dfs(node):
        # BUG: Lacks in-stack recursion tracking; infinite recursion on cyclic dependency
        if node in visited:
            return
        visited.add(node)
        for dep in graph.get(node, []):
            dfs(dep)
        result.append(node)

    for node in graph:
        dfs(node)
    return result
