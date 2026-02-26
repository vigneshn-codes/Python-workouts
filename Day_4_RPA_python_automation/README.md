## Day 4 – RPA & Automation (PyAutoGUI + Playwright)

This folder contains simple RPA-style automation demos using `pyautogui` (desktop GUI automation) and `playwright` (browser automation).

### Structure

- **pyautogui/**
  - `demo-automation.py` – menu-driven script showcasing:
    - Mouse operations
    - Keyboard input
    - Scrolling
    - Screenshots
    - Pixel color validation
    - Image-based clicking
    - A sample login flow
    - A small end-to-end demo

- **playwright/**
  - `demo-playwright.py` – menu-driven browser test suite with examples for:
    - Basic navigation and waits
    - Search input on DuckDuckGo
    - Button/link click on `example.com`
    - Dropdown and checkbox handling
    - File upload (using `sample.txt` in the same folder)
    - Scrolling, screenshots, keyboard operations
    - Multi-tab handling and a small end-to-end flow
  - `sample.txt` – file used by the upload test.

---

### Prerequisites

Create/activate a virtual environment (optional but recommended) and install dependencies:

```bash
cd Python-workouts
python3 -m venv myenv
source myenv/bin/activate

pip install pyautogui playwright
playwright install
```

On macOS, you may need to grant Screen Recording / Accessibility permissions for `pyautogui` to control the mouse and keyboard.

---

### Run PyAutoGUI demo

From the project root:

```bash
python3 Day_4_RPA_python_automation/pyautogui/demo-automation.py
```

Follow the on-screen menu to pick a scenario.

---

### Run Playwright demo

From the project root:

```bash
python3 Day_4_RPA_python_automation/playwright/demo-playwright.py
```

Then use the console menu:

- Options **1–5, 7–9** run individual browser interactions.
- Option **6** runs the file upload test (uses `sample.txt` from the `playwright` folder).
- Option **10** runs the full end-to-end sequence.

If you change test URLs or locators, update the functions in `demo-playwright.py` accordingly.

