from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_config_settings_config_settings_replacement_admin_tls_type_0 import (
        PutConfigSettingsConfigSettingsReplacementAdminTlsType0,
    )
    from ..models.put_config_settings_config_settings_replacement_advanced_type_0 import (
        PutConfigSettingsConfigSettingsReplacementAdvancedType0,
    )
    from ..models.put_config_settings_config_settings_replacement_health_type_0 import (
        PutConfigSettingsConfigSettingsReplacementHealthType0,
    )
    from ..models.put_config_settings_config_settings_replacement_limits_type_0 import (
        PutConfigSettingsConfigSettingsReplacementLimitsType0,
    )
    from ..models.put_config_settings_config_settings_replacement_plugin_rate_cards_type_0 import (
        PutConfigSettingsConfigSettingsReplacementPluginRateCardsType0,
    )
    from ..models.put_config_settings_config_settings_replacement_rate_card_type_0 import (
        PutConfigSettingsConfigSettingsReplacementRateCardType0,
    )
    from ..models.put_config_settings_config_settings_replacement_routing_type_0 import (
        PutConfigSettingsConfigSettingsReplacementRoutingType0,
    )
    from ..models.put_config_settings_config_settings_replacement_security_type_0 import (
        PutConfigSettingsConfigSettingsReplacementSecurityType0,
    )
    from ..models.put_config_settings_config_settings_replacement_store_type_0 import (
        PutConfigSettingsConfigSettingsReplacementStoreType0,
    )
    from ..models.put_config_settings_config_settings_replacement_tls_type_0 import (
        PutConfigSettingsConfigSettingsReplacementTlsType0,
    )


T = TypeVar("T", bound="PutConfigSettingsConfigSettingsReplacement")


