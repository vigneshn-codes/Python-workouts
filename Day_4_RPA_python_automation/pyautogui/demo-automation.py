import pyautogui
import time
import sys

# ====== GLOBAL SETTINGS ======
pyautogui.FAILSAFE = True   # Move mouse to top-left to abort
pyautogui.PAUSE = 0.5       # pause after each action


# ====== UTILITY FUNCTIONS ======

def wait(seconds=2):
    print(f"Waiting {seconds}s...")
    time.sleep(seconds)


def wait_for_element(image, timeout=10, confidence=0.8):
    """Wait until an image appears on screen"""
    start = time.time()
    while time.time() - start < timeout:
        pos = pyautogui.locateCenterOnScreen(image, confidence=confidence)
        if pos:
            print(f"Found element: {image} at {pos}")
            return pos
    print(f"Timeout: {image} not found")
    return None


# ====== MOUSE OPERATIONS ======

def mouse_operations():
    print("Running mouse operations...")
    pyautogui.moveTo(400, 300, duration=1)
    # pyautogui.click()
    # pyautogui.doubleClick()
    # pyautogui.rightClick()
    # pyautogui.dragTo(700, 300, duration=1)
    print("Mouse operations done")


# ====== KEYBOARD OPERATIONS ======

def keyboard_operations():
    print("Running keyboard operations...")
    pyautogui.write("Hello Automation!", interval=0.05)
    # pyautogui.press('enter')
    # pyautogui.hotkey('ctrl', 's')
    # pyautogui.press('esc')
    print("Keyboard operations done")


# ====== SCROLL TEST ======

def scroll_test():
    print("Scrolling down")
    pyautogui.scroll(-500)
    wait(1)
    print("Scrolling up")
    pyautogui.scroll(500)

# ====== SCREENSHOT TEST ======

def take_screenshot():
    filename = f"screenshot_{int(time.time())}.png"
    pyautogui.screenshot(filename)
    print(f"Screenshot saved: {filename}")


# ====== PIXEL COLOR VALIDATION ======

def validate_pixel(x=100, y=200, expected=(0, 128, 0)):
    pixel = pyautogui.pixel(x, y)
    print(f"Pixel at ({x},{y}) = {pixel}")
    if pixel == expected:
        print("Expected color detected ✅")
    else:
        print("Color does not match ❌")


# ====== IMAGE CLICK TEST ======

def click_image(image):
    pos = wait_for_element(image)
    if pos:
        pyautogui.click(pos)


# ====== SAMPLE LOGIN FLOW ======

def login_test():
    print("Starting login automation...")
    wait(3)

    pyautogui.click(600, 350)
    pyautogui.write("testuser")

    pyautogui.click(600, 420)
    pyautogui.write("password123")

    pyautogui.click(650, 500)
    print("Login flow executed")


# ====== END-TO-END DEMO FLOW ======

def end_to_end_flow():
    print("Running end-to-end demo...")
    wait(2)

    pyautogui.click(300, 300)
    pyautogui.write("Test Data")
    pyautogui.press('enter')

    wait(1)
    take_screenshot()

    print("Demo flow complete")


# ====== MENU ======

def show_menu():
    print("""
PyAutoGUI Test Suite
--------------------
1. Mouse operations
2. Keyboard operations
3. Scroll test
4. Screenshot test
5. Pixel validation
6. Click image element
7. Login test
8. End-to-end demo
9. Run ALL tests
0. Exit
""")


def run_all():
    # mouse_operations()
    # keyboard_operations()
    scroll_test()
    take_screenshot()
    validate_pixel()
    end_to_end_flow()


# ====== MAIN ======

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Select option: ")

        if choice == "1":
            mouse_operations()

        elif choice == "2":
            keyboard_operations()

        elif choice == "3":
            scroll_test()

        elif choice == "4":
            take_screenshot()

        elif choice == "5":
            validate_pixel()

        elif choice == "6":
            img = input("Enter image filename: ")
            click_image(img)

        elif choice == "7":
            login_test()

        elif choice == "8":
            end_to_end_flow()

        elif choice == "9":
            run_all()

        elif choice == "0":
            sys.exit()

        else:
            print("Invalid choice")