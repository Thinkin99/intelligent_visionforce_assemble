import cv2
import numpy as np
import time
import tuoyuan



# cv2.namedWindow('control')
# cv2.createTrackbar('threshold', 'control', 127, 255, tuoyuan.nothing)
j=1
while 1:
    path='Bearing/'+str(j)+'.jpg'
    img_raw = cv2.imread(path)
    img_copy = img_raw.copy()
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)  # 灰度图
    # t = cv2.getTrackbarPos('threshold', 'control')  # 得到滤波阈值
    # flag, binary = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)  # 二值化
    # cv2.imshow('binary', binary)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 70, param1=100, param2=45, minRadius=30,
                               maxRadius=70)  # hough圆
    print(circles)
    x = 0
    y = 0
    if np.any(circles):
        circles = np.uint(np.around(circles))
        for i in circles[0]:
            x, y, r = i
            cv2.circle(img_raw, (x, y), r, (0, 255, 0), 2)
            cv2.circle(img_raw, (x, y), 2, (0, 255, 0), 2)
            cv2.putText(img_raw, str((x, y)), (x + 20, y + 10), 0, 0.5,
                        [225, 255, 255], thickness=1, lineType=cv2.LINE_AA)
    cv2.imshow('detect', img_raw)
    j=j+1
    if j==44:
        j=1
    time.sleep(0.5)
    cv2.waitKey(20)




