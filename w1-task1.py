import cv2 as cv

def main():


  fourier = cv.imread("C:\\Users\\hirom\\OneDrive\\Documents\\Pictures\\Fourier Terms.jpg")

  cv.imshow("Fourier", fourier) # Show window_

  cv.waitKey(0) # Wait and close window only when key is pressed_

if __name__ == "__main__":

  main()

