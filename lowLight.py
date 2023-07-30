import cv2
import numpy as np

# Load the low-light image
img = cv2.imread('lowLight.jpg')

if img is None:
    print('Error: could not load image')
else:
    # Increase the brightness and contrast
    alpha = 1.5
    beta = 30
    img = cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)

    # Apply a bilateral filter to reduce noise while preserving edges
    img = cv2.bilateralFilter(img, 9, 75, 75)

    # Apply a histogram equalization to enhance the contrast
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    # Save the output image
    cv2.imwrite('improved_image.jpg', img)