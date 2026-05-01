# SMART DESKTOP STATION

### Professional Smart Desktop Monitoring & Security Station

**Sentinel-Pico** is a multi-modal monitoring system powered by the Raspberry Pi Pico. It leverages a suite of environmental and proximity sensors to create an interactive, context-aware desktop companion.

---

## 🚀 Overview
This project integrates environmental data logging, security alerts, and visual feedback into a single compact unit. Whether you need to monitor your room's climate or secure your workspace when you're away, Sentinel-Pico provides a robust, programmable solution.

## 🛠️ Components List
| Component | Function |
| :--- | :--- |
| **Raspberry Pi Pico** | Central Logic & Processing |
| **DHT22** | High-accuracy Temperature & Humidity sensing |
| **SSD1306 OLED** | 128x64 Dashboard for real-time telemetry |
| **MAX7219 LED Matrix** | 8x8 Visual notifications and status emojis |
| **HC-SR04** | Ultrasonic proximity/distance tracking |
| **LDR** | Ambient light detection for auto-dimming |
| **Buzzer** | Auditory alerts and UI feedback |
| **Buttons** | User interaction and mode switching |

## 🔌 Pin Mapping (Suggested)
The following GPIO configuration is optimized for MicroPython:

- **I2C (OLED):** `GP8` (SDA), `GP9` (SCL)
- **SPI (LED Matrix):** `GP11` (MOSI), `GP13` (SCK), `GP10` (CS)
- **Digital (DHT22):** `GP15`
- **Ultrasonic (HC-SR04):** `GP16` (Trig), `GP17` (Echo)
- **ADC (LDR):** `GP26`
- **PWM (Buzzer):** `GP14`
- **Input (Buttons):** `GP18`, `GP19`

## 🧠 Key Features
### 1. Contextual Awareness
The system uses the **HC-SR04** to detect your arrival.
- **Distance > 1m:** Low-power mode, scrolling clock on Matrix.
- **Distance < 50cm:** "Welcome" sequence, OLED lights up with full data.

### 2. Environment Safeguard
The **DHT22** and **LDR** work together to ensure your comfort:
- High Temperature Alert: Buzzer warning + visual icon.
- Low Light Warning: Reminder to turn on desk lamps for eye safety.

### 3. Progression Logic
The software includes a "Daily Multiplier" system. Starting at `1.0x`, the multiplier increases by `0.01` each day.
- **Goal:** Reach `2.0x` Multiplier.
- **Timeframe:** 100 Days of consistent operation.

## 📂 Installation
1. Flash **MicroPython** firmware to your Pi Pico.
2. Clone this repository.
3. Upload the `lib/` folder containing drivers for the SSD1306 and MAX7219.
4. Run `main.py`.

---
*Developed with ❤️ for the Pi Pico Community.*
