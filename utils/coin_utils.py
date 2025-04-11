"""
coin_utils.py

Utility functions for coin detection and classification using OpenCV and NumPy.

Functions:
- average_pixel_brightness: Computes average brightness around coin centers.
- get_radii: Extracts radii of detected coins.
- classify_coin: Classifies coins based on radius and brightness.

Author: Arnold Murphy
Created: April 11, 2025
"""

import numpy as np  # Import NumPy for numerical operations


def average_pixel_brightness(img, circles, size=20):
    """
    Calculates the average brightness around the center of each detected circle.

    Parameters:
        img (np.ndarray): Grayscale image.
        circles (np.ndarray): Array of detected circles [1, N, 3].
        size (int): Half-width of square region for averaging (default: 20).

    Returns:
        List[float]: List of average brightness values for each circle.
    """
    av_value = []  # List to hold brightness values

    for coords in circles[0, :]:
        x, y = coords[0], coords[1]  # Get x, y center of circle

        # Extract a square region around the circle center
        region = img[y - size:y + size, x - size:x + size]

        # Calculate the mean pixel intensity of the region
        average = np.mean(region)

        av_value.append(average)  # Store result

    return av_value  # Return list of brightness values


def get_radii(circles):
    """
    Extracts radii from detected circles.

    Parameters:
        circles (np.ndarray): Array of detected circles [1, N, 3].

    Returns:
        List[int]: Radii of each detected circle.
    """
    return [coords[2] for coords in circles[0, :]]


def classify_coin(radius, brightness):
    """
    Classifies coin denomination based on radius and brightness.

    Parameters:
        radius (int): Radius of the coin.
        brightness (float): Brightness around the coin's center.

    Returns:
        int: Coin value (1p, 2p, 5p, or 10p).
    """
    if brightness > 150 and radius > 110:
        return 10  # Bright and large -> 10p
    elif brightness > 150 and radius <= 110:
        return 5   # Bright and small -> 5p
    elif brightness <= 150 and radius > 110:
        return 2   # Dark and large -> 2p
    else:
        return 1   # Dark and small -> 1p


# End of file
