![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%20Pico-red.svg)
![Language](https://img.shields.io/badge/Language-MicroPython-yellow.svg)

# SMART DESKTOP STATION — Sentinel-Pico

<table>
  <tr>
    <td width="60%">
      <img width="100%" alt="Full circuit on Wokwi" src="https://github.com/user-attachments/assets/9fdb7b7b-884d-43d9-91e0-78f3baa4d8ae" />
    </td>
    <td>
      <p>
        An intelligent desk environment monitor built on the <strong>Raspberry Pi Pico</strong> and written in <strong>MicroPython</strong>.
        Sentinel-Pico uses a proximity sensor to detect whether someone is sitting at the desk, then reads
        temperature, humidity, and ambient light to display contextual information on a small OLED screen.
        Try it online — no hardware required — on <a href="https://wokwi.com/projects/462996062362677249">Wokwi</a>.
      </p>
    </td>
  </tr>
</table>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Hardware / Components](#hardware--components)
- [Wiring / Pinout](#wiring--pinout)
- [Logic Flow](#logic-flow)
- [Repository Structure](#repository-structure)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Simulated Screens](#simulated-screens)
- [Troubleshooting](#troubleshooting)
- [Roadmap / Cool Ideas](#roadmap--cool-ideas)
- [License](#license)
- [Contributing](#contributing)

---

## Overview

Sentinel-Pico turns any desk into a smart monitoring station. When no one is detected within 50 cm, the OLED
display enters a low-power idle screen. When someone sits down, it immediately reports ambient conditions and
alerts the user if the lighting is too dim for comfortable work.

---

## Features

- **Presence detection** via HC-SR04 ultrasonic sensor
- **Temperature & humidity** readout from a DHT22 sensor
- **Ambient light** monitoring with a photoresistor (LDR)
- **OLED display** driven by an SSD1306 over I2C
- **Three distinct display modes** based on real-time sensor data
- Fully simulated on **Wokwi** — no physical hardware needed to try it

---

## Hardware / Components

| Component | Model | Pin(s) |
|---|---|---|
| Microcontroller | Raspberry Pi Pico (MicroPython) | — |
| OLED Display | SSD1306 128×64 (I2C) | GP4 (SDA), GP5 (SCL) |
| Temperature & Humidity Sensor | DHT22 | GP14 |
| Light Sensor | Photoresistor (LDR) | GP26 (ADC0) |
| Ultrasonic Sensor | HC-SR04 | GP28 (TRIG), GP27 (ECHO) |

---

## Wiring / Pinout

```
SSD1306 OLED  →  SDA: GP4, SCL: GP5, VCC: 3.3 V, GND
DHT22         →  DATA: GP14, VCC: 3.3 V, GND
LDR Sensor    →  OUT: GP26 (ADC0), VCC: 3.3 V, GND
HC-SR04       →  TRIG: GP28, ECHO: GP27, VCC: 5 V (VBUS), GND
```

---

## Logic Flow

```
Loop:
 ├── Measure distance (HC-SR04)
 │
 ├── Distance > 50 cm  OR  sensor error
 │    └── OLED: "Nobody Detected / Shutdown"
 │
 └── Distance ≤ 50 cm (someone at desk)
      ├── Read DHT22 (temperature + humidity)
      ├── Read LDR (ambient light level)
      │
      ├── LDR ADC value ≥ 32727  (≤ ~100 lux — too dark)
      │    └── OLED: "Please turn on the light!"
      │
      └── LDR ADC value < 32727  (bright enough)
           └── OLED: "Hi Sir! / Humidity: X% / Temp: X °C"
                └── Wait 5 s, then repeat
```

---

## Repository Structure

```
DE/
├── deskstation.py     # Main application logic (MicroPython)
├── journal.md         # Dev log / Hack Club Lapse links
└── README.md
```

> **Note:** `ssd1306.py` (the OLED driver) must be placed on the Pico alongside `deskstation.py`.
> You can download it from the [MicroPython SSD1306 driver](https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/display/ssd1306/ssd1306.py).

---

## Quick Start

### Simulate online (no hardware required)

Open the project directly on Wokwi:
[https://wokwi.com/projects/462996062362677249](https://wokwi.com/projects/462996062362677249)

### Run on real hardware

1. Flash **MicroPython v1.24.1** (or later) on your Raspberry Pi Pico.
2. Download `ssd1306.py` from the MicroPython library (link above).
3. Copy `deskstation.py` and `ssd1306.py` to the Pico using **Thonny** or **mpremote**:
   ```bash
   mpremote cp deskstation.py :main.py
   mpremote cp ssd1306.py :ssd1306.py
   ```
4. Wire the components according to the [Wiring / Pinout](#wiring--pinout) section.
5. Power up — the program starts automatically on boot.

---

## Configuration

All tunable values are located at the top of [`deskstation.py`](deskstation.py):

| Variable | Default | Description |
|---|---|---|
| Distance threshold | `50` cm | Maximum distance to consider someone present |
| LDR threshold | `32727` | ADC value above which the light is considered insufficient |
| Refresh interval | `5` s | Delay between sensor readings when someone is detected |

---

## Simulated Screens

**Full circuit on Wokwi**

<img width="575" alt="Full circuit" src="https://github.com/user-attachments/assets/9fdb7b7b-884d-43d9-91e0-78f3baa4d8ae" />

**No one detected** (distance > 50 cm)

<img width="348" alt="Nobody detected" src="https://github.com/user-attachments/assets/0beb32c5-5ed1-4b3d-bb53-6972d76d873e" />

**Too dark** (ambient light < 100 lux)

<img width="400" alt="Too dark warning" src="https://github.com/user-attachments/assets/853ad87c-a130-4f1b-a94d-df331c37ac9e" />

**Normal operation** — temperature & humidity displayed

<img width="353" alt="Normal display" src="https://github.com/user-attachments/assets/35e305e7-6ced-4507-97e7-5a496150a23f" />

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| OLED stays blank | Wrong I2C pins or missing `ssd1306.py` | Check GP4/GP5 wiring; ensure driver file is on Pico |
| Distance always returns -1 | Echo pin not connected or timeout | Verify HC-SR04 wiring (5 V on VCC) and GP27/GP28 |
| DHT22 read error | Sensor not stabilised | Add a 2-second warm-up delay before the first read |
| LDR value always 0 | ADC pin floating | Ensure voltage-divider resistor is connected to GND |

---

## Roadmap / Cool Ideas

This project can still be improved a lot. Here are some ideas for future features:

- **Wi-Fi dashboard** — push sensor data to a web page using the Pico W
- **BLE notifications** — send a phone alert when lighting is too dim
- **CO2 / air-quality sensor** — add an MH-Z19 or SGP30 for air quality monitoring
- **Configurable thresholds** — read distance/light thresholds from a `config.json` on the filesystem
- **Sleep / wake animation** — add a small animation when someone sits down
- **Data logging** — write sensor readings to a CSV file on an SD card
- **Multi-user greeting** — detect different users by RFID card

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions, improvements, and remixes are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) guide to get started.
