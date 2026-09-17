"""Challenge 08: High-Precision Financial Portfolio Allocator."""

def allocate_shares(total_capital: float, weights: dict) -> dict:
    # BUG: Float precision accumulates and sum of shares != total
    allocations = {}
    for asset, weight in weights.items():
        # BUG: Binary float multiplication loses exact cents
        allocations[asset] = round(total_capital * weight, 2)
    return allocations
