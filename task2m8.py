import cv2
import numpy as np

import cv2
import numpy as np

# 1. read image in grayscale
img1 = cv2.imread("Elephants1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("Elephants2.jpg", cv2.IMREAD_GRAYSCALE)

# 2. thresholding
_, thresh = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)

# 3. gaussian Blur
gaussian = cv2.GaussianBlur(img1, (5, 5), 0)

# 4. edge Detection
edges = cv2.Canny(img1, 100, 200)

# 5. eeature Detection 
orb = cv2.ORB_create()
keypoints, descriptors = orb.detectAndCompute(img1, None)
img_features = cv2.drawKeypoints(img1, keypoints, None, color=(0,255,0))

# 6. eanorama Stitching
stitcher = cv2.Stitcher_create()
(status, pano) = stitcher.stitch([img1, img2])

# ehow results
cv2.imshow("Original Grayscale", img1)
cv2.imshow("Threshold", thresh)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Edges", edges)
cv2.imshow("Features", img_features)

if status == cv2.STITCHER_OK:
    cv2.imshow("Panorama", pano)
    cv2.imwrite("panorama_result.jpg", pano)  
else:
    print("Panorama stitching failed!")

cv2.waitKey(0)
cv2.destroyAllWindows()