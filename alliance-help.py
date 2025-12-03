import pyautogui
import time
import random
from datetime import datetime

def find_and_click_image():
    print("Starting image detection loop - Press CTRL+C to stop")
    count = 0
    
    while True:  # Run indefinitely until manually stopped
        try:
            # Store current mouse position
            original_x, original_y = pyautogui.position()
            
            # Look for either image
            help_location = None
            
            # First try to find help.png
            try:
                help_location = pyautogui.locateOnScreen('help.png', confidence=0.8)
                if help_location:
                    image_name = 'help.png'
            except:
                pass
                
            # If not found, try help_bluestacks.png
            if not help_location:
                try:
                    help_location = pyautogui.locateOnScreen('help_bluestacks.png', confidence=0.8)
                    if help_location:
                        image_name = 'help_bluestacks.png'
                except:
                    pass
            
            # If either image was found
            if help_location:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Generate random delay between 0-5 seconds
                delay = random.uniform(0, 5)
                print(f"[{timestamp}] Found {image_name}! Waiting for {delay:.2f} seconds...")
                time.sleep(delay)
                
                # Confirm image is still there after delay
                confirmation = None
                try:
                    confirmation = pyautogui.locateOnScreen(image_name, confidence=0.8)
                except:
                    pass
                
                if confirmation:
                    # Get center of the image
                    target_x, target_y = pyautogui.center(confirmation)
                    
                    # Click the image
                    count += 1
                    print(f"[{timestamp}] Clicking at ({target_x}, {target_y}) - Successful click #{count}")
                    pyautogui.click(target_x, target_y)
                    
                    # Return to original position
                    pyautogui.moveTo(original_x, original_y)
                    print(f"[{timestamp}] Returned to original position ({original_x}, {original_y})")
                else:
                    print(f"[{timestamp}] Image disappeared during delay, continuing search...")
            
            # Small pause to reduce CPU usage
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(1)  # Wait a bit before retrying

if __name__ == "__main__":
    try:
        # Make sure pyautogui works correctly
        pyautogui.FAILSAFE = True
        find_and_click_image()
    except KeyboardInterrupt:
        print("\nScript terminated by user (CTRL+C)")
