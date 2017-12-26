#python3
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/jlhelmers/Desktop/sudokubig.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F, ksize=7)

#lines = cv2.Canny(laplacian, 100,)

# pre-process the image by resizing it, converting it to
# graycale, blurring it, and computing an edge map


plt.subplot(11  1),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.show()
