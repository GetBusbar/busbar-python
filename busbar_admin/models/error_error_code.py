from enum import StrEnum
from typing import Self


class ErrorErrorCode(StrEnum):
    ACTION_IN_FLIGHT = "action_in_flight"
    CONFLICT = "conflict"
    FORBIDDEN = "forbidden"
    IDEMPOTENCY_MISMATCH = "idempotency_mismatch"
    INTERNAL = "internal"
    INVALID_REQUEST = "invalid_request"
    METHOD_NOT_ALLOWED = "method_not_allowed"
    MUTATION_APPLIED = "mutation_applied"
    NOT_FOUND = "not_found"
    RATE_LIMITED = "rate_limited"
    REQUEST_TOO_LARGE = "request_too_large"
    UNAUTHORIZED = "unauthorized"
    UNAVAILABLE = "unavailable"
    UNPRICED_CLASS = "unpriced_class"
    VERSION_CONFLICT = "version_conflict"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, value: object) -> Self | None:
        # Error.code is explicitly extensible; preserve unknown strings without
        # adding arbitrary wire values to the class's named-member registry.
        if isinstance(value, str):
            member = str.__new__(cls, value)
            member._name_ = None
            member._value_ = value
            return member
        return None
