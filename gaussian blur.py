import cv2

image=cv2.imread("johncena.jpg")                        # Type the file name with extension
gaussianBlurImg=cv2.GaussianBlur(image,(33,33),0)       # Here (33,33) value respresents the thickness of the blur
cv2.imshow("Original image",image)
cv2.imshow("Gaussianblur image",gaussianBlurImg)


# if u want more blur just increse those values ( use only odd numbers )     
