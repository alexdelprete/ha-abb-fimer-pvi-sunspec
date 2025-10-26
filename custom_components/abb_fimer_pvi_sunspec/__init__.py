"""ABB FIMER PVI SunSpec Integration.

https://github.com/alexdelprete/ha-abb-fimer-pvi-sunspec
"""

import logging
from dataclasses import dataclass

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from .const import DOMAIN, STARTUP_MESSAGE

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]

type ABBFimerPVISunSpecConfigEntry = ConfigEntry[RuntimeData]


@dataclass
class RuntimeData:
    """Runtime data for the integration."""

    coordinator: object  # TODO: Add actual type when coordinator is implemented


async def async_setup_entry(
    hass: HomeAssistant, config_entry: ABBFimerPVISunSpecConfigEntry
) -> bool:
    """Set up ABB FIMER PVI SunSpec from a config entry."""
    _LOGGER.info(STARTUP_MESSAGE)

    # TODO: Initialize async-sunspec-client and coordinator
    # coordinator = ABBFimerPVISunSpecCoordinator(hass, config_entry)
    # await coordinator.async_config_entry_first_refresh()

    # config_entry.runtime_data = RuntimeData(coordinator=coordinator)
    # await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)

    raise ConfigEntryNotReady("TODO: Implement async_setup_entry")


async def async_unload_entry(
    hass: HomeAssistant, config_entry: ABBFimerPVISunSpecConfigEntry
) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(config_entry, PLATFORMS)
