import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
import pylab
from skimage import io

img = "/Users/Mikazuki/Document/GitHub/Digital Image Processing/Gesture Recognition/1.jpg"

srcImage = cv2.imread(img)
grayImage = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
plt.imshow(grayImage)
plt.show()
