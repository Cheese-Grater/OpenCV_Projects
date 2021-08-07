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
    if k%256 == 32:
        # SPACE pressed
        img_name = "photo_taken.png"
        cv2.imwrite(img_name, frame)
        break

cam.release()
cv2.destroyAllWindows()
hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
rgb_img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
hsl_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HLS)
cmy_img = cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
cv2.imshow("HSV Image",hsv_img)
cv2.waitKey(0) 
cv2.imshow("RGB Image",rgb_img)
cv2.waitKey(0) 
cv2.imshow("HSL Image",hsl_img)
cv2.waitKey(0) 
cv2.imshow("CMY Image",cmy_img)
cv2.waitKey(0) 


