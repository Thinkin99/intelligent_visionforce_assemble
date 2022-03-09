import numpy as np
# import cv2
# chess_board_x_num=6
# chess_board_y_num=6
# i=1
# while i in range(13):
#     path = "D:/Desktop/eyehand0309/" + str(i) + ".jpg"
#     img = cv2.imread(path)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     ret, corners = cv2.findChessboardCorners(gray, (chess_board_x_num, chess_board_y_num), None)
#     cv2.drawChessboardCorners(img, (chess_board_x_num, chess_board_y_num), corners, ret)
#     name="D:/Desktop/eyehand0309/after"+str(i)+".jpg"
#     cv2.imwrite(name,img)
#     i=i+1;
#     # cv2.imshow("gray", img)
#
#
#
# with open("D:/Desktop/eyehand0309/eyehand.txt", "r") as f:  # 打开文件
#     data = f.read()  # 读取文件
#     datalist=list(data)
#     print(data)
#     print(datalist[1])
def quaternion_to_rotation_matrix(q):  # x, y ,z ,w
    rot_matrix = np.array(
        [[1.0 - 2 * (q[1] * q[1] + q[2] * q[2]), 2 * (q[0] * q[1] - q[3] * q[2]), 2 * (q[3] * q[1] + q[0] * q[2])],
         [2 * (q[0] * q[1] + q[3] * q[2]), 1.0 - 2 * (q[0] * q[0] + q[2] * q[2]), 2 * (q[1] * q[2] - q[3] * q[0])],
         [2 * (q[0] * q[2] - q[3] * q[1]), 2 * (q[1] * q[2] + q[3] * q[0]), 1.0 - 2 * (q[0] * q[0] + q[1] * q[1])]],
        )
    return rot_matrix
data = []
with open("D:/Desktop/eyehand0309/eyehand.txt") as f:
    for line in f.readlines():
        temp = line.split()
        datafloat=[]
        for i in temp:
            datafloat.append(float(i))
        data.append(datafloat)
print(data[0])
q=[0.0277,	0.2267	,0.9714	,0.0655]
print(quaternion_to_rotation_matrix(q))
