"""
main.py

Main script for detecting and classifying coins in an image using OpenCV.

Steps:
1. Load and preprocess the input image.
2. Detect coins using Hough Circle Transform.
3. Extract brightness and radii of detected circles.
4. Classify coins based on radius and brightness.
5. Annotate the image and log the results.

Author: Arnold Murphy
Created: April 11, 2025
"""

import cv2  # OpenCV for image processing
import numpy as np  # NumPy for array operations
import os

# Import utility functions from the coin_utils module
from utils.coin_utils import average_pixel_brightness, get_radii, classify_coin

# ---------------------------------------------------------------------
# File Paths
# ---------------------------------------------------------------------
image_path = 'images/capstone_coins.png'          # Input image
output_image_path = 'output/detected_coins.png'   # Annotated output image
log_file_path = 'output/detection_log.txt'        # Log file with details

# ---------------------------------------------------------------------
# Load Image
# ---------------------------------------------------------------------
gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Load grayscale version
color = cv2.imread(image_path)                       # Load color version for annotation

# ---------------------------------------------------------------------
# Preprocess Image
# ---------------------------------------------------------------------
gray_blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur to reduce noise

# ---------------------------------------------------------------------
# Detect Coins using Hough Circle Transform
# ---------------------------------------------------------------------
circles = cv2.HoughCircles(
    gray_blurred,
    cv2.HOUGH_GRADIENT,
    dp=0.9,
    minDist=120,
    param1=50,
    param2=27,
    minRadius=60,
    maxRadius=120
)

# ---------------------------------------------------------------------
# If Coins Detected: Classify and Annotate
# ---------------------------------------------------------------------
if circles is not None:
    circles = np.uint16(np.around(circles))  # Round values to integers

    # Extract brightness values and radii of detected circles
    brightness_values = average_pixel_brightness(gray, circles, size=20)
    radii = get_radii(circles)

    total_value = 0         # Total coin value accumulator
    log_lines = []          # To store details for log file

    # Process each detected coin
    for idx, (coords, brightness, radius) in enumerate(zip(circles[0, :], brightness_values, radii)):
        x, y, r = coords

        # Classify the coin based on radius and brightness
        value = classify_coin(radius, brightness)
        total_value += value

        # Draw detected coin circle and center
        cv2.circle(color, (x, y), r, (0, 255, 0), 2)       # Outer circle
        cv2.circle(color, (x, y), 2, (0, 0, 255), 3)       # Center dot

        # Label the coin with its value
        cv2.putText(color, f"{value}p", (x - 30, y), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 3)

        # Add entry to the log
        log_lines.append(
            f"Coin {idx + 1}: Center=({x}, {y}), Radius={radius}, Brightness={brightness:.2f}, Value={value}p"
        )

    # Write total value on image and in log
    total_line = f"ESTIMATED TOTAL VALUE: {total_value}p"
    log_lines.append("\n" + total_line)
    cv2.putText(color, total_line, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)

    # Save annotated image
    cv2.imwrite(output_image_path, color)

    # Save log to file
    with open(log_file_path, 'w') as log_file:
        log_file.write("\n".join(log_lines))

    # Display final image with detected coins
    cv2.imshow("Detected Coins", color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"\n✅ Results saved to: {output_image_path}")
    print(f"📄 Log saved to: {log_file_path}")

# ---------------------------------------------------------------------
# No Coins Detected
# ---------------------------------------------------------------------
else:
    print("⚠️ No coins detected.")


# EOF
# This script detects coins in an image, classifies them by type,
# annotates them visually, and logs the results to a file.
