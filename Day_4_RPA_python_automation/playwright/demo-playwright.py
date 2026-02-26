from pathlib import Path
from playwright.sync_api import sync_playwright


# =============================
# CONFIG
# =============================

BASE_URL = "https://example.com"
SCRIPT_DIR = Path(__file__).parent


# =============================
# TEST FUNCTIONS
# =============================

def open_browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    return browser, page


def navigate_test(page):
    print("Navigating to site...")
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")


def click_and_input_test(page):
    print("Typing into input field...")
    # Use a page that actually has a search box
    page.goto("https://duckduckgo.com/")
    page.wait_for_selector("input[name='q']")
    page.fill("input[name='q']", "Playwright automation")
    page.press("input[name='q']", "Enter")


def button_click_test(page):
    print("Clicking button...")
    # Ensure we are on the correct page and the element exists
    page.goto(BASE_URL)
    page.wait_for_selector("text=Learn more")
    page.click("text=Learn more")


def wait_test(page):
    print("Waiting for element...")
    page.wait_for_selector("h1")


def dropdown_test(page):
    print("Handling dropdown...")
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.select_option("#dropdown", "2")


def checkbox_test(page):
    print("Checking checkbox...")
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.check("input[type=checkbox]:first-child")


def file_upload_test(page):
    print("Uploading file...")
    page.goto("https://the-internet.herokuapp.com/upload")
    file_path = SCRIPT_DIR / "sample.txt"
    page.set_input_files("#file-upload", str(file_path))
    page.click("#file-submit")


def keyboard_test(page):
    print("Keyboard operations...")
    page.goto("https://example.com")
    page.keyboard.press("PageDown")


def scroll_test(page):
    print("Scrolling page...")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")


def screenshot_test(page):
    print("Taking screenshot...")
    page.screenshot(path="screenshot.png")


def assertion_test(page):
    print("Validating page title...")
    assert "Example Domain" in page.title()


def multi_tab_test(page, context):
    print("Opening new tab...")
    new_page = context.new_page()
    new_page.goto("https://example.com")
    print("New tab title:", new_page.title())
    new_page.close()


def login_flow_example(page):
    """
    Demo login flow (replace selectors with your app)
    """
    print("Running login flow...")
    page.goto("https://example.com")

    # Replace with real selectors
    # page.fill("#username", "testuser")
    # page.fill("#password", "password123")
    # page.click("#login-btn")


def end_to_end_demo(page):
    print("Running end-to-end demo...")
    page.goto("https://example.com")
    page.wait_for_selector("h1")
    screenshot_test(page)


# =============================
# RUN ALL TESTS
# =============================

def run_all_tests():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        navigate_test(page)
        wait_test(page)
        assertion_test(page)
        screenshot_test(page)
        scroll_test(page)
        keyboard_test(page)
        multi_tab_test(page, context)
        end_to_end_demo(page)

        browser.close()


# =============================
# MENU
# =============================

def menu():
    print("""
Playwright Test Suite
---------------------
1. Navigate test
2. Input & search
3. Button click
4. Dropdown test
5. Checkbox test
6. File upload
7. Screenshot
8. Scroll test
9. Multi-tab test
10. Run ALL tests
0. Exit
""")


def main():
    with sync_playwright() as playwright:
        browser, page = open_browser(playwright)
        context = page.context

        while True:
            menu()
            choice = input("Select option: ")

            if choice == "1":
                navigate_test(page)

            elif choice == "2":
                click_and_input_test(page)

            elif choice == "3":
                button_click_test(page)

            elif choice == "4":
                dropdown_test(page)

            elif choice == "5":
                checkbox_test(page)

            elif choice == "6":
                file_upload_test(page)

            elif choice == "7":
                screenshot_test(page)

            elif choice == "8":
                scroll_test(page)

            elif choice == "9":
                multi_tab_test(page, context)

            elif choice == "10":
                run_all_tests()

            elif choice == "0":
                browser.close()
                break

            else:
                print("Invalid choice")


if __name__ == "__main__":
    main()