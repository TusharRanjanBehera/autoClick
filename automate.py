import pygetwindow as gw
import pyautogui
import time

# Function to maximize and click inside the Teams window
def maximize_and_click():
    try:
        teams_window = gw.getWindowsWithTitle("Microsoft Teams classic")[0]  # Get the Teams window
        teams_window.maximize()  # Maximize the Teams window

        # Wait for 1 second
        time.sleep(1)

        # Click inside the Teams window (replace these coordinates with the desired click position)
        pyautogui.click(teams_window.left + 50, teams_window.top + 50)  # Click 50 pixels from the top-left corner

        # Wait for 1 second
        time.sleep(1)

        teams_window.minimize()  # Minimize the Teams window

    except IndexError:
        print("No Microsoft Teams window found.")

# Loop to repeat the actions every 10 minutes
while True:
    maximize_and_click()
    time.sleep(600)  # 10 minutes delay (600 seconds)
