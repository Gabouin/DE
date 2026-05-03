
Full circuit on [wowki](https://wokwi.com/projects/462996062362677249)
<img width="575" height="450" alt="Capture d&#39;écran 2026-05-03 163614" src="https://github.com/user-attachments/assets/9fdb7b7b-884d-43d9-91e0-78f3baa4d8ae" />

when nobody is detected near the sensor ( >50cm )
<img width="348" height="278" alt="Capture d&#39;écran 2026-05-03 163710" src="https://github.com/user-attachments/assets/0beb32c5-5ed1-4b3d-bb53-6972d76d873e" />

when brightness is too low ( < 100 lux )
<img width="400" height="327" alt="Capture d&#39;écran 2026-05-03 163648" src="https://github.com/user-attachments/assets/853ad87c-a130-4f1b-a94d-df331c37ac9e" />

when someone is detected and brightness correct, it displays humidity and temperature
<img width="353" height="290" alt="Capture d&#39;écran 2026-05-03 163628" src="https://github.com/user-attachments/assets/35e305e7-6ced-4507-97e7-5a496150a23f" />


# 🖥️ Smart Desk Monitor

A MicroPython project simulating an intelligent desk environment monitor, built on **Raspberry Pi Pico** and running on [Wokwi](https://wokwi.com/projects/462996062362677249).

---

## 📋 Overview

This project turns your desk into a smart station. Using a **proximity sensor**, it detects whether someone is sitting at the desk, then reads **temperature**, **humidity**, and **ambient light** to display contextual information on a small OLED screen.

- No one nearby → display shows "Nobody Detected / Shutdown"
- Someone detected + bright enough → display shows temperature & humidity
- Someone detected + too dark → display warns the user to turn on the light

---

## 🧰 Hardware Components

| Component | Model | Pin(s) |
|---|---|---|
| Microcontroller | Raspberry Pi Pico (MicroPython) | — |
| OLED Display | SSD1306 128×64 (I2C) | GP4 (SDA), GP5 (SCL) |
| Temp & Humidity Sensor | DHT22 | GP14 |
| Light Sensor | Photoresistor (LDR) | GP26 (ADC) |
| Ultrasonic Sensor | HC-SR04 | GP28 (TRIG), GP27 (ECHO) |

---

## 🔌 Wiring Summary

```
SSD1306 OLED  →  I2C: GP4/GP5, 3.3V, GND
DHT22         →  GP14, 3.3V, GND
LDR Sensor    →  GP26 (analog), 3.3V, GND
HC-SR04       →  TRIG: GP28, ECHO: GP27, VBUS (5V), GND
```

---

## 🧠 Logic Flow

```
Loop:
 ├── Measure distance (HC-SR04)
 │
 ├── Distance > 50 cm or error
 │    └── OLED: "Nobody Detected / Shutdowned"
 │
 └── Distance ≤ 50 cm (someone at desk)
      ├── Read DHT22 (temp + humidity)
      ├── Read LDR (ambient light)
      │
      ├── LDR value ≥ 32727 (≤ ~100 lux → too dark)
      │    └── OLED: "Please turn on the light!"
      │
      └── LDR value < 32727 (bright enough)
           └── OLED: "Hi Sir! / Humidity: X% / Temp: X°C"
                └── Wait 5 seconds
```

---

## 📁 File Structure

```
desk/
├── main.py            # Main application logic
├── ssd1306.py         # SSD1306 OLED driver (MicroPython)
├── diagram.json       # Wokwi circuit diagram
└── wokwi-project.txt  # Wokwi project link
```

---

## 🚀 Getting Started

### Simulate online
Open the project directly on Wokwi:
👉 https://wokwi.com/projects/462996062362677249

### Run on real hardware
1. Flash **MicroPython v1.24.1** on your Raspberry Pi Pico
2. Copy `main.py` and `ssd1306.py` to the Pico using **Thonny** or **mpremote**
3. Wire the components according to the table above
4. Power up — the program runs automatically on boot

---

## ⚙️ Configuration

You can tweak these values in `main.py`:

| Variable | Default | Description |
|---|---|---|
| `50` (distance threshold) | 50 cm | Max distance to consider someone present |
| `32727` (LDR threshold) | ~32727 | ADC value below which light is considered sufficient |
| `time.sleep(5)` | 5 s | Refresh interval when displaying sensor data |

---

## 📦 Dependencies

- `dht` — built-in MicroPython DHT library
- `machine` — built-in MicroPython hardware library
- `ssd1306.py` — included in this repo (MicroPython OLED driver)

---

## 👤 Author

**Gabouin** — [Wokwi Profile](https://wokwi.com)
