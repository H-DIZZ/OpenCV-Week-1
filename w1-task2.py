import cv2 as cv

capture = cv.VideoCapture("C:\\Users\\hirom\\OneDrive\\Documents\\Pictures\\MTRX1705 Biased Coin Toss Demo.mp4")

while True:

  retval, frame = capture.read() # retval is bool for successful read_

  # Exit loop once end of the video is reached_

  if not retval:

    break

  cv.imshow("Display name", frame)

  if cv.waitKey(17) ==ord('d'): # Close if 'd' is pressed_

    break

capture.release()

cv.destroyAllWindows()