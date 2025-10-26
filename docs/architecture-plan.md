# Architecture Plan - ABB/FIMER PVI SunSpec (Modbus)

## Executive Summary

This integration provides direct Modbus/TCP communication with ABB/FIMER PVI inverters using the industry-standard SunSpec protocol. Dynamic model discovery ensures support for various inverter configurations without hardcoding.

## Goals

1. **Dynamic Discovery**: Scan and detect all SunSpec models present
2. **Multi-Device Support**: Handle inverter + meter + storage + MPPT
3. **Stable Device IDs**: Synthesize deterministic IDs when needed
4. **Robust Parsing**: Handle scale factors, repeating groups, invalid sentinels
5. **HA Best Practices**: Config flow, coordinator pattern, proper entity types

## Component Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              Home Assistant Integration                     │
├─────────────────────────────────────────────────────────────┤
│  config_flow.py │ coordinator.py │ sensor.py │ __init__.py │
└────────────┬────────────────────────────────────────────────┘
             │
             ├──> async_sunspec_client/
             │    ├── discovery.py   (Model scanning)
             │    ├── models.py      (JSON model loader)
             │    ├── parser.py      (Data parsing & scaling)
             │    └── exceptions.py  (Custom errors)
             │
             └──> ModbusLink (async Modbus client)
                  └──> Inverter (Modbus/TCP)
```

## Discovery Algorithm

```python
async def discover():
    1. Scan for "SunS" (0x53756e53) at base_addr (0 or 40000)
    2. If found, read M1 (Common) model:
       - Manufacturer, Model, Serial, Version
       - Model length (L bytes)
    3. Set offset = base_addr + 2 + L
    4. Loop:
       a. Read model_id at offset
       b. If model_id == 0xFFFF: break (end of chain)
       c. Read model_length at offset + 1
       d. Store (model_id, offset)
       e. offset += 2 + model_length
    5. Return discovered_models list
```

## Model Loading

```python
def load_model(model_id: int):
    1. Load vendor/sunspec_models/json/model_{model_id}.json
    2. Parse:
       - Registers (address, type, units, scale factor)
       - Repeating groups (MPPT channels, batteries)
       - Invalid sentinels (0x8000 for int16, NaN for others)
    3. Build lookup tables for parsing
    4. Return structured model definition
```

## Data Parsing

```python
def parse(model_def, raw_registers):
    1. For each register in model_def:
       a. Extract value from raw_registers[offset]
       b. Check if value == invalid_sentinel
       c. If not invalid:
          - Apply scale factor if present
          - Convert to appropriate type
          - Store in points dict
    2. For repeating groups:
       a. Read count register
       b. Loop count times:
          - Parse group registers
          - Store with index (_1, _2, etc.)
    3. Return points dict
```

## Entity Creation

```python
# Unique ID format
entity_id = f"{device_type}_{serial}_{sunspec_point}"

# Examples:
"inverter_077909_W"          # AC Power
"inverter_077909_WH"         # Lifetime Energy
"mppt_077909_DCA_1"          # MPPT 1 DC Current
"battery_123456_SoC"         # Battery State of Charge
"meter_789012_TotWhImp"      # Meter Total Import Energy
```

## State Class Logic

```python
# total_increasing: Lifetime counters
"WH", "TotWhImp", "TotWhExp", "ECharge", "EDischarge"

# total: Periodic counters (reset after period)
"DayWH", "WeekWH", "MonthWH", "YearWH"

# measurement: Instantaneous values
"W", "A", "V", "Hz", "SoC", "SoH", "Tmp"
```

## Error Handling

1. **Connection Errors**: Retry with exponential backoff
2. **Discovery Failures**: Log and fail setup (can't proceed without models)
3. **Model Load Errors**: Skip that model, continue with others
4. **Parse Errors**: Log warning, mark point as unavailable
5. **Invalid Sentinels**: Detect and skip (don't create entity with bad data)

## Testing Strategy

### Unit Tests
- discovery.py: Model scanning logic
- models.py: JSON parsing
- parser.py: Scale factor application, sentinel detection, repeating groups

### Integration Tests
- Full discovery + parse cycle with mock Modbus data
- Different inverter types (M101 vs M103)
- MPPT variations (1-4 channels)
- Battery + meter combinations

### Real-World Testing
- Beta user feedback across different hardware
- Long-term stability testing
- Network interruption recovery

## Performance Targets

- Discovery: < 5 seconds
- Polling cycle: < 2 seconds for typical setup
- Memory: < 50MB for large multi-device install

## Milestones

**Phase 1: Core Implementation**
- [x] Project structure
- [ ] async_sunspec_client library
- [ ] Basic config flow
- [ ] Simple coordinator
- [ ] Test with M1 + M103 only

**Phase 2: Full Model Support**
- [ ] M101, M120, M160 support
- [ ] Repeating groups (MPPT)
- [ ] Scale factors and sentinels
- [ ] Dynamic sensor creation

**Phase 3: Storage & Meters**
- [ ] M124, M802-804 (batteries)
- [ ] M201, M203, M204 (meters)
- [ ] Multi-device topology
- [ ] Device ID synthesis

**Phase 4: Vendor Models**
- [ ] M64061 (ABB vendor)
- [ ] Periodic energy counters
- [ ] Diagnostics and isolation

**Phase 5: Polish & Release**
- [ ] Documentation
- [ ] Beta testing
- [ ] Bug fixes
- [ ] v1.0.0 stable release
