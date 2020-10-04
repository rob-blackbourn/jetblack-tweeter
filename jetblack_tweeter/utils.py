"""Utilities"""

from typing import Any, List, Mapping, Optional


def str_list_to_str(values: List[str]) -> str:
    return ','.join(values)


def optional_str_list_to_str(
        values: Optional[List[str]],
        default: Optional[str] = None
) -> Optional[str]:
    return str_list_to_str(values) if values else default


def int_list_to_str(values: List[int]) -> str:
    return ','.join(
        str(value)
        for value in values
    )


def optional_int_list_to_str(values: Optional[List[int]]) -> Optional[str]:
    return int_list_to_str(values) if values else None


def clean_dict(data: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        key: value
        for key, value in data.items()
        if value is not None
    }


def clean_optional_dict(data: Optional[Mapping[str, Any]]) -> Optional[Mapping[str, Any]]:
    return clean_dict(data) if data is not None else None


def bool_to_str(value: bool) -> str:
    return 'true' if value else 'false'


def optional_bool_to_str(value: Optional[bool], default: Optional[str] = None) -> Optional[str]:
    return bool_to_str(value) if value is not None else default
