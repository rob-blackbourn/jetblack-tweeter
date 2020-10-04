"""Test for barclient utils"""

from jetblack_tweeter.bareclient.utils import to_lines


def test_to_lines() -> None:
    """Test for to_lines"""
    lines, rest = to_lines(b'no line ending')
    assert lines == [] and rest == b'no line ending'

    lines, rest = to_lines(b'one line\r\n')
    assert lines == [b'one line'] and rest == b''

    lines, rest = to_lines(b'first\r\nsecond\r\n')
    assert lines == [b'first', b'second'] and rest == b''

    lines, rest = to_lines(b'first\r\nsecond\r\nincomplete')
    assert lines == [b'first', b'second'] and rest == b'incomplete'
