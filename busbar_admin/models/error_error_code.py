from enum import Enum


class ErrorErrorCode(str, Enum):
    CONFLICT = "conflict"
    FORBIDDEN = "forbidden"
    INTERNAL = "internal"
    INVALID_REQUEST = "invalid_request"
    METHOD_NOT_ALLOWED = "method_not_allowed"
    NOT_FOUND = "not_found"
    RATE_LIMITED = "rate_limited"
    UNAUTHORIZED = "unauthorized"
    VERSION_CONFLICT = "version_conflict"

    def __str__(self) -> str:
        return str(self.value)
