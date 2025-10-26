"""SunSpec data parser."""

import logging

_LOGGER = logging.getLogger(__name__)


class SunSpecParser:
    """Parse SunSpec model data."""

    def __init__(self, model_definition: dict):
        """Initialize parser with model definition."""
        self.model_definition = model_definition

    def parse(self, raw_registers: list[int]) -> dict:
        """Parse raw Modbus registers into structured data.

        TODO:
        - Apply scale factors
        - Handle invalid sentinels (0x8000, 0x7FFF, etc.)
        - Parse repeating groups
        - Convert data types
        - Return structured point data
        """
        raise NotImplementedError("TODO: Implement data parsing")
