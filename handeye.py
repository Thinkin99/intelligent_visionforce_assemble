import cv2
import numpy as np
import glob
from math import *
import pandas as pd
import os
# p[330.464 232.998]  f[603.283 602.968]
# K = fx		s		x0
#    	  0		fy		y0
# 	  0		0		1
# Camera
# Intrinsics
# IntrinsicMatrix: [3×3
# double]
# FocalLength: [597.3251 596.2561]
# PrincipalPoint: [332.6717 235.9280]
# Skew: 0
# RadialDistortion: [0.1335 - 0.2408]
# TangentialDistortion: [0 0]
# ImageSize: [480 640]
K=np.array([[597.3251,0,332.6717],
            [0,596.2561,235.9280],
            [0,0,1]],dtype=np.float64)#realsense d435i 相机内参
chess_board_x_num=10#棋盘格x方向格子数
chess_board_y_num=7#棋盘格y方向格子数
chess_board_len=20#单位棋盘格长度,mm
folder = r"D:/Desktop/eyehand0311"  # 棋盘格图片存放文件夹
file_address = r'D:/Desktop/eyehand0311/eyehand.txt'  # 从记录文件读取机器人六个位姿

# 四元数到旋转矩阵
def quaternion_to_rotation_matrix(q):  # x, y ,z ,w
    rot_matrix = np.array(
        [[1.0 - 2 * (q[1] * q[1] + q[2] * q[2]), 2 * (q[0] * q[1] - q[3] * q[2]), 2 * (q[3] * q[1] + q[0] * q[2])],
         [2 * (q[0] * q[1] + q[3] * q[2]), 1.0 - 2 * (q[0] * q[0] + q[2] * q[2]), 2 * (q[1] * q[2] - q[3] * q[0])],
         [2 * (q[0] * q[2] - q[3] * q[1]), 2 * (q[1] * q[2] + q[3] * q[0]), 1.0 - 2 * (q[0] * q[0] + q[1] * q[1])]],
        )
    return rot_matrix
#用于根据欧拉角计算旋转矩阵
def myRPY2R_robot(x, y, z):
    Rx = np.array([[1, 0, 0], [0, cos(x), -sin(x)], [0, sin(x), cos(x)]])
    Ry = np.array([[cos(y), 0, sin(y)], [0, 1, 0], [-sin(y), 0, cos(y)]])
    Rz = np.array([[cos(z), -sin(z), 0], [sin(z), cos(z), 0], [0, 0, 1]])
    R = Rz@Ry@Rx
    return R

#用于根据位姿计算变换矩阵
def pose_robot(q, Tx, Ty, Tz):
    # thetaX = x / 180 * pi
    # thetaY = y / 180 * pi
    # thetaZ = z / 180 * pi
    # R = myRPY2R_robot(thetaX, thetaY, thetaZ)
    R = quaternion_to_rotation_matrix(q)
    t = np.array([[Tx], [Ty], [Tz]])
    RT1 = np.column_stack([R, t])  # 列合并
    RT1 = np.row_stack((RT1, np.array([0,0,0,1])))
    # RT1=np.linalg.inv(RT1)
    return RT1

#用来从棋盘格图片得到相机外参
def get_RT_from_chessboard(img_path,chess_board_x_num,chess_board_y_num,K,chess_board_len):
    # '''
    # :param img_path: 读取图片路径
    # :param chess_board_x_num: 棋盘格x方向格子数
    # :param chess_board_y_num: 棋盘格y方向格子数
    # :param K: 相机内参
    # :param chess_board_len: 单位棋盘格长度,mm
    # :return: 相机外参
    # '''
    img=cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    size = gray.shape[::-1]
    ret, corners = cv2.findChessboardCorners(gray, (chess_board_x_num, chess_board_y_num), None)
    # print(corners)
    corner_points=np.zeros((2,corners.shape[0]),dtype=np.float64)
    for i in range(corners.shape[0]):
        corner_points[:,i]=corners[i,0,:]
    # print(corner_points)
    object_points=np.zeros((3,chess_board_x_num*chess_board_y_num),dtype=np.float64)
    flag=0
    for i in range(chess_board_y_num):
        for j in range(chess_board_x_num):
            object_points[:2,flag]=np.array([(11-j-1)*chess_board_len,(8-i-1)*chess_board_len])
            flag+=1
    # print(object_points)

    retval,rvec,tvec  = cv2.solvePnP(object_points.T,corner_points.T, K, distCoeffs=None)
    # print(rvec.reshape((1,3)))
    # RT=np.column_stack((rvec,tvec))
    RT=np.column_stack(((cv2.Rodrigues(rvec))[0],tvec))
    RT = np.row_stack((RT, np.array([0, 0, 0, 1])))
    # RT=pose(rvec[0,0],rvec[1,0],rvec[2,0],tvec[0,0],tvec[1,0],tvec[2,0])
    # print(RT)

    # print(retval, rvec, tvec)
    print(RT)
    print('')
    return RT



