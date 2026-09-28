from typing import Literal

AddIssueToCollectionBodyCondition = Literal[
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

ADD_ISSUE_TO_COLLECTION_BODY_CONDITION_VALUES: set[AddIssueToCollectionBodyCondition] = {
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


def check_add_issue_to_collection_body_condition(value: str) -> AddIssueToCollectionBodyCondition:
    if value in ADD_ISSUE_TO_COLLECTION_BODY_CONDITION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ADD_ISSUE_TO_COLLECTION_BODY_CONDITION_VALUES!r}")
