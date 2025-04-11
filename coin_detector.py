"""
Created on Tue Apr  11 09:50:48 2025

@author: ArnoldMurphy
"""

import cv2
import numpy as np
import os
from utils.coin_utils import average_pixel_brightness, get_radii, classify_coin

# File paths
image_path = 'images/capstone_coins.png'
output_image_path = 'output/detected_coins.png'
log_file_path = 'output/detection_log.txt'

# Load image
gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
color = cv2.imread(image_path)

# Preprocess image
gray_blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect coins
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

if circles is not None:
    circles = np.uint16(np.around(circles))
    brightness_values = average_pixel_brightness(gray, circles, size=20)
    radii = get_radii(circles)

    # Prepare log
    log_lines = []
    total_value = 0

    for idx, (coords, brightness, radius) in enumerate(zip(circles[0, :], brightness_values, radii)):
        x, y, r = coords
        value = classify_coin(radius, brightness)
        total_value += value

        # Draw coins
        cv2.circle(color, (x, y), r, (0, 255, 0), 2)
        cv2.circle(color, (x, y), 2, (0, 0, 255), 3)
        cv2.putText(color, f"{value}p", (x - 30, y), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 3)

        log_lines.append(
            f"Coin {idx + 1}: Center=({x}, {y}), Radius={radius}, Brightness={brightness:.2f}, Value={value}p"
        )

    # Add total value
    total_line = f"ESTIMATED TOTAL VALUE: {total_value}p"
    log_lines.append("\n" + total_line)
    cv2.putText(color, total_line, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)

    # Save output image
    cv2.imwrite(output_image_path, color)

    # Save log file
    with open(log_file_path, 'w') as log_file:
        log_file.write("\n".join(log_lines))

    # Show result
    cv2.imshow("Detected Coins", color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(f"\n✅ Results saved to: {output_image_path}")
    print(f"📄 Log saved to: {log_file_path}")

else:
    print("⚠️ No coins detected.")


#EOF
# This script detects coins in an image, classifies them based on their size and brightness, and logs the results.
