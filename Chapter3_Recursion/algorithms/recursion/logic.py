"""
Pure recursion examples implementation.
No Manim imports - outputs step-by-step states.
"""
from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class CountdownState:
    """Represents one step in countdown recursion."""
    value: int
    is_base_case: bool
    action: str  # "call", "base_reached", "return"
    depth: int


@dataclass
class FactorialState:
    """Represents one step in factorial recursion."""
    n: int
    is_base_case: bool
    action: str  # "call", "base_reached", "computing", "return"
    depth: int
    partial_result: int = None


def countdown_steps(start: int) -> List[CountdownState]:
    """
    Generate step-by-step states for countdown recursion.
    
    countdown(n):
        if n <= 0:  # base case
            return
        print(n)
        countdown(n - 1)  # recursive case
    """
    states = []
    
    def _countdown(n, depth):
        # Record call
        states.append(CountdownState(
            value=n,
            is_base_case=(n <= 0),
            action="call",
            depth=depth
        ))
        
        if n <= 0:
            # Base case reached
            states.append(CountdownState(
                value=n,
                is_base_case=True,
                action="base_reached",
                depth=depth
            ))
            return
        
        # Recursive case - continue
        _countdown(n - 1, depth + 1)
        
        # Return
        states.append(CountdownState(
            value=n,
            is_base_case=False,
            action="return",
            depth=depth
        ))
    
    _countdown(start, 0)
    return states


def factorial_steps(n: int) -> List[FactorialState]:
    """
    Generate step-by-step states for factorial recursion.
    
    factorial(n):
        if n == 1:  # base case
            return 1
        return n * factorial(n - 1)  # recursive case
    """
    states = []
    
    def _factorial(x, depth):
        # Record call
        states.append(FactorialState(
            n=x,
            is_base_case=(x == 1),
            action="call",
            depth=depth
        ))
        
        if x == 1:
            # Base case
            states.append(FactorialState(
                n=x,
                is_base_case=True,
                action="base_reached",
                depth=depth,
                partial_result=1
            ))
            return 1
        
        # Recursive call
        result = _factorial(x - 1, depth + 1)
        
        # Computing result
        computed = x * result
        states.append(FactorialState(
            n=x,
            is_base_case=False,
            action="computing",
            depth=depth,
            partial_result=computed
        ))
        
        # Return
        states.append(FactorialState(
            n=x,
            is_base_case=False,
            action="return",
            depth=depth,
            partial_result=computed
        ))
        
        return computed
    
    _factorial(n, 0)
    return states


def sum_recursive_steps(arr: List[int]) -> List[dict]:
    """
    Generate step-by-step states for recursive sum.
    
    sum(arr):
        if len(arr) == 0:  # base case
            return 0
        return arr[0] + sum(arr[1:])  # recursive case
    """
    states = []
    
    def _sum(arr, depth):
        states.append({
            "array": arr.copy(),
            "is_base_case": len(arr) == 0,
            "action": "call",
            "depth": depth
        })
        
        if len(arr) == 0:
            states.append({
                "array": arr.copy(),
                "is_base_case": True,
                "action": "return",
                "depth": depth,
                "result": 0
            })
            return 0
        
        rest_sum = _sum(arr[1:], depth + 1)
        total = arr[0] + rest_sum
        
        states.append({
            "array": arr.copy(),
            "is_base_case": False,
            "action": "return",
            "depth": depth,
            "result": total
        })
        
        return total
    
    _sum(arr, 0)
    return states


# Complexity information
RECURSION_COMPLEXITY = {
    "countdown": {
        "time": "O(n)",
        "space": "O(n)",  # stack frames
        "description": "Linear recursion depth"
    },
    "factorial": {
        "time": "O(n)",
        "space": "O(n)",  # stack frames
        "description": "Linear recursion depth"
    },
    "fibonacci_naive": {
        "time": "O(2^n)",
        "space": "O(n)",
        "description": "Exponential due to repeated calls"
    },
}
