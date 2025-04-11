"""
Created on Tue Apr  11 09:50:48 2025

@author: ArnoldMurphy
"""

import numpy as np

def average_pixel_brightness(img, circles, size=20):
    av_value = []
    for coords in circles[0, :]:
        x, y = coords[0], coords[1]
        region = img[y - size:y + size, x - size:x + size]
        av_value.append(np.mean(region))
    return av_value

def get_radii(circles):
    return [coords[2] for coords in circles[0, :]]

def classify_coin(radius, brightness):
    if brightness > 150 and radius > 110:
        return 10
    elif brightness > 150 and radius <= 110:
        return 5
    elif brightness <= 150 and radius > 110:
        return 2
    else:
        return 1

#EOF
# The above code is a utility module for coin detection and classification.
