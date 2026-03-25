from __future__ import annotations
from dataclasses import dataclass
from typing import List

@dataclass
class FilterOutput:
    input_signal: List[float]
    output_signal: List[float]

def simulate_biquad(input_signal: List[float]) -> FilterOutput:
    """
    Implements a second-order IIR filter:

        y[n] = (x[n] + x[n-1] + x[n-2] + y[n-1] + y[n-2]) / 8

    Assumes zero initial conditions.
    """

    # Delay elements for inputs and outputs
    x_prev1 = 0.0
    x_prev2 = 0.0
    y_prev1 = 0.0
    y_prev2 = 0.0

    output_signal: List[float] = []

    for current in input_signal:
        # Compute current output
        y_curr = (current + x_prev1 + x_prev2 + y_prev1 + y_prev2) / 8.0
        output_signal.append(y_curr)

        # Update state (shift registers)
        x_prev2 = x_prev1
        x_prev1 = current

        y_prev2 = y_prev1
        y_prev1 = y_curr

    return FilterOutput(input_signal, output_signal)


def print_results(result: FilterOutput) -> None:
    print("Second-Order Biquad Simulation")
    print(f"{'n':>3} {'Input':>10} {'Output':>12}")

    for idx, (inp, out) in enumerate(zip(result.input_signal, result.output_signal), start=1):
        print(f"{idx:>3} {inp:>10.2f} {out:>12.6f}")


if __name__ == "__main__":
    test_input = [100, 5, 500, 20, 250]

    result = simulate_biquad(test_input)
    print_results(result)
