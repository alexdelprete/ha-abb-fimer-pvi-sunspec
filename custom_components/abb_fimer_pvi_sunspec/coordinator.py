"""DataUpdateCoordinator for SunSpec."""
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL, DOMAIN

class ABBFimerPVISunSpecCoordinator(DataUpdateCoordinator):
    """Coordinator for SunSpec data."""

    def __init__(self, hass, config_entry, client):
        scan_interval = config_entry.data.get(
            CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL
        )
        super().__init__(
            hass, None, name=DOMAIN,
            update_interval=timedelta(seconds=scan_interval)
        )
        self.client = client
        self.config_entry = config_entry

    async def _async_update_data(self):
        """Fetch data from SunSpec client."""
        try:
            return await self.client.read_all()
        except Exception as err:
            raise UpdateFailed(f"Error: {err}") from err
