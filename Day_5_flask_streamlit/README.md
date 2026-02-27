🚀 API Response Tester Dashboard

A lightweight developer tool built using Flask (Backend API) and Streamlit (Frontend UI) to test external APIs, measure response times, and inspect responses in real time.

This project helps developers quickly debug endpoints and validate API performance without relying on tools like Postman.

📌 Features

✅ Test GET and POST APIs

⏱ Measure response time (milliseconds)

📦 View formatted JSON response

🧾 Inspect response headers

🔐 Send custom request headers

📝 Send custom JSON payload

🎯 Clean and interactive UI

🏗️ Architecture Overview

Streamlit UI → Flask API → External API

Streamlit handles user interaction and dashboard display.

Flask processes incoming requests and measures response time.

Requests library performs HTTP calls to external APIs.

📂 Project Structure
api-response-tester/
│
├── app.py              # Flask backend
├── streamlit_app.py    # Streamlit frontend
├── requirements.txt
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/YOUR_GITHUB_USERNAME/api-response-tester.git
cd api-response-tester
2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Running the Application
Step 1: Start Flask Backend
python app.py

The Flask server will run at:

http://127.0.0.1:5000
Step 2: Start Streamlit Frontend

Open a new terminal window and run:

streamlit run streamlit_app.py

Your browser will automatically open the dashboard.

🧪 Example API Tests
🔹 Example GET Request

Use:

https://jsonplaceholder.typicode.com/posts/1

Click Send Request to view response details.

🔹 Example POST Request

URL

https://jsonplaceholder.typicode.com/posts

Payload

{
  "title": "test",
  "body": "hello world",
  "userId": 1
}
📊 Dashboard Output

After sending a request, the dashboard displays:

Status Code

Response Time (ms)

Response Body

Response Headers

🛠️ Tech Stack

Python 3.9+

Flask – Backend REST API

Streamlit – Frontend UI

Requests – HTTP client library

🚀 Future Enhancements

📈 Response time analytics charts

🗂 Request history storage (SQLite)

🔐 Bearer token authentication support

🚦 Load testing (multiple concurrent requests)

🐳 Docker support

☁️ Cloud deployment (Render / Azure / AWS)

🎯 Use Cases

API debugging

Backend validation

Microservices testing

Performance measurement

Developer productivity tool

👨‍💻 Author

Vignesh Nagarajan

Full Stack Developer | Backend & Automation Enthusiast

📄 License

This project is open-source and available under the MIT License.

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

