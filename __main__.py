import csv
from pynput.mouse import Listener
import pygetwindow as gw
from datetime import datetime

# Define the CSV file path
csv_file = 'mouse_clicks.csv'

# Create or open the CSV file and write the header if the file doesn't exist
def create_csv_file():
    try:
        with open(csv_file, mode='x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'X', 'Y', 'Window Title'])
    except FileExistsError:
        pass  # If the file already exists, don't do anything

# Function to write click data to CSV
def write_to_csv(timestamp, x, y, window_title):
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, x, y, window_title])

# Define the on_click function to track mouse clicks and store them
def on_click(x, y, button, pressed):
    if pressed:
        # Get the active window at the time of click
        active_window = gw.getActiveWindow()
        if active_window:
            window_title = active_window.title
        else:
            window_title = "Unknown Window"
        
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Print the click details (optional)
        print(f"Mouse clicked at X={x}, Y={y} on {window_title}")
        
        # Write data to CSV
        write_to_csv(timestamp, x, y, window_title)

# Create the CSV file with a header if it doesn't exist
create_csv_file()

# Start the mouse listener
with Listener(on_click=on_click) as listener:
    listener.join()
