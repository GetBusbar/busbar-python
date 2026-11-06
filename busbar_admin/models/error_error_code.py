from enum import StrEnum


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
