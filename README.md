# lastwar-alliance-help

A small automation script that detects and clicks the in-game **Help** button in **Last War**.

## What it does

- Continuously scans your screen for either `help.png` or `help_bluestacks.png`
- Runs silently while searching (no spammy logs)
- When an image is found:
  - waits a random delay (0–5s) to look more human
  - verifies the image is still present after the delay
  - clicks it
  - returns your mouse to its original position
- Only prints output when a click actually happens

## Key features

- **Silent operation:** no output until an image is found *and clicked*
- **Click counter:** tracks only successful clicks (not just detections)
- **Timestamps:** every message includes the current date/time
- **Human-like behavior:** random delay before clicking
- **Failsafe protection:** moving the mouse to a screen corner stops the script
- **Verification step:** double-checks the image is still there to avoid false positives

## Example output

```text
[2025-12-03 14:30:15] Found help.png! Waiting for 2.34 seconds...
[2025-12-03 14:30:17] Clicking at (500, 300) - Successful click #1
[2025-12-03 14:30:17] Returned to original position (800, 600)
