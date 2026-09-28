from typing import Literal

UpdateCollectionItemBodyCondition = Literal[
    "F",
    "F+",
    "F-",
    "F/VF",
    "FR",
    "G",
    "G/VG",
    "MT",
    "NM",
    "NM+",
    "NM-",
    "NM/MT",
    "PR",
    "VF",
    "VF+",
    "VF-",
    "VF/NM",
    "VG",
    "VG+",
    "VG-",
    "VG/F",
]

UPDATE_COLLECTION_ITEM_BODY_CONDITION_VALUES: set[UpdateCollectionItemBodyCondition] = {
    "F",
    "F+",
    "F-",
    "F/VF",
    "FR",
    "G",
    "G/VG",
    "MT",
    "NM",
    "NM+",
    "NM-",
    "NM/MT",
    "PR",
    "VF",
    "VF+",
    "VF-",
    "VF/NM",
    "VG",
    "VG+",
    "VG-",
    "VG/F",
}


def check_update_collection_item_body_condition(value: str) -> UpdateCollectionItemBodyCondition:
    if value in UPDATE_COLLECTION_ITEM_BODY_CONDITION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_COLLECTION_ITEM_BODY_CONDITION_VALUES!r}")
