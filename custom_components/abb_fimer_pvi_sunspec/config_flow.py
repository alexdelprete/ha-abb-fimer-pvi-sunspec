"""Config flow for ABB FIMER PVI SunSpec."""

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PORT
from homeassistant.core import callback

from .const import (
    CONF_BASE_ADDR,
    CONF_DEVICE_ID,
    CONF_SCAN_INTERVAL,
    DEFAULT_BASE_ADDR,
    DEFAULT_DEVICE_ID,
    DEFAULT_PORT,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
    MAX_SCAN_INTERVAL,
    MIN_SCAN_INTERVAL,
)

_LOGGER = logging.getLogger(__name__)


class ABBFimerPVISunSpecConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for ABB FIMER PVI SunSpec."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.FlowResult:
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # TODO: Validate connection to inverter
            # TODO: Discover SunSpec models
            # TODO: Create unique_id based on serial number

            return self.async_create_entry(
                title=user_input.get(CONF_NAME, user_input[CONF_HOST]),
                data=user_input,
            )

        data_schema = vol.Schema(
            {
                vol.Optional(CONF_NAME): str,
                vol.Required(CONF_HOST): str,
                vol.Optional(CONF_PORT, default=DEFAULT_PORT): int,
                vol.Optional(CONF_DEVICE_ID, default=DEFAULT_DEVICE_ID): vol.All(
                    int, vol.Range(min=1, max=247)
                ),
                vol.Optional(CONF_BASE_ADDR, default=DEFAULT_BASE_ADDR): vol.In(
                    [0, 40000]
                ),
                vol.Optional(
                    CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL
                ): vol.All(
                    int, vol.Range(min=MIN_SCAN_INTERVAL, max=MAX_SCAN_INTERVAL)
                ),
            }
        )

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> config_entries.OptionsFlow:
        """Get the options flow for this handler."""
        return ABBFimerPVISunSpecOptionsFlow(config_entry)


class ABBFimerPVISunSpecOptionsFlow(config_entries.OptionsFlow):
    """Handle options flow for ABB FIMER PVI SunSpec."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.FlowResult:
        """Manage the options."""
        if user_input is not None:
            # Update config entry data
            self.hass.config_entries.async_update_entry(
                self.config_entry, data={**self.config_entry.data, **user_input}
            )
            return self.async_create_entry(title="", data={})

        current_config = self.config_entry.data

        data_schema = vol.Schema(
            {
                vol.Optional(
                    CONF_PORT, default=current_config.get(CONF_PORT, DEFAULT_PORT)
                ): int,
                vol.Optional(
                    CONF_DEVICE_ID,
                    default=current_config.get(CONF_DEVICE_ID, DEFAULT_DEVICE_ID),
                ): vol.All(int, vol.Range(min=1, max=247)),
                vol.Optional(
                    CONF_BASE_ADDR,
                    default=current_config.get(CONF_BASE_ADDR, DEFAULT_BASE_ADDR),
                ): vol.In([0, 40000]),
                vol.Optional(
                    CONF_SCAN_INTERVAL,
                    default=current_config.get(
                        CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL
                    ),
                ): vol.All(
                    int, vol.Range(min=MIN_SCAN_INTERVAL, max=MAX_SCAN_INTERVAL)
                ),
            }
        )

        return self.async_show_form(step_id="init", data_schema=data_schema)
