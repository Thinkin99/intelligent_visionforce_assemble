import numpy as np
import cv2
RT=np.array[ -9.9993899e-01,-1.0088946e-02 ,  4.4969959e-03  , 8.8015883e+01;
   1.0510047e-02 , -9.9427378e-01  , 1.0634463e-01 ,  6.2791604e+01;
   3.3983400e-03   1.0638540e-01   9.9431916e-01   2.2532238e+02
   0.0000000e+00   0.0000000e+00   0.0000000e+00   1.0000000e+00
  -9.9730962e-01   6.3086842e-02  -3.7330709e-02   7.3375047e+01
  -5.6348514e-02  -9.8549812e-01  -1.6005720e-01   4.8148063e+01
  -4.6886846e-02  -1.5752305e-01   9.8640160e-01   3.0117252e+02
   0.0000000e+00   0.0000000e+00   0.0000000e+00   1.0000000e+00
  -9.7148784e-01  -5.6978423e-02   2.3014091e-01   7.7008279e+01
   1.7854134e-02  -9.8551806e-01  -1.6862795e-01   6.9272063e+01
   2.3641618e-01  -1.5971104e-01   9.5843611e-01   2.5192154e+02
   0.0000000e+00   0.0000000e+00   0.0000000e+00   1.0000000e+00
  -9.2861908e-01  -4.0700233e-02   3.6879547e-01   8.4792203e+01
  -3.4046939e-02  -9.8042457e-01  -1.9392903e-01   7.2760962e+01
   3.6946910e-01  -1.9264255e-01   9.0905524e-01   2.5687939e+02
   0.0000000e+00   0.0000000e+00   0.0000000e+00   1.0000000e+00
  -9.3893123e-01  -3.7151034e-02   3.4209348e-01   8.3645708e+01
   5.7096400e-02  -9.9719401e-01   4.8416018e-02   7.0322520e+01
   3.3933486e-01   6.4991617e-02   9.3841779e-01   2.7371126e+02
   0.0000000e+00   0.0000000e+00   0.0000000e+00   1.0000000e+00
  -8.9785966e-01   3.8721307e-02   4.3857575e-01   7.9309588e+01
  -2.4378221e-02  -9.9896925e-01   3.8290247e-02   5.8467788e+01
   4.3960633e-01   2.3687572e-02   8.9787815e-01   2.4153663e+02
   0.0000000e+00   0.0000000e+00   0.0000000e+00   1.0000000e+00
  -9.5695824e-01   1.6528007e-01  -2.3856536e-01   1.2178482e+02
  -1.8499487e-01  -9.8074344e-01   6.2603496e-02   3.9185645e+01
  -2.2362431e-01   1.0404230e-01   9.6910648e-01   3.2769235e+02
   0.0000000e+00   0.0000000e+00   0.0000000e+00   1.0000000e+00
  -9.8716920e-01   1.9658909e-02  -1.5846295e-01   9.3933918e+01
  -2.8239727e-02  -9.9824347e-01   5.2081645e-02   5.2731297e+01
  -1.5716074e-01   5.5888346e-02   9.8599036e-01   2.8334293e+02
   0.0000000e+00   0.0000000e+00   0.0000000e+00   1.0000000e+00
  -9.9232532e-01   1.1302892e-01   5.0149014e-02   8.9960219e+01
  -1.0465602e-01  -9.8369835e-01   1.4623500e-01   3.8378588e+01
   6.5860286e-02   1.3986429e-01   9.8797794e-01   2.4887455e+02
   0.0000000e+00   0.0000000e+00   0.0000000e+00   1.0000000e+00
  -9.6654436e-01  -2.3989575e-02   2.5537520e-01   9.4178996e+01
   3.3665352e-02  -9.9886873e-01   3.3584391e-02   6.4140905e+01
   2.5428063e-01   4.1058100e-02   9.6625855e-01   2.6813850e+02
   0.0000000e+00   0.0000000e+00   0.0000000e+00   1.0000000e+00];

    # cv2.imshow("gray", img)

#
#
# with open("D:/Desktop/eyehand0309/eyehand.txt", "r") as f:  # 打开文件
#     data = f.read()  # 读取文件
#     datalist=list(data)
#     print(data)
#     print(datalist[1])
# def quaternion_to_rotation_matrix(q):  # x, y ,z ,w
#     rot_matrix = np.array(
#         [[1.0 - 2 * (q[1] * q[1] + q[2] * q[2]), 2 * (q[0] * q[1] - q[3] * q[2]), 2 * (q[3] * q[1] + q[0] * q[2])],
#          [2 * (q[0] * q[1] + q[3] * q[2]), 1.0 - 2 * (q[0] * q[0] + q[2] * q[2]), 2 * (q[1] * q[2] - q[3] * q[0])],
#          [2 * (q[0] * q[2] - q[3] * q[1]), 2 * (q[1] * q[2] + q[3] * q[0]), 1.0 - 2 * (q[0] * q[0] + q[1] * q[1])]],
#         )
#     return rot_matrix
# data = []
# with open("D:/Desktop/eyehand0309/eyehand.txt") as f:
#     for line in f.readlines():
#         temp = line.split()
#         datafloat=[]
#         for i in temp:
#             datafloat.append(float(i))
#         data.append(datafloat)
# print(data[0])
# q=[0.0277,	0.2267	,0.9714	,0.0655]
# print(quaternion_to_rotation_matrix(q))
