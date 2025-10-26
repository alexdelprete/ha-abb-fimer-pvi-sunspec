"""SunSpec model definitions and loader."""

import json
import logging
from pathlib import Path

_LOGGER = logging.getLogger(__name__)


def load_model_definition(model_id: int) -> dict:
    """Load SunSpec model definition from JSON.

    TODO:
    - Load from vendor/sunspec_models/json/model_{model_id}.json
    - Parse registers, scale factors, types
    - Handle repeating groups
    - Return structured model definition
    """
    raise NotImplementedError("TODO: Implement model loading")
