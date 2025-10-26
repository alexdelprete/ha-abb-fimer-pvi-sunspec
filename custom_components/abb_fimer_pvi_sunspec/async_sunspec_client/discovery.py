"""SunSpec model discovery."""

import logging

_LOGGER = logging.getLogger(__name__)


async def discover_models(
    modbus_client, base_addr: int, device_id: int
) -> list[tuple[int, int]]:
    """Discover SunSpec models.

    Returns:
        List of (model_id, offset) tuples

    TODO:
    - Scan for "SunS" magic number at base_addr
    - Read M1 (Common) model
    - Follow model chain until 0xFFFF
    - Return list of discovered (model_id, offset) pairs
    """
    raise NotImplementedError("TODO: Implement model discovery")
