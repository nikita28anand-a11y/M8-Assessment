import cv2
import numpy as np

# 1. read and display image
img = cv2.imread("landscape_photography_tips_featured_image.webp")   
cv2.imshow("Original", img)

# 2. save image
cv2.imwrite("saved_lion.jpg", img)

# 3. resize, rotate, flip, crop
resized = cv2.resize(img, (300, 300))  
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  
flipped = cv2.flip(img, 1)   
cropped = img[50:250, 100:300]  

# 4. work with image arrays using NumPy
print("Image shape:", img.shape)        
print("Pixel value at (100,100):", img[100,100]) 

# 5. split and merge color channels
b, g, r = cv2.split(img)
merged = cv2.merge([r, g, b])   

# show resultsd
# resized
cv2.imshow("Resized", resized)
# rotated
cv2.imshow("Rotated", rotated)
# flipped
cv2.imshow("Flipped", flipped)
# cropped
cv2.imshow("Cropped", cropped)

cv2.imshow("Merged Channels", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()