#**THIS ONE TAKES A FRAME FROM THE VIDEO FEED AND DETECTS CIRCLES
# import the necessary packages
import numpy as np
import cv2
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k % 256 == 32:
        # SPACE pressed
        img_name = "photo_taken.png"
        cv2.imwrite(img_name, frame)
        break

cam.release()
cv2.destroyAllWindows()

# load the image, clone it for output, and then convert it to grayscale
output = frame.copy()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
blurred = cv2.medianBlur(gray,3)
# detect circles in the image
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.2, 100)
# ensure at least some circles were found
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")
    # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5),
                      (x + 5, y + 5), (0, 128, 255), -1)
    # show the output image
    cv2.imshow("output", np.hstack([frame, output]))
    cv2.waitKey(0)
