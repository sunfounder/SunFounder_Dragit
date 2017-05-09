from time import sleep
import cv2
import cv2.cv as cv
import numpy as np

kernel = np.ones((5,5),np.uint8)

SCREEN_WIDTH = 160
SCREEN_HIGHT = 120
CENTER_X = SCREEN_WIDTH/2
CENTER_Y = SCREEN_HIGHT/2
BALL_SIZE_MIN = SCREEN_HIGHT/10
BALL_SIZE_MAX = SCREEN_HIGHT/3

# Filter setting, DONOT CHANGE
hmn = 12
hmx = 37
smn = 96
smx = 255
vmn = 186
vmx = 255

def destroy():
    img.release()


def find_blob() :
    radius = 0
    # Load input image
    img = cv2.VideoCapture(-1)
    img.set(3,SCREEN_WIDTH)
    img.set(4,SCREEN_HIGHT)
    _, bgr_image = img.read()

    orig_image = bgr_image

    bgr_image = cv2.medianBlur(bgr_image, 3)

    # Convert input image to HSV
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image, keep only the red pixels
    lower_red_hue_range = cv2.inRange(hsv_image, (0, 100, 100), (10, 255, 255))
    upper_red_hue_range = cv2.inRange(hsv_image, (160, 100, 100), (179, 255, 255))
    # Combine the above two images
    red_hue_image = cv2.addWeighted(lower_red_hue_range, 1.0, upper_red_hue_range, 1.0, 0.0)

    red_hue_image = cv2.GaussianBlur(red_hue_image, (9, 9), 2, 2)

    # Use the Hough transform to detect circles in the combined threshold image
    circles = cv2.HoughCircles(red_hue_image, cv.CV_HOUGH_GRADIENT, 1, 120, 100, 20, 10, 0);

    # Loop over all detected circles and outline them on the original image
    all_r = np.array([])
    if circles is not None:
        for i in circles[0]:

            all_r = np.append(all_r, int(round(i[2])))
        closest_ball = all_r.argmax()
        center=(int(round(circles[0][closest_ball][0])), int(round(circles[0][closest_ball][1])))
        radius=int(round(circles[0][closest_ball][2]))
        if draw_circle_enable:
            cv2.circle(orig_image, center, radius, (0, 255, 0), 5);

    # Show images
    if show_image_enable:
        cv2.namedWindow("Threshold lower image", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Threshold lower image", lower_red_hue_range)
        cv2.namedWindow("Threshold upper image", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Threshold upper image", upper_red_hue_range)
        cv2.namedWindow("Combined threshold images", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Combined threshold images", red_hue_image)
        cv2.namedWindow("Detected red circles on the input image", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Detected red circles on the input image", orig_image)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        return (0, 0), 0
    if radius > 3:
        return center, radius;
    else:
        return (-1, -1), -1

def get_color(x, y):
    img = cv2.VideoCapture(-1)
    img.set(3,SCREEN_WIDTH)
    img.set(4,SCREEN_HIGHT)

    _, bgr_image = img.read()

    orig_image = bgr_image

    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

    hsv_value = cv.Get2D(hsv_image,x,y)

    print hsv_value
