"""Utilities for sessions"""

from typing import List, Mapping, Tuple

from baretypes import Header


def to_lines(buf) -> Tuple[List[bytes], bytes]:
    lines: List[bytes] = []
    sep = b'\r\n'
    while sep:
        line, sep, rest = buf.partition(sep)
        if sep:
            lines.append(line)
            buf = rest
    return lines, buf


def make_headers(headers: Mapping[str, str]) -> List[Header]:
    return [
        (name.lower().encode(), value.encode())
        for name, value in headers.items()
    ]
