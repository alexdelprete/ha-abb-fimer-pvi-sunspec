# Claude Code Development Guidelines - ABB/FIMER PVI SunSpec (Modbus)

## Project Overview

This repository provides a Home Assistant custom integration for ABB/FIMER PVI inverters via **direct Modbus/TCP** communication using SunSpec protocol.

**Version:** 1.0.0-beta.1 (BETA)

**Key Technologies:**
- ModbusLink - Async Modbus client library
- SunSpec protocol - Industry-standard solar inverter communication
- Vendored JSON models from github.com/sunspec/models (Apache-2.0)

## Architecture Overview

### async-sunspec-client (Embedded Library)

The integration includes an embedded async SunSpec client library:

**discovery.py** - Model Discovery
- Scan for "SunS" magic number at base addresses (0 or 40000)
- Read M1 (Common) model header
- Follow model chain until 0xFFFF sentinel
- Return list of discovered (model_id, offset) tuples

**models.py** - Model Definitions
- Load JSON model definitions from vendor/sunspec_models/json/
- Parse register layouts, data types, scale factors
- Handle repeating groups (e.g., MPPT channels)
- Provide structured model metadata

**parser.py** - Data Parser
- Read raw Modbus registers via ModbusLink
- Apply scale factors for unit conversion
- Detect and handle invalid sentinels (0x8000, 0x7FFF, NaN markers)
- Parse repeating groups dynamically
- Build component tree with stable device IDs

**exceptions.py** - Custom Exceptions
- SunSpecConnectionError - Modbus communication failures
- SunSpecDiscoveryError - Model discovery failures
- SunSpecModelError - Model loading/parsing errors
- SunSpecParseError - Data parsing errors

### Home Assistant Integration

**__init__.py**
- async_setup_entry(): Initialize ModbusLink client + SunSpec discovery + coordinator
- async_unload_entry(): Clean shutdown and resource cleanup
- Uses config_entry.runtime_data to store coordinator

**coordinator.py**
- ABBFimerPVISunSpecCoordinator extends DataUpdateCoordinator
- Polls discovered models at configured interval
- Handles connection errors and retries
- Provides parsed data to sensor platform

**config_flow.py**
- ConfigFlow: Initial setup with host, port, device_id, base_addr, scan_interval
- OptionsFlow: Runtime reconfiguration without restart
- Validation: Test connection and discover models during setup

**sensor.py**
- Dynamic sensor creation from discovered models
- Entity unique_id: `{device_type}_{serial}_{sunspec_point}`
- State class logic:
  - `total_increasing`: Lifetime energy counters (WH, TotWhImp, etc.)
  - `total`: Periodic counters (DayWH, WeekWH, MonthWH, YearWH from M64061)
  - `measurement`: Instantaneous values (W, A, V, Hz, SoC, etc.)

## SunSpec Models

### Core Models
- **M1** - Common (manufacturer, model, serial, version)
- **M101** - Single-phase inverter
- **M103** - Three-phase inverter
- **M120** - Nameplate ratings
- **M124** - Storage control
- **M160** - MPPT (up to 4 channels with repeating groups)

### Storage Models
- **M802** - Battery base model
- **M803** - Lithium-ion battery
- **M804** - Flow battery

### Meter Models
- **M201** - Single-phase meter
- **M203** - Three-phase meter (WYE)
- **M204** - Three-phase meter (Delta)

### Vendor Models
- **M64061** - ABB vendor-specific (diagnostics, isolation, periodic energy counters)

## Development Patterns

### Error Handling
- Use custom exceptions from async_sunspec_client.exceptions
- Log errors with context using helpers.py functions
- Graceful degradation: if one model fails, continue with others

### Logging
- Use helpers from helpers.py:
  - log_debug(logger, context, message, **kwargs)
  - log_info(logger, context, message, **kwargs)
  - log_warning(logger, context, message, **kwargs)
  - log_error(logger, context, message, **kwargs)
- Never use f-strings in logger calls
- Always include context parameter

### Async/Await
- All I/O must be async
- ModbusLink is async-only
- Coordinator runs in async context

### Data Storage
- Use config_entry.runtime_data with typed RuntimeData dataclass
- Never use hass.data[DOMAIN]

## Code Quality Standards

### Ruff Configuration
- Follow .ruff.toml strictly
- Key rules: A001, TRY300, TRY301, G004, SIM222, PIE796
- Run `ruff check .` before committing

### Type Hints
- Add type hints to all functions and class methods
- Use modern type syntax (e.g., `list[str]` not `List[str]`)
- Type alias: `type ABBFimerPVISunSpecConfigEntry = ConfigEntry[RuntimeData]`

### Testing
- Unit tests for parser, discovery, model loading
- Integration tests for actual Modbus communication
- Test with different inverter models and configurations

## Vendor SunSpec Models

**Source:** https://github.com/sunspec/models (Apache-2.0)

**Location:** vendor/sunspec_models/json/

**Files Required:**
- model_1.json (Common)
- model_101.json, model_103.json (Inverters)
- model_120.json (Nameplate)
- model_124.json (Storage)
- model_160.json (MPPT)
- model_201.json, model_203.json, model_204.json (Meters)
- model_802.json, model_803.json, model_804.json (Battery)
- model_64061.json (ABB vendor - if available)

**Attribution:**
- NOTICE file with Apache-2.0 license text
- NAMESPACE file with upstream URL, ref, timestamp

## Git Workflow

### Commit Messages
- Use conventional commits (feat:, fix:, docs:, etc.)
- Include Claude attribution block:
  ```
  🤖 Generated with [Claude Code](https://claude.com/claude-code)

  Co-Authored-By: Claude <noreply@anthropic.com>
  ```

### Branch Strategy
- Main branch: master
- Feature branches: feature/xxx
- Beta releases tagged as v1.0.0-beta.1, v1.0.0-beta.2, etc.

### Releases
- Tag beta releases with `--prerelease` flag
- Use docs/releases/vX.Y.Z.md for detailed notes
- Update CHANGELOG.md summary

## Beta Testing Checklist

- [ ] Single-phase inverters (M101)
- [ ] Three-phase inverters (M103)
- [ ] MPPT configurations (1-4 channels)
- [ ] Battery/storage systems (M802, M124)
- [ ] Meter integration (M201, M203, M204)
- [ ] M64061 vendor model points
- [ ] Different base addresses (0 vs 40000)
- [ ] Various device_id configurations (1-247)
- [ ] Long-term stability (24+ hours)
- [ ] Error recovery (network interruptions)

## Key Files to Review

- .ruff.toml - Linting configuration
- const.py - Constants and defaults
- helpers.py - Logging helpers
- async_sunspec_client/ - Client library implementation
- docs/pysunspec2-analysis.md - Decision record (copied from old repo)

## Don't Do

- Do not use hass.data[DOMAIN]; use runtime_data
- Do not shadow builtins
- Do not use f-strings in logging
- Do not forget to await async methods
- Do not mix sync/async patterns
- Do not hardcode model IDs - use dynamic discovery
