"""Utilities"""

from typing import Any, List, Mapping, Optional

from .types import BoundingBox, Location


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


def optional_int_list_to_str(
        values: Optional[List[int]],
        default: Optional[str] = None
) -> Optional[str]:
    return int_list_to_str(values) if values else default


def clean_dict(data: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        key: value
        for key, value in data.items()
        if value is not None
    }


def clean_optional_dict(
        data: Optional[Mapping[str, Any]]
) -> Optional[Mapping[str, Any]]:
    return clean_dict(data) if data is not None else None


def bool_to_str(value: bool) -> str:
    return 'true' if value else 'false'


def optional_bool_to_str(
        value: Optional[bool],
        default: Optional[str] = None
) -> Optional[str]:
    return bool_to_str(value) if value is not None else default


def location_to_str(value: Location) -> str:
    longitude, latitude = value
    return f'{longitude},{latitude}'


def optional_location_to_str(
        value: Optional[Location],
        default: Optional[str] = None
) -> Optional[str]:
    return location_to_str(value) if value is not None else default


def bounding_box_to_str(value: BoundingBox) -> str:
    top_left, bottom_right = value
    return f'{location_to_str(top_left)},{location_to_str(bottom_right)}'


def optional_bounding_box_to_str(
        value: Optional[BoundingBox],
        default: Optional[str] = None
) -> Optional[str]:
    return bounding_box_to_str(value) if value is not None else default


def bounding_box_list_to_str(value: List[BoundingBox]) -> str:
    return ",".join(bounding_box_to_str(x) for x in value)


def optional_bounding_box_list_to_str(
        value: Optional[List[BoundingBox]],
        default: Optional[str] = None
) -> Optional[str]:
    return bounding_box_list_to_str(value) if value is not None else default
