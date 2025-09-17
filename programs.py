import pyautogui
import pyperclip
import time
import sys

# Ensure Unicode output works
sys.stdout.reconfigure(encoding='utf-8')

# Step 1: Give user time to focus screen (or you can auto-focus a window if needed)
print("Starting in 3 seconds... Move your mouse away!")
time.sleep(3)

# Step 2: Click the icon (to open or activate the window)
pyautogui.click(1221, 1067)
time.sleep(1.5)  # Increased wait

# Step 3: Drag to select text
pyautogui.moveTo(667, 220)
pyautogui.mouseDown()
pyautogui.moveTo(670, 1011, duration=0.7)  # Slower drag = more accurate selection
pyautogui.mouseUp()

# Step 4: Wait before copying
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')

# Step 5: Wait before accessing clipboard
time.sleep(1)
copied_text = pyperclip.paste()

# Step 6: Show the result
print("Copied Text:\n", copied_text)
