import time
import cv2
import tuoyuan
import pyrealsense2 as rs

pipeline = rs.pipeline()  # 定义流程pipeline
config = rs.config()  # 定义配置config
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
# config.enable_stream(rs.stream.depth, 1280, 960, rs.format.z16, 30)
# config.enable_stream(rs.stream.color, 1280, 960, rs.format.bgr8, 30)
profile = pipeline.start(config)  # 流程开始
align_to = rs.stream.color  # 与color流对齐
align = rs.align(align_to)
index=1
# cap = cv2.VideoCapture(2)
# tuoyuan.circle_detect_init()
while 1:
    intr, depth_intrin, color_image, depth_image, aligned_depth_frame = tuoyuan.get_aligned_images(pipeline, align)
    # img_raw = color_image
    cv2.imshow("img", color_image)
    # img = cv2.inRange(color_image, (0, 0, 50), (255, 255, 255))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)

    #
    # img = cv2.imread("1.jpg")
    # ux, uy, detect = tuoyuan.circle_dectect(img, img_raw)

    # ux, uy = tuoyuan.ell_detect(img)
    # if ux:
    #     dis = aligned_depth_frame.get_distance(ux, uy)
    #     camera_xyz = rs.rs2_deproject_pixel_to_point(
    #         depth_intrin, (ux, uy), dis)
    #     print(str(camera_xyz))
    # tuoyuan.blob_detect(img)
    # if ux :
    #     tuoyuan.depth_detect(aligned_depth_frame, depth_intrin, ux, uy, detect)

    # cv2.imshow("detect", detect)
    # print(intr)
    # time.sleep(0.3)
    key = cv2.waitKey(20)
    if key & 0xFF == ord('q') or key == 27:
        break
    elif key & 0xFF == ord('s'):
        # int i=
        path='D:/Desktop/intelligent_visionforce_assemble/handeye/'+str(index)+'.jpg'
        cv2.imwrite(path,color_image)
        index+=1
# cap.release()
cv2.destroyAllWindows()
#
