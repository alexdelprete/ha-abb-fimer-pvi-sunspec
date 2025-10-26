# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0-beta.1] - 2025-10-26

### Added
- Initial beta release
- Async SunSpec Modbus/TCP client based on ModbusLink
- Dynamic model discovery and parsing
- Support for M1, M101, M103, M120, M160, M124, M802-804, M201-204, M64061
- Multi-device support (inverter, meter, storage, MPPT)
- Scale factor handling and data type conversions
- Repeating group support (MPPT channels)
- Invalid sentinel detection (0x8000, 0x7FFF)
- Component tree with stable device IDs
- Config flow with validation
- Options flow for runtime reconfiguration
- Comprehensive error handling and logging

### Known Limitations
- Beta release - limited user testing
- Needs validation across different inverter models
- Performance tuning may be needed
- M64061 vendor model availability varies by firmware

### Testing Needed
- Single-phase inverters (M101)
- Three-phase inverters (M103)
- MPPT configurations (1-4 channels)
- Battery/storage systems (M802, M124)
- Meter integration (M201, M203, M204)
- Different base addresses (0 vs 40000)
- Various device_id configurations

[Unreleased]: https://github.com/alexdelprete/ha-abb-fimer-pvi-sunspec/compare/v1.0.0-beta.1...HEAD
[1.0.0-beta.1]: https://github.com/alexdelprete/ha-abb-fimer-pvi-sunspec/releases/tag/v1.0.0-beta.1
