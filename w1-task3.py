import cv2 as cv

fourier = cv.imread("C:\\Users\\hirom\\OneDrive\\Documents\\Pictures\\Fourier Terms.jpg")

def rescale(fourier: cv.Mat, scale:float) -> cv.Mat:

  height =int(fourier.shape[0] * scale)

  width =int(fourier.shape[1] * scale)

  dim = (width, height)

  return cv.resize(fourier, dim, interpolation=cv.INTER_AREA)

fourier_rescaled = rescale(fourier, 0.3)

cv.imshow("Fourier Rescaled", fourier_rescaled) # Show window_

cv.waitKey(0) # Wait and close window only when key is pressed_
