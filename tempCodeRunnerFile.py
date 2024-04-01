
# import cv2

# # Try to access the webcam.
# cap = cv2.VideoCapture(0)

# # Check if the webcam is opened correctly
# if not cap.isOpened():
#     print("Could not open webcam")
# else:
#     print("Webcam is accessible")

#     while True:
#         # Capture frame-by-frame
#         ret, frame = cap.read()

#         # If frame is read correctly ret is True
#         if not ret:
#             print("Can't receive frame (stream end?). Exiting ...")
#             break

#         # Display the resulting frame
#         cv2.imshow('Frame', frame)

#         # Wait for a key press and break the loop if 'q' is pressed
#         if cv2.waitKey(1) == ord('q'):
#             break

# # Release the webcam resource
# cap.release()
# cv2.destroyAllWindows()

