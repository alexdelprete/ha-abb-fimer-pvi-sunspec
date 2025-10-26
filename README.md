# ABB/FIMER PVI SunSpec (Modbus/TCP)

⚠️ **BETA RELEASE v1.0.0-beta.1**

[![GitHub Release][releases-shield]][releases]
[![HACS][hacs-shield]][hacs]

## Overview

Home Assistant custom integration for ABB/FIMER PVI inverters via **direct Modbus/TCP** communication.

**Key Features:**
- ✅ Dynamic SunSpec model discovery
- ✅ Support for M1, M101, M103, M120, M160, M124, M802-804, M201-204, M64061
- ✅ Multi-device support (inverter, meter, storage, MPPT)
- ✅ Async implementation based on ModbusLink
- ✅ Single-phase (M101) and three-phase (M103) inverters
- ⚠️ BETA - needs real-world testing

## ⚠️ Beta Status

This is a **BETA release**. While the integration has been thoroughly designed, it requires testing across various:
- Inverter models (single-phase, three-phase)
- MPPT configurations
- Battery/storage systems
- Meter integration

**How to help:**
1. Install and test
2. Report issues at [GitHub Issues](https://github.com/alexdelprete/ha-abb-fimer-pvi-sunspec/issues)
3. Share your configuration details
4. Monitor logs for errors

## Installation

### Via HACS (Recommended)

1. Open HACS in Home Assistant
2. Go to "Integrations"
3. Click "Explore & Download Repositories"
4. Search for "ABB FIMER PVI SunSpec"
5. Click "Download"
6. Restart Home Assistant
7. Go to Settings > Devices & Services > Add Integration
8. Search for "ABB FIMER PVI SunSpec"

### Manual Installation

1. Download the latest release from [GitHub Releases](https://github.com/alexdelprete/ha-abb-fimer-pvi-sunspec/releases)
2. Extract to `custom_components/abb_fimer_pvi_sunspec`
3. Restart Home Assistant
4. Add integration via UI

## Configuration

Configure via the Home Assistant UI:

- **Host**: IP address or hostname of the inverter
- **Port**: Modbus TCP port (default: 502)
- **Device ID**: Modbus unit ID (default: 2, range: 1-247)
- **Base Address**: SunSpec base address (0 or 40000)
- **Scan Interval**: Polling frequency in seconds (default: 60, range: 30-600)

## Supported Models

**Core Models:**
- **M1** - Common (manufacturer, model, serial number)
- **M101** - Single-phase inverter
- **M103** - Three-phase inverter
- **M120** - Nameplate ratings
- **M160** - MPPT (up to 4 channels)

**Storage Models:**
- **M124** - Storage control
- **M802** - Battery base model
- **M803** - Lithium-ion battery
- **M804** - Flow battery

**Meter Models:**
- **M201** - Single-phase meter
- **M203** - Three-phase meter (WYE)
- **M204** - Three-phase meter (Delta)

**Vendor Models:**
- **M64061** - ABB vendor-specific (diagnostics, isolation, periodic energy counters)

## Entity Naming

Entities are created with SunSpec-based naming:

- `inverter_<serial>_W` - AC Power
- `inverter_<serial>_A` - AC Current
- `inverter_<serial>_Hz` - Frequency
- `inverter_<serial>_WH` - Lifetime Energy
- `mppt_<serial>_DCA_1` - MPPT 1 Current
- `battery_<serial>_SoC` - Battery State of Charge
- `meter_<serial>_TotWhImp` - Total Energy Imported

## Known Limitations

- Beta release - limited production testing
- M64061 vendor model availability varies by inverter firmware
- Performance tuning may be needed for large installations

## Troubleshooting

Enable debug logging in `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.abb_fimer_pvi_sunspec: debug
```

## Support

- [GitHub Issues](https://github.com/alexdelprete/ha-abb-fimer-pvi-sunspec/issues)
- [Home Assistant Community Forum](https://community.home-assistant.io/)

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Follow the code style (.ruff.toml)
4. Add tests if applicable
5. Submit a pull request

## Credits

- Original SolarEdge integration by @binsentsu
- Adapted for ABB/Power-One/FIMER by @alexdelprete
- Built with ModbusLink library
- SunSpec models courtesy of SunSpec Alliance (Apache-2.0)

## License

MIT License - see [LICENSE](LICENSE)

---

_This project is not endorsed by, directly affiliated with, maintained, authorized, or sponsored by ABB or FIMER_

[releases-shield]: https://img.shields.io/github/v/release/alexdelprete/ha-abb-fimer-pvi-sunspec
[releases]: https://github.com/alexdelprete/ha-abb-fimer-pvi-sunspec/releases
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-orange.svg
[hacs]: https://github.com/custom-components/hacs
