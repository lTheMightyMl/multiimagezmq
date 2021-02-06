import imagezmq
import numpy as np
import cv2
import time

# initialize the ImageHub object
imageHub = imagezmq.ImageHub(open_port='tcp://127.0.0.1:5555', REQ_REP=False)
imageHub.connect('tcp://127.0.0.1:5556')

print('here')

# start looping over all the frames
time.sleep(10)
start = time.time()
num_of_frames = 0

show_frame = None

while True:
    # receive RPi name and frame from the RPi and acknowledge
    # the receipt
    rpiName, frame = imageHub.recv_image()
    # print(time.time() - start)
    # print(frame.shape)

    # frame = imutils.resize(frame, width=400)

    if rpiName == 'test':
        show_frame = np.vstack(tuple(frame))
    elif show_frame is not None:
        num_of_frames += 1
        show_frame = np.vstack((show_frame, *frame))
        cv2.imshow('frame', show_frame)
        key = cv2.waitKey(1) & 0xFF
        print(show_frame.shape)
        if key == ord("q"):
            break


# do a bit of cleanup


fps = num_of_frames / (time.time() - start)
print("fps is: ")
print(fps)
cv2.destroyAllWindows()
