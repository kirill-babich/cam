import cv2
#url = "rtsp://admin:admin@192.168.1.168:554/0"
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)

    #Размеры в пикселях
    #cv2.resizeWindow('Video', 2000, 2000)

    #Черно-белое
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray feed', gray)
    key = cv2.waitKey(1)
    if key == ord('p'):
        cv2.waitKey(-1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()