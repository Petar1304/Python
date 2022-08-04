import matplotlib.pyplot as plt
import cv2
import numpy as np

img_path = ''
img = cv2.imread(img_path, 0) # 0 for grayscale


# SIFT algorithm
def sift_algorithm():
  sift = cv2.SIFT_create()
  kp = sift.detect(img, None)
  img_ = cv2.drawKeypoints(img, kp, img)
  cv2.imshow('SIFT', img_)


# ORB algorithm
def orb_algorithm():
  orb = cv2.ORB_create()
  kp = orb.detect(img, None)
  kp, des = orb.compute(img, kp)

  img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
  cv2.imshow("", img2)


# finding contours
def find_contours():
  blur = cv2.GaussianBlur(img, (3, 3), 0)
  canny = cv2.Canny(blur, 30, 150, 3)
  dilated = cv2.dilate(canny, (1, 1), iterations=0)

  (cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

  cv2.drawContours(img, cnt, -1, (0, 255, 0), 2)
  print(len(cnt))

  cv2.imshow('rgb', img)


# template matching algorithm
def template_matching():
  template_path = ''
  template = cv2.imread(template_path, 0)
  w, h = template.shape[::-1]

  # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
  res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

  # tweak to fix accuracy
  threshold = 0.4
  loc = np.where(res >= threshold)

  num = 0
  for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
    num += 1

  print(f'Number of flies: {num}')

  cv2.imshow('template_matching', img)


# draw rectangle
# cv2.rectangle(gray, [1280, 140], [1320, 180], (0, 255, 0), 3)

if __name__ == '__main__':
  # choose algorithm to test
  
  # template_matching()
  # find_contours()
  sift_algorithm()
  # orb_algorithm()

  # closing windows
  cv2.waitKey(0)
  cv2.destroyAllWindows()
