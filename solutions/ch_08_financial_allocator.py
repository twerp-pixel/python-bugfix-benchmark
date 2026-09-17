"""Reference Solution: High-Precision Financial Portfolio Allocator."""
from decimal import Decimal, ROUND_HALF_EVEN

def allocate_shares(total_capital: str, weights: dict) -> dict:
    cap = Decimal(str(total_capital))
    allocations = {}
    allocated_sum = Decimal("0.00")
    
    items = list(weights.items())
    for i, (asset, weight_str) in enumerate(items):
        weight = Decimal(str(weight_str))
        if i == len(items) - 1:
            amount = cap - allocated_sum
        else:
            amount = (cap * weight).quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)
            allocated_sum += amount
        allocations[asset] = str(amount)
    return allocations
