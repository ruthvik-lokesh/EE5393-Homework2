from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class FibonacciRun:
    seed_a: int
    seed_b: int
    iterations: int
    sequence: List[Tuple[int, int]]

def run_fibonacci(seed_a: int, seed_b: int, iterations: int = 12) -> FibonacciRun:
    """
    Perform iterative Fibonacci updates:
        (a, b) -> (b, a + b)
    for a fixed number of iterations.
    """
    a, b = seed_a, seed_b
    sequence: List[Tuple[int, int]] = [(a, b)]

    for _ in range(iterations):
        next_a = b
        next_b = a + b
        a, b = next_a, next_b
        sequence.append((a, b))

    return FibonacciRun(seed_a, seed_b, iterations, sequence)


def display_run(result: FibonacciRun) -> None:
    print(f"Start: ({result.seed_a}, {result.seed_b}) | Steps: {result.iterations}")
    print("Step   A        B")

    for idx, (a_val, b_val) in enumerate(result.sequence):
        print(f"{idx:>4} {a_val:>8} {b_val:>8}")

    final_a, final_b = result.sequence[-1]
    print(f"Result -> A: {final_a}, B: {final_b}\n")


if __name__ == "__main__":
    test_cases = [(0, 1), (3, 7)]

    for a_init, b_init in test_cases:
        outcome = run_fibonacci(a_init, b_init, 12)
        display_run(outcome)
