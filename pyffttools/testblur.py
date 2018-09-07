from blurbuilder import BlurBuilder
import numpy as np
import cv2

img = cv2.imread('~\\..\\Physicians.jpg')
height, width, channels = img.shape
data = np.asarray(img, float)/255
builder = BlurBuilder((int)(height/2), (int)(width/2))
cv2.imshow('image', builder.Blur(data))
cv2.imshow('filter', builder.ToBitmap(data.shape))
cv2.waitKey(0)
cv2.destroyAllWindows()