@_attrs_define(repr=False)
class PutConfigSettingsConfigSettingsReplacement:
    """Replace named root settings sections, merging omitted sections with the existing overlay. Null preserves a section.
    A mutable configuration stores changes through its configured Store; a locked configuration refuses changes. Listen,
    TLS and Store changes require restart. Unknown or retired fields, including persist, are refused. Nested section
    parsers and normal configuration validation remain authoritative.

        Attributes:
            listen (None | str | Unset):
            tls (list[Any] | None | PutConfigSettingsConfigSettingsReplacementTlsType0 | Unset): Inbound TLS: cert and key
                SecretRefs, plus optional client_ca.
            admin_listen (None | str | Unset):
            admin_tls (list[Any] | None | PutConfigSettingsConfigSettingsReplacementAdminTlsType0 | Unset): Admin listener
                TLS: cert and key SecretRefs, plus optional client_ca.
            admin_require_mtls (bool | None | Unset):
            rate_card (None | PutConfigSettingsConfigSettingsReplacementRateCardType0 | Unset):
            plugin_rate_cards (None | PutConfigSettingsConfigSettingsReplacementPluginRateCardsType0 | Unset): Exact common
                measurement rates by plugin kind, actual configured namespace, and declared class. Integer or decimal-string
                micro-units per quantity; missing rates remain unpriced. The whole map is replaced when supplied, including an
                empty map to clear it.
            per_request_fee (int | None | Unset):
            store (list[Any] | None | PutConfigSettingsConfigSettingsReplacementStoreType0 | Unset): Store selection: module
                and module-owned settings; requires restart.
            security (list[Any] | None | PutConfigSettingsConfigSettingsReplacementSecurityType0 | Unset): Per-field
                SecurityPatch; omitted or null members preserve their value.
            limits (list[Any] | None | PutConfigSettingsConfigSettingsReplacementLimitsType0 | Unset): Per-field
                LimitsPatch; omitted members preserve their value. Null datagram_line_memory_bytes explicitly disables that
                limit.
            advanced (list[Any] | None | PutConfigSettingsConfigSettingsReplacementAdvancedType0 | Unset): Per-field
                AdvancedPatch; omitted or null members preserve their value.
            health (list[Any] | None | PutConfigSettingsConfigSettingsReplacementHealthType0 | Unset): Per-field
                HealthPatch; omitted or null members preserve their value.
            routing (list[Any] | None | PutConfigSettingsConfigSettingsReplacementRoutingType0 | Unset): Per-field
                RoutingPatch; omitted or null members preserve their value.
    """

    listen: None | str | Unset = UNSET
    tls: list[Any] | None | PutConfigSettingsConfigSettingsReplacementTlsType0 | Unset = UNSET
    admin_listen: None | str | Unset = UNSET
    admin_tls: list[Any] | None | PutConfigSettingsConfigSettingsReplacementAdminTlsType0 | Unset = UNSET
    admin_require_mtls: bool | None | Unset = UNSET
    rate_card: None | PutConfigSettingsConfigSettingsReplacementRateCardType0 | Unset = UNSET
    plugin_rate_cards: None | PutConfigSettingsConfigSettingsReplacementPluginRateCardsType0 | Unset = UNSET
    per_request_fee: int | None | Unset = UNSET
    store: list[Any] | None | PutConfigSettingsConfigSettingsReplacementStoreType0 | Unset = UNSET
    security: list[Any] | None | PutConfigSettingsConfigSettingsReplacementSecurityType0 | Unset = UNSET
    limits: list[Any] | None | PutConfigSettingsConfigSettingsReplacementLimitsType0 | Unset = UNSET
    advanced: list[Any] | None | PutConfigSettingsConfigSettingsReplacementAdvancedType0 | Unset = UNSET
    health: list[Any] | None | PutConfigSettingsConfigSettingsReplacementHealthType0 | Unset = UNSET
    routing: list[Any] | None | PutConfigSettingsConfigSettingsReplacementRoutingType0 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.put_config_settings_config_settings_replacement_admin_tls_type_0 import (
            PutConfigSettingsConfigSettingsReplacementAdminTlsType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_advanced_type_0 import (
            PutConfigSettingsConfigSettingsReplacementAdvancedType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_health_type_0 import (
            PutConfigSettingsConfigSettingsReplacementHealthType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_limits_type_0 import (
            PutConfigSettingsConfigSettingsReplacementLimitsType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_plugin_rate_cards_type_0 import (
            PutConfigSettingsConfigSettingsReplacementPluginRateCardsType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_rate_card_type_0 import (
            PutConfigSettingsConfigSettingsReplacementRateCardType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_routing_type_0 import (
            PutConfigSettingsConfigSettingsReplacementRoutingType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_security_type_0 import (
            PutConfigSettingsConfigSettingsReplacementSecurityType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_store_type_0 import (
            PutConfigSettingsConfigSettingsReplacementStoreType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_tls_type_0 import (
            PutConfigSettingsConfigSettingsReplacementTlsType0,  # noqa: PLC0415
        )

        listen: None | str | Unset
        if isinstance(self.listen, Unset):
            listen = UNSET
        else:
            listen = self.listen

        tls: dict[str, Any] | list[Any] | None | Unset
        if isinstance(self.tls, Unset):
            tls = UNSET
        elif isinstance(self.tls, PutConfigSettingsConfigSettingsReplacementTlsType0):
            tls = self.tls.to_dict()
        elif isinstance(self.tls, list):
            tls = self.tls

        else:
            tls = self.tls

        admin_listen: None | str | Unset
        if isinstance(self.admin_listen, Unset):
            admin_listen = UNSET
        else:
            admin_listen = self.admin_listen

        admin_tls: dict[str, Any] | list[Any] | None | Unset
        if isinstance(self.admin_tls, Unset):
            admin_tls = UNSET
        elif isinstance(self.admin_tls, PutConfigSettingsConfigSettingsReplacementAdminTlsType0):
            admin_tls = self.admin_tls.to_dict()
        elif isinstance(self.admin_tls, list):
            admin_tls = self.admin_tls

        else:
            admin_tls = self.admin_tls

        admin_require_mtls: bool | None | Unset
        if isinstance(self.admin_require_mtls, Unset):
            admin_require_mtls = UNSET
        else:
            admin_require_mtls = self.admin_require_mtls

        rate_card: dict[str, Any] | None | Unset
        if isinstance(self.rate_card, Unset):
            rate_card = UNSET
        elif isinstance(self.rate_card, PutConfigSettingsConfigSettingsReplacementRateCardType0):
            rate_card = self.rate_card.to_dict()
        else:
            rate_card = self.rate_card

        plugin_rate_cards: dict[str, Any] | None | Unset
        if isinstance(self.plugin_rate_cards, Unset):
            plugin_rate_cards = UNSET
        elif isinstance(self.plugin_rate_cards, PutConfigSettingsConfigSettingsReplacementPluginRateCardsType0):
            plugin_rate_cards = self.plugin_rate_cards.to_dict()
        else:
            plugin_rate_cards = self.plugin_rate_cards

        per_request_fee: int | None | Unset
        if isinstance(self.per_request_fee, Unset):
            per_request_fee = UNSET
        else:
            per_request_fee = self.per_request_fee

        store: dict[str, Any] | list[Any] | None | Unset
        if isinstance(self.store, Unset):
            store = UNSET
        elif isinstance(self.store, PutConfigSettingsConfigSettingsReplacementStoreType0):
            store = self.store.to_dict()
        elif isinstance(self.store, list):
            store = self.store

        else:
            store = self.store

        security: dict[str, Any] | list[Any] | None | Unset
        if isinstance(self.security, Unset):
            security = UNSET
        elif isinstance(self.security, PutConfigSettingsConfigSettingsReplacementSecurityType0):
            security = self.security.to_dict()
        elif isinstance(self.security, list):
            security = self.security

        else:
            security = self.security

        limits: dict[str, Any] | list[Any] | None | Unset
        if isinstance(self.limits, Unset):
            limits = UNSET
        elif isinstance(self.limits, PutConfigSettingsConfigSettingsReplacementLimitsType0):
            limits = self.limits.to_dict()
        elif isinstance(self.limits, list):
            limits = self.limits

        else:
            limits = self.limits

        advanced: dict[str, Any] | list[Any] | None | Unset
        if isinstance(self.advanced, Unset):
            advanced = UNSET
        elif isinstance(self.advanced, PutConfigSettingsConfigSettingsReplacementAdvancedType0):
            advanced = self.advanced.to_dict()
        elif isinstance(self.advanced, list):
            advanced = self.advanced

        else:
            advanced = self.advanced

        health: dict[str, Any] | list[Any] | None | Unset
        if isinstance(self.health, Unset):
            health = UNSET
        elif isinstance(self.health, PutConfigSettingsConfigSettingsReplacementHealthType0):
            health = self.health.to_dict()
        elif isinstance(self.health, list):
            health = self.health

        else:
            health = self.health

        routing: dict[str, Any] | list[Any] | None | Unset
        if isinstance(self.routing, Unset):
            routing = UNSET
        elif isinstance(self.routing, PutConfigSettingsConfigSettingsReplacementRoutingType0):
            routing = self.routing.to_dict()
        elif isinstance(self.routing, list):
            routing = self.routing

        else:
            routing = self.routing

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if listen is not UNSET:
            field_dict["listen"] = listen
        if tls is not UNSET:
            field_dict["tls"] = tls
        if admin_listen is not UNSET:
            field_dict["admin_listen"] = admin_listen
        if admin_tls is not UNSET:
            field_dict["admin_tls"] = admin_tls
        if admin_require_mtls is not UNSET:
            field_dict["admin_require_mtls"] = admin_require_mtls
        if rate_card is not UNSET:
            field_dict["rate_card"] = rate_card
        if plugin_rate_cards is not UNSET:
            field_dict["plugin_rate_cards"] = plugin_rate_cards
        if per_request_fee is not UNSET:
            field_dict["per_request_fee"] = per_request_fee
        if store is not UNSET:
            field_dict["store"] = store
        if security is not UNSET:
            field_dict["security"] = security
        if limits is not UNSET:
            field_dict["limits"] = limits
        if advanced is not UNSET:
            field_dict["advanced"] = advanced
        if health is not UNSET:
            field_dict["health"] = health
        if routing is not UNSET:
            field_dict["routing"] = routing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_config_settings_config_settings_replacement_admin_tls_type_0 import (
            PutConfigSettingsConfigSettingsReplacementAdminTlsType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_advanced_type_0 import (
            PutConfigSettingsConfigSettingsReplacementAdvancedType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_health_type_0 import (
            PutConfigSettingsConfigSettingsReplacementHealthType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_limits_type_0 import (
            PutConfigSettingsConfigSettingsReplacementLimitsType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_plugin_rate_cards_type_0 import (
            PutConfigSettingsConfigSettingsReplacementPluginRateCardsType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_rate_card_type_0 import (
            PutConfigSettingsConfigSettingsReplacementRateCardType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_routing_type_0 import (
            PutConfigSettingsConfigSettingsReplacementRoutingType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_security_type_0 import (
            PutConfigSettingsConfigSettingsReplacementSecurityType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_store_type_0 import (
            PutConfigSettingsConfigSettingsReplacementStoreType0,  # noqa: PLC0415
        )
        from ..models.put_config_settings_config_settings_replacement_tls_type_0 import (
            PutConfigSettingsConfigSettingsReplacementTlsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_listen(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listen = _parse_listen(d.pop("listen", UNSET))

        def _parse_tls(data: object) -> list[Any] | None | PutConfigSettingsConfigSettingsReplacementTlsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tls_type_0 = PutConfigSettingsConfigSettingsReplacementTlsType0.from_dict(data)

                return tls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tls_type_1 = cast(list[Any], data)

                return tls_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for tls")

        tls = _parse_tls(d.pop("tls", UNSET))

        def _parse_admin_listen(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_listen = _parse_admin_listen(d.pop("admin_listen", UNSET))

        def _parse_admin_tls(
            data: object,
        ) -> list[Any] | None | PutConfigSettingsConfigSettingsReplacementAdminTlsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                admin_tls_type_0 = PutConfigSettingsConfigSettingsReplacementAdminTlsType0.from_dict(data)

                return admin_tls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                admin_tls_type_1 = cast(list[Any], data)

                return admin_tls_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for admin_tls")

        admin_tls = _parse_admin_tls(d.pop("admin_tls", UNSET))

        def _parse_admin_require_mtls(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        admin_require_mtls = _parse_admin_require_mtls(d.pop("admin_require_mtls", UNSET))

        def _parse_rate_card(data: object) -> None | PutConfigSettingsConfigSettingsReplacementRateCardType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rate_card_type_0 = PutConfigSettingsConfigSettingsReplacementRateCardType0.from_dict(data)

                return rate_card_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for rate_card")

        rate_card = _parse_rate_card(d.pop("rate_card", UNSET))

        def _parse_plugin_rate_cards(
            data: object,
        ) -> None | PutConfigSettingsConfigSettingsReplacementPluginRateCardsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                plugin_rate_cards_type_0 = PutConfigSettingsConfigSettingsReplacementPluginRateCardsType0.from_dict(
                    data
                )

                return plugin_rate_cards_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for plugin_rate_cards")

        plugin_rate_cards = _parse_plugin_rate_cards(d.pop("plugin_rate_cards", UNSET))

        def _parse_per_request_fee(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        per_request_fee = _parse_per_request_fee(d.pop("per_request_fee", UNSET))

        def _parse_store(
            data: object,
        ) -> list[Any] | None | PutConfigSettingsConfigSettingsReplacementStoreType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                store_type_0 = PutConfigSettingsConfigSettingsReplacementStoreType0.from_dict(data)

                return store_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                store_type_1 = cast(list[Any], data)

                return store_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for store")

        store = _parse_store(d.pop("store", UNSET))

        def _parse_security(
            data: object,
        ) -> list[Any] | None | PutConfigSettingsConfigSettingsReplacementSecurityType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                security_type_0 = PutConfigSettingsConfigSettingsReplacementSecurityType0.from_dict(data)

                return security_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                security_type_1 = cast(list[Any], data)

                return security_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for security")

        security = _parse_security(d.pop("security", UNSET))

        def _parse_limits(
            data: object,
        ) -> list[Any] | None | PutConfigSettingsConfigSettingsReplacementLimitsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                limits_type_0 = PutConfigSettingsConfigSettingsReplacementLimitsType0.from_dict(data)

                return limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                limits_type_1 = cast(list[Any], data)

                return limits_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for limits")

        limits = _parse_limits(d.pop("limits", UNSET))

        def _parse_advanced(
            data: object,
        ) -> list[Any] | None | PutConfigSettingsConfigSettingsReplacementAdvancedType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                advanced_type_0 = PutConfigSettingsConfigSettingsReplacementAdvancedType0.from_dict(data)

                return advanced_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                advanced_type_1 = cast(list[Any], data)

                return advanced_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for advanced")

        advanced = _parse_advanced(d.pop("advanced", UNSET))

        def _parse_health(
            data: object,
        ) -> list[Any] | None | PutConfigSettingsConfigSettingsReplacementHealthType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                health_type_0 = PutConfigSettingsConfigSettingsReplacementHealthType0.from_dict(data)

                return health_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                health_type_1 = cast(list[Any], data)

                return health_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for health")

        health = _parse_health(d.pop("health", UNSET))

        def _parse_routing(
            data: object,
        ) -> list[Any] | None | PutConfigSettingsConfigSettingsReplacementRoutingType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                routing_type_0 = PutConfigSettingsConfigSettingsReplacementRoutingType0.from_dict(data)

                return routing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                routing_type_1 = cast(list[Any], data)

                return routing_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid value for routing")

        routing = _parse_routing(d.pop("routing", UNSET))

        if d:
            raise ValueError("Unexpected fields for PutConfigSettingsConfigSettingsReplacement")
        put_config_settings_config_settings_replacement = cls(
            listen=listen,
            tls=tls,
            admin_listen=admin_listen,
            admin_tls=admin_tls,
            admin_require_mtls=admin_require_mtls,
            rate_card=rate_card,
            plugin_rate_cards=plugin_rate_cards,
            per_request_fee=per_request_fee,
            store=store,
            security=security,
            limits=limits,
            advanced=advanced,
            health=health,
            routing=routing,
        )

        return put_config_settings_config_settings_replacement
