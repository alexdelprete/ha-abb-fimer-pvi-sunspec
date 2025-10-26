"""Constants for ABB FIMER PVI SunSpec integration."""

DOMAIN = "abb_fimer_pvi_sunspec"
VERSION = "1.0.0-beta.1"

# Configuration
CONF_HOST = "host"
CONF_PORT = "port"
CONF_DEVICE_ID = "device_id"
CONF_BASE_ADDR = "base_addr"
CONF_SCAN_INTERVAL = "scan_interval"

DEFAULT_PORT = 502
DEFAULT_DEVICE_ID = 2
DEFAULT_BASE_ADDR = 0
DEFAULT_SCAN_INTERVAL = 60
MIN_SCAN_INTERVAL = 30
MAX_SCAN_INTERVAL = 600

# SunSpec
SUNSPEC_REGISTER_END = 0xFFFF

# Core SunSpec Models
MODEL_COMMON = 1
MODEL_INVERTER_SINGLE_PHASE = 101
MODEL_INVERTER_THREE_PHASE = 103
MODEL_NAMEPLATE = 120
MODEL_STORAGE = 124
MODEL_MPPT = 160
MODEL_METER_SINGLE_PHASE = 201
MODEL_METER_THREE_PHASE_WYE = 203
MODEL_METER_THREE_PHASE_DELTA = 204
MODEL_BATTERY = 802
MODEL_LITHIUM_ION = 803
MODEL_FLOW_BATTERY = 804
MODEL_ABB_VENDOR = 64061

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
ABB/FIMER PVI SunSpec (Modbus)
Version: 1.0.0-beta.1
This is a custom integration for Home Assistant
If you have any issues, please report them at:
https://github.com/alexdelprete/ha-abb-fimer-pvi-sunspec/issues
-------------------------------------------------------------------
"""
