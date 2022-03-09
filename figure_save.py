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
while 1:
    intr, depth_intrin, color_image, depth_image, aligned_depth_frame = tuoyuan.get_aligned_images(pipeline, align)
    img=color_image
    cv2.imshow('det',img)

