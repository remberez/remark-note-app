from enum import Enum


class OrderByDateFields(str, Enum):
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