# good_picture =   # 存放可以检测出棋盘格角点的图片
good_picture=[1,2,3,4,5,6,7,8,9,10]
# file_num = len(good_picture)

# 计算board to cam 变换矩阵
R_all_chess_to_cam_1 = []
T_all_chess_to_cam_1 = []
for i in good_picture:
    # print(i)
    image_path = folder + '/' + str(i) + '.jpg'
    RT = get_RT_from_chessboard(image_path, chess_board_x_num, chess_board_y_num, K, chess_board_len)

    # RT=np.linalg.inv(RT)

    R_all_chess_to_cam_1.append(RT[:3, :3])
    T_all_chess_to_cam_1.append(RT[:3, 3].reshape((3, 1)))
print(R_all_chess_to_cam_1)

# 计算end to base变换矩阵
data=[]

with open(file_address) as f:
    for line in f.readlines():
        temp = line.split()
        datafloat=[]
        for i in temp:
            datafloat.append(float(i))
        data.append(datafloat)
# print(data)
R_all_end_to_base_1 = []
T_all_end_to_base_1 = []
# print(sheet_1.iloc[0]['ax'])
index=0
for i in good_picture:
    # print(sheet_1.iloc[i-1]['ax'],sheet_1.iloc[i-1]['ay'],sheet_1.iloc[i-1]['az'],sheet_1.iloc[i-1]['dx'],
    #                                   sheet_1.iloc[i-1]['dy'],sheet_1.iloc[i-1]['dz'])
    q=data[index][3],data[index][4],data[index][5],data[index][6]
    RT = pose_robot(q,data[index][0],data[index][1],data[index][2])
    index+=1
    R_all_end_to_base_1.append(RT[:3, :3])
    T_all_end_to_base_1.append(RT[:3, 3].reshape((3, 1)))

print(R_all_end_to_base_1)
R, T = cv2.calibrateHandEye(R_all_end_to_base_1, T_all_end_to_base_1, R_all_chess_to_cam_1,
                            T_all_chess_to_cam_1)  # 手眼标定
RT = np.column_stack((R, T))
RT = np.row_stack((RT, np.array([0, 0, 0, 1])))  # 即为cam to end变换矩阵
print('相机相对于末端的变换矩阵为：')

# print(RT)

# 结果验证，原则上来说，每次结果相差较小
for i in range(len(good_picture)):
    RT_end_to_base = np.column_stack((R_all_end_to_base_1[i], T_all_end_to_base_1[i]))
    RT_end_to_base = np.row_stack((RT_end_to_base, np.array([0, 0, 0, 1])))
    # print(RT_end_to_base)

    RT_chess_to_cam = np.column_stack((R_all_chess_to_cam_1[i], T_all_chess_to_cam_1[i]))
    RT_chess_to_cam = np.row_stack((RT_chess_to_cam, np.array([0, 0, 0, 1])))
    # print(RT_chess_to_cam)

    RT_cam_to_end = np.column_stack((R, T))
    RT_cam_to_end = np.row_stack((RT_cam_to_end, np.array([0, 0, 0, 1])))
    # print(RT_cam_to_end)

    RT_chess_to_base = RT_end_to_base @ RT_cam_to_end @ RT_chess_to_cam  # 即为固定的棋盘格相对于机器人基坐标系位姿
    RT_chess_to_base = np.linalg.inv(RT_chess_to_base)
    print('第', i, '次')
    print(RT_chess_to_base[:3, :])
    print('')
