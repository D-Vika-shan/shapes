import cv2

cam = cv2.VideoCapture("input_video.mp4")
count = 0
while True:
    ret, frame = cam.read()
    if not ret:
        break
    count += 1
    if count % 4 == 0:
        continue
    cv2.imshow("Output Video", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
