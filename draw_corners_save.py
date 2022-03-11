import numpy as np
import cv2
chess_board_x_num=10
chess_board_y_num=7
i=1
while i in range(13):
    path = "D:/Desktop/eyehand0309/" + str(i) + ".jpg"
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (chess_board_x_num, chess_board_y_num), None)
    cv2.drawChessboardCorners(img, (chess_board_x_num, chess_board_y_num), corners, ret)
    name="D:/Desktop/eyehand0309/after"+str(i)+".jpg"
    cv2.imwrite(name,img)
    i=i+1;