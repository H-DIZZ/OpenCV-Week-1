import cv2 as cv
import matplotlib.pyplot as plt

def main():
    fourier = cv.imread("C:\\Users\\hirom\\OneDrive\\Documents\\Pictures\\Fourier Terms.jpg")

    # Convert from BGR to RGB color space
    fourier_rgb = cv.cvtColor(fourier, cv.COLOR_BGR2RGB)

    # Plot the image using matplotlib
    plt.imshow(fourier_rgb)
    #plt.imshow(fourier)
    plt.title('Fourier Image in RGB') # Title of the plot
    plt.xlabel('Width') # X-axis label
    plt.ylabel('Height') # Y-axis label
    plt.show() # Show the plot

if __name__ == "__main__":
    main()


