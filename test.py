import cv2
from matplotlib import pyplot as plt
import numpy as np
import urllib.request

# from util import get_limits
from PIL import Image

from util import get_limits
# url="http://192.168.1.3:8080/shot.jpg"
y = [0,255,255] # yellow in BGR
cap = cv2.VideoCapture(0)

while True:
    # img_arr = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)     
    # frame = cv2.imdecode(img_arr, -1)
    ret, frame = cap.read()
    # cv2.imshow('frame', frame)
    hsv =   cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerlimit , upperlimit = get_limits(y)
    # LowerLimit= np.array([22, 93, 0]) # type: ignore
     # UpperLimit= np.array([45, 255, 255]) # type: ignore
    mask = cv2.inRange(hsv, lowerlimit, upperlimit)
    # kernel = np.ones((40,40), np.uint8)

    # closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    res = cv2.bitwise_and(frame, frame, mask=mask)
        
    mask_ = Image.fromarray(res)

    bbox = mask_.getbbox()
    if bbox is not None:
        x1 , y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break























# while True:
#     ret, frame = cap.read()
    
#     hsv =   cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     lowerlimit , upperlimit = get_limits(color=y)
#     # LowerLimit= np.array([22, 93, 0]) # type: ignore
#     # UpperLimit= np.array([45, 255, 255]) # type: ignore
#     mask = cv2.inRange(hsv, lowerlimit, upperlimit)
#     # kernel = np.ones((40,40), np.uint8)

#     # closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#     res = cv2.bitwise_and(frame, frame, mask=mask)
    
#     mask_ = Image.fromarray(res)

#     bbox = mask_.getbbox()
#     if bbox is not None:
#         x1 , y1, x2, y2 = bbox

#         frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

#     cv2.imshow('Frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'): 
#         break


    





# # import cv2

# # # Try to access the webcam.
# # cap = cv2.VideoCapture(0)

# # # Check if the webcam is opened correctly
# # if not cap.isOpened():
# #     print("Could not open webcam")
# # else:
# #     print("Webcam is accessible")

# #     while True:
# #         # Capture frame-by-frame
# #         ret, frame = cap.read()

# #         # If frame is read correctly ret is True
# #         if not ret:
# #             print("Can't receive frame (stream end?). Exiting ...")
# #             break

# #         # Display the resulting frame
# #         cv2.imshow('Frame', frame)

# #         # Wait for a key press and break the loop if 'q' is pressed
# #         if cv2.waitKey(1) == ord('q'):
# #             break

# # # Release the webcam resource
# # cap.release()
# # cv2.destroyAllWindows()

