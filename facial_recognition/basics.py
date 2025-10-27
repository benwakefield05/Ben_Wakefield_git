import cv2
import face_recognition

Bill_Gates = cv2.imread("resources/Bill_Gates.jpg")
test_img = cv2.imread("resources/Bill_Gates_2.jpg")

# will return (top, right, bottom, left)
face_location = face_recognition.face_locations(Bill_Gates)[0]
test_face_location = face_recognition.face_locations(test_img)[0]

cv2.rectangle(Bill_Gates, (face_location[3], face_location[0], face_location[1], face_location[2]), (255, 255, 0), 3)

cv2.rectangle(test_img, (test_face_location[3], test_face_location[0], test_face_location[1], test_face_location[2]), (255, 255, 0), 3)

cv2.imshow("Bill Gates", Bill_Gates)
cv2.imshow("Test Image", test_img)

cv2.waitKey(7000)
