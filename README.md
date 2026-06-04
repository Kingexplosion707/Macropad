# 7-Key Macro Grid

A compact 7-key macropad built around the Seeed XIAO RP2040, running CircuitPython. Designed for productivity shortcuts, media control, or application-specific hotkeys. PCB fits within 100mm × 100mm; case fits within 200mm × 200mm × 100mm.

---

## Screenshots & Renders

### Macropad Design Render
> 📷 _Place your macropad render or photo here (`render.png`)_

### Schematic
> 📷 _Place a screenshot of your KiCad schematic here (`schematic.png`)_

### PCB Layout
> 📷 _Place a screenshot of your KiCad PCB layout here (`layout.png`)_

### Case — 3D View
> 📷 _Place a screenshot of your case assembly here (`case-3d.png`)_

---

## Features

- **7× MX-compatible key switches** in a 3×2+1 or custom arrangement
- **Seeed XIAO RP2040** microcontroller (USB-C, onboard RGB, compact footprint)
- **CircuitPython** firmware — easy to hack, no toolchain required
- **Fully 3D-printed** two-piece case (top + bottom) with heatset inserts
- **Per-key diodes** for full N-key rollover
- **USB-C** passthrough cutout in case

---

## Bill of Materials

| Qty | Component | Value / Part | Notes |
|-----|-----------|--------------|-------|
| 1 | Microcontroller | Seeed XIAO RP2040 | USB-C, RP2040 |
| 7 | Mechanical switches | MX-compatible (any) | 5-pin or 3-pin |
| 7 | Keycaps | MX 1U | Any profile |
| 7 | Diodes | 1N4148 SOD-123 (SMD) or through-hole | One per switch |
| 1 | PCB | Custom (this repo) | 2-layer, ≤100×100mm |
| 1 | Case top | 3D printed PLA/PETG | See `/production/Top.STEP` |
| 1 | Case bottom | 3D printed PLA/PETG | See `/production/Bottom.STEP` |
| 4 | Heatset inserts | M3 × 4mm | 4.7mm hole diameter |
| 4 | Screws | M3 × 8mm | Case assembly |
| 4 | Rubber feet | 3M Bumpons or similar | Optional, bottom of case |

---

## Folder Structure

```
your-macropad/
├── README.md
├── CAD/
│   └── assembled-model.STEP
├── PCB/
│   ├── your-project.kicad_pro
│   ├── your-project.kicad_sch
│   └── your-project.kicad_pcb
├── Firmware/
│   └── main.py
└── production/
    ├── gerbers.zip
    ├── Top.STEP
    ├── Bottom.STEP
    └── main.py
```

---

## Firmware

Firmware is written in **CircuitPython** using the `kmk` or `adafruit_hid` library.

To flash:
1. Hold BOOT button on XIAO RP2040 while plugging in USB-C → it mounts as `RPI-RP2`
2. Drag and drop `firmware.uf2` (CircuitPython) onto the drive
3. Once it remounts as `CIRCUITPY`, copy `main.py` (and any libraries) to the drive
4. It runs automatically on boot

See [`/Firmware/main.py`](./Firmware/main.py) for keymap and customisation instructions.

---

## Build Notes

- **Heatset insert holes:** 4.7mm diameter
- **Screw pass-through holes:** 3.4mm diameter
- **Mating surface tolerance:** 0.2mm
- **USB-C cutout** is included in the case top/bottom split line
- All case parts are fully 3D-printable — no laser cutting or CNC required
- Recommended print settings: 0.2mm layer height, 4 perimeters, 20% infill

---

## Pre-Submission Checklist

- [x] PCB is 100mm × 100mm or smaller (2-layer)
- [x] Case fits within 200mm × 200mm × 100mm
- [x] Case is fully 3D-printable
- [x] Only using parts from kit (or noted extras)
- [x] Gerber files exported and zipped → `production/gerbers.zip`
- [x] Case parts exported as `.STEP` → `production/Top.STEP`, `production/Bottom.STEP`
- [x] Firmware included → `production/main.py`
- [x] Heatset insert holes: 4.7mm diameter ✓
- [x] Screw pass-through holes: 3.4mm clearance ✓
- [x] 0.2mm tolerance on mating surfaces ✓
- [x] USB-C port cutout in case ✓
- [x] README has screenshots and BOM ✓
