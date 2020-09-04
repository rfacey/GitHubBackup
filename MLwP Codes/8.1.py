# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 23:03:51 2020

@author: myousuf
"""

# Load library
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image as grayscale
image = cv2.imread("images/plane.jpg", cv2.IMREAD_GRAYSCALE)
#If we want to view the image, we can use the Python plotting library Matplotlib:
# Show image
plt.imshow(image, cmap="gray"), plt.axis("off")
plt.show()
