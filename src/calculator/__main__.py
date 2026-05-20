"""CLI entry point: `python -m calculator 2 + 3`."""
import sys

from calculator.operations import add, div, mul, sub

OPS = {"+": add, "-": sub, "*": mul, "x": mul, "/": div}


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) != 3:
        print("usage: calculator <a> <op> <b>", file=sys.stderr)
        return 2
    a_raw, op, b_raw = argv
    try:
        a, b = float(a_raw), float(b_raw)
    except ValueError:
        print(f"error: operands must be numbers, got {a_raw!r} and {b_raw!r}", file=sys.stderr)
        return 2
    if op not in OPS:
        print(f"error: unknown operator {op!r}; expected one of {sorted(OPS)}", file=sys.stderr)
        return 2
    print(OPS[op](a, b))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
