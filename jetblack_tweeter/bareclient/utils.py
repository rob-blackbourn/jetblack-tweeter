"""Utilities for sessions"""

from typing import List, Tuple


def to_lines(buf) -> Tuple[List[bytes], bytes]:
    lines: List[bytes] = []
    sep = b'\r\n'
    while sep:
        line, sep, rest = buf.partition(sep)
        if sep:
            lines.append(line)
            buf = rest
    return lines, buf
