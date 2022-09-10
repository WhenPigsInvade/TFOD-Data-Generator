# https://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv/14102014#14102014][1]
import os
import cv2
import numpy as np
import random

# Parameters are filepaths to the images
def merge(background, pokemon):
    l_img = cv2.imread(background)
    s_img = cv2.imread(pokemon, -1)

    random_size = [0.6, 0.65, 0.7, 0.75]
    ran_size = random.choice(random_size)
    s_img = cv2.resize(s_img, (0,0), fx=ran_size, fy=ran_size)

    if random.random() > 0.5:
        s_img = cv2.flip(s_img, 1)

    x_offset=80+int((random.random()*(l_img.shape[1] - s_img.shape[1] - 80)))
    y_offset=50+int((random.random()*(l_img.shape[0] - s_img.shape[0] - 80)))

    y1, y2 = y_offset, y_offset + s_img.shape[0]
    x1, x2 = x_offset, x_offset + s_img.shape[1]

    alpha_s = s_img[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        l_img[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] +
                                alpha_l * l_img[y1:y2, x1:x2, c])

    # Result, Pokemon width, Pokemon height, Pokemon x location, Pokemon y location
    return (l_img, s_img.shape[1], s_img.shape[0], x_offset, y_offset)

