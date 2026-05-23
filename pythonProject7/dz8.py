import cv2
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
image = cv2.imread("woman69.jpeg")
mask = cv2.imread("mask.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for x, y, w, h in faces:
    resized_mask = cv2.resize(mask, (w, h))
    for i in range(h):
        for j in range(w):
            if not (
                resized_mask[i, j][0] > 240
                and resized_mask[i, j][1] > 240
                and resized_mask[i, j][2] > 240):
                image[y + i, x + j] = resized_mask[i, j]
cv2.imwrite("result.jpg", image)
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()