import cv2
'''
# reading image
img = cv2.imread('img.png')
cv2.imshow('WINDOW NAME', img)
'''
# reading video
cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  
  if not ret:
    break

  # resized_frame = cv2.resize(frame, (500, 500))

  # hsv = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

  # cv2.rectangle(resized_frame, (50, 50), (350, 350) , (0, 0, 255), thickness=1)
  
  # drawing a line 
  cv2.line(frame, (100, 100), (400, 400), (0, 255, 0), 5)

  cv2.imshow('Web Cam', frame)

  if cv2.waitKey(1) == ord('q'):
    break

  # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # blur = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)

  # Edge Cascade
  # canny = cv2.Canny(img, 125, 175)



print(f'Shape: {frame.shape}')

cap.release()
cv2.destroyAllWindows()

