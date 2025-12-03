# lastwar-alliance-help

This script automatically detects and clicks on the help button in Last War. Here's what it does:

Main Functionality:

Continuously searches the screen for two possible images: help.png or help_bluestacks.png
Runs silently until it finds one of the images
When found, waits a random delay (0-5 seconds) to appear more human-like
Confirms the image is still there after the delay
If still present, clicks on it and returns the mouse to its original position
Only prints output when it successfully finds and clicks an image

Key Features:

Silent operation: No output while searching, only prints when images are detected
Click counter: Tracks only successful clicks (not just detections)
Timestamps: All messages include the current date/time
Human-like behavior: Random delays before clicking
Failsafe protection: Moving mouse to screen corner stops the script
Verification: Double-checks the image is still there before clicking to avoid false positives

Output Format:

[2025-12-03 14:30:15] Found help.png! Waiting for 2.34 seconds...
[2025-12-03 14:30:17] Clicking at (500, 300) - Successful click #1
[2025-12-03 14:30:17] Returned to original position (800, 600)

The script runs indefinitely until you stop it with CTRL+C.
