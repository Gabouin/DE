# Contributing to Sentinel-Pico

Thank you for your interest in contributing! Sentinel-Pico is a hobby project that **can be improved a lot**, and there are plenty of opportunities to **add cool features**, fix bugs, or improve the documentation. All skill levels are welcome.

---

## Table of Contents

- [What could be added](#what-could-be-added)
- [How to Propose Changes](#how-to-propose-changes)
- [Opening an Issue](#opening-an-issue)
- [Creating a Pull Request](#creating-a-pull-request)
- [Code Style (MicroPython)](#code-style-micropython)
- [Testing on the Pico](#testing-on-the-pico)
- [Documenting Wiring Changes](#documenting-wiring-changes)

---

## What could be added

This project can still be improved a lot. Here are some ideas for future features:

- **Wi-Fi dashboard** — push sensor data to a web page using the Pico W
- **BLE notifications** — send a phone alert when lighting is too dim
- **CO2 / air-quality sensor** — add an MH-Z19 or SGP30 for air quality monitoring
- **Configurable thresholds** — read distance/light thresholds from a `config.json` on the filesystem
- **Sleep / wake animation** — add a small animation when someone sits down
- **Data logging** — write sensor readings to a CSV file on an SD card
- **Multi-user greeting** — detect different users by RFID card

---


## How to Propose Changes

1. **Fork** the repository and create a new branch from `main`:
   ```bash
   git checkout -b feature/my-cool-feature
   ```
2. Make your changes (see style and testing guidelines below).
3. Commit with a clear message:
   ```bash
   git commit -m "feat: add BLE notification when light is too dim"
   ```
4. Push your branch and open a Pull Request against `main`.

---

## Opening an Issue

If you find a bug or have an idea for a new feature, please open an issue before writing code. This helps avoid duplicated effort and lets us discuss the best approach.

A good issue includes:
- A clear title and description
- Steps to reproduce (for bugs)
- What you expected vs. what actually happened
- Your hardware setup or Wokwi link (if relevant)

---

## Creating a Pull Request

- Keep PRs focused: one feature or fix per PR is easier to review.
- Reference any related issue in the PR description (e.g., `Closes #12`).
- Update the `README.md` if your change affects wiring, configuration, or behaviour.
- Make sure your code runs without errors on Wokwi or real hardware before submitting.

---

## Code Style (MicroPython)

- Use **4 spaces** for indentation (no tabs).
- Keep variable names lowercase with underscores: `ldr_value`, `dist_cm`.
- Add a short comment on any non-obvious line.
- Avoid importing modules that are not available in MicroPython (no `os.path`, no `threading`, etc.).
- Prefer built-in MicroPython libraries (`machine`, `dht`, `time`) over third-party ones.

---

## Testing on the Pico

1. Flash the latest **MicroPython** firmware on a Raspberry Pi Pico.
2. Copy the modified `deskstation.py` (and `ssd1306.py` if changed) using **Thonny** or **mpremote**:
   ```bash
   mpremote cp deskstation.py :main.py
   mpremote cp ssd1306.py :ssd1306.py
   ```
3. Open a serial monitor and confirm the OLED shows the expected screens for each sensor state.
4. If you don't have physical hardware, you can test using the [Wokwi simulator](https://wokwi.com/projects/462996062362677249).

---

## Documenting Wiring Changes

If your contribution adds or changes wiring:

- Update the **Hardware / Components** table in `README.md`.
- Update the **Wiring / Pinout** section in `README.md` with the new pin assignments.
- If you created a new Wokwi diagram, include the updated link in the README.

---

Again, thank you for contributing — every improvement, no matter how small, makes the project better!
