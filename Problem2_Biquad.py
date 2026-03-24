from __future__ import annotations
from dataclasses import dataclass
from typing import List

@dataclass
class BiquadResult:
    inputs: List[float]
    outputs: List[float]

def biquad_filter(inputs: List[float]) -> BiquadResult:
    """Second-order IIR (biquad) filter from Figure 2.

    Recurrence:
        y[n] = (x[n] + x[n-1] + x[n-2] + y[n-1] + y[n-2]) / 8

    Initial conditions: x[-1] = x[-2] = y[-1] = y[-2] = 0.
    Each input value corresponds to one RGB clock cycle.
    After recording y[n] the output register is cleared (sampled externally).
    """

    x1 = x2 = 0.0  # x[n-1], x[n-2]
    y1 = y2 = 0.0  # y[n-1], y[n-2]
    outputs: List[float] = []

    for x in inputs:
        y = (x + x1 + x2 + y1 + y2) / 8.0
        outputs.append(y)

        # Shift delay registers
        x2, x1 = x1, x
        y2, y1 = y1, y

    return BiquadResult(inputs, outputs)

if __name__ == "__main__":
    inp = [100, 5, 500, 20, 250]
    res = biquad_filter(inp)

    print("Biquad filter --- 5-cycle simulation")
    print(f"{'Cycle':>5} {'x[n]':>7} {'y[n]':>12}")
    for i, (x, y) in enumerate(zip(res.inputs, res.outputs), start=1):
        print(f"{i:5d} {x:7.1f} {y:12.6f}")
