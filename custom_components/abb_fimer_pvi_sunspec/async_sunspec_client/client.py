"""Main SunSpec client implementation."""
import logging
from .discovery import discover_models
from .models import load_model_definition
from .parser import SunSpecParser
from .exceptions import SunSpecConnectionError

_LOGGER = logging.getLogger(__name__)

class AsyncSunSpecClient:
    """Async SunSpec Modbus client."""

    def __init__(self, modbus_client, base_addr: int = 0, device_id: int = 2):
        self.modbus_client = modbus_client
        self.base_addr = base_addr
        self.device_id = device_id
        self.discovered_models = []
        self.parsers = {}

    async def connect(self):
        """Connect and discover models."""
        self.discovered_models = await discover_models(
            self.modbus_client, self.base_addr, self.device_id
        )
        for model_id, offset in self.discovered_models:
            try:
                model_def = load_model_definition(model_id)
                self.parsers[model_id] = SunSpecParser(model_def)
            except Exception as err:
                _LOGGER.warning("Failed to load model %d: %s", model_id, err)

    async def read_all(self):
        """Read all discovered models."""
        # TODO: Implement Modbus reading
        return {}
