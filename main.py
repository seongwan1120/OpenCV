import cv2

## 영상 이미지 읽기

src = cv2.imread('Nature99(Small)/picture01.jpg')

## 영상 디스플레이

cv2.imshow('src', src)

## 마무리

cv2.waitKey(0)
cv2.destroyAllWindows()
