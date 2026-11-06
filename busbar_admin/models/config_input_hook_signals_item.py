from enum import StrEnum


class ConfigInputHookSignalsItem(StrEnum):
    CANDIDATE_BREAKER_STATE = "candidate_breaker_state"
    CANDIDATE_ERROR_RATE = "candidate_error_rate"
    CANDIDATE_LATENCY_P95_MS = "candidate_latency_p95_ms"
    CANDIDATE_ROUTE_COST = "candidate_route_cost"
    REQUESTED_MODEL = "requested_model"
    REQUEST_MESSAGE_COUNT = "request_message_count"
    REQUEST_SYSTEM_CHARS = "request_system_chars"
    REQUEST_TOOL_COUNT = "request_tool_count"
    REQUEST_TOTAL_CHARS = "request_total_chars"
    RESPONSE_TOKENS_OUT = "response_tokens_out"
    ROUTING_POLICY = "routing_policy"

    def __str__(self) -> str:
        return str(self.value)
