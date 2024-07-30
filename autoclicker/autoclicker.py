import time
import threading
import keyboard
import pyautogui

class AutoClicker:
    def __init__(self):
        self.clicking = False
        self.clicks_per_second = 10

    def set_clicks_per_second(self, clicks_per_second):
        self.clicks_per_second = clicks_per_second

    def click_loop(self):
        while self.clicking:
            pyautogui.click()
            time.sleep(1 / self.clicks_per_second)

    def start_clicking(self):
        self.clicking = True
        threading.Thread(target=self.click_loop).start()

    def stop_clicking(self):
        self.clicking = False

def main():
    auto_clicker = AutoClicker()

    print("AutoClicker - Press Ctrl+R to start, Ctrl+S to stop")

    def start_stop(event):
        if event.name == 'ctrl+r':
            auto_clicker.start_clicking()
            print("AutoClicker started")
        elif event.name == 'ctrl+s':
            auto_clicker.stop_clicking()
            print("AutoClicker stopped")

    keyboard.on_press(start_stop)

    while True:
        clicks_per_second = input("Enter clicks per second (default is 10): ")
        if clicks_per_second.isdigit():
            auto_clicker.set_clicks_per_second(int(clicks_per_second))
            break
        else:
            print("Invalid input. Please enter a valid number.")

    keyboard.wait('esc')

if __name__ == "__main__":
    main()