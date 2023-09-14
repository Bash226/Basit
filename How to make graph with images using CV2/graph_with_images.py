from PIL import ImageFilter 
import pyrealsense2 as rs
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.infrared,1, 640, 480, rs.format.y8, 30)


profile = pipeline.start(config)

device = profile.get_device()
depth_sensor = device.first_depth_sensor()
device.hardware_reset()


frames = pipeline.wait_for_frames()
left_ir_frame = frames.get_infrared_frame(1)

    
left_image = np.asanyarray(left_ir_frame.get_data())


bilateralFilter_image = cv2.bilateralFilter(left_image, d=6, sigmaColor=75, sigmaSpace=75)

fig, ax = plt.subplots(1, 2, figsize=(10,5))
ax[0][0].imshow(bilateralFilter_image)
ax[0][1].imshow(left_image)

plt.savefig('combined_ir_img.jpg', bbox_inches='tight')

cv2.waitKey(1)

pipeline.stop()
pipeline.close()
