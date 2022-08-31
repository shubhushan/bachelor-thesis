from os import listdir, makedirs
from os.path import isfile, join, exists
import shutil

import cv2
import numpy as np

base_image_path = "../maze"
folder_lst = [join(base_image_path,f) for f in listdir(base_image_path)]

gray_scale_path = "../grayscale"

if exists(gray_scale_path):
    shutil.rmtree(gray_scale_path)

makedirs(gray_scale_path)

for folder_ in folder_lst:
    folder_name = folder_.split('/')[-1]
    #create folders inside grayscale path
    makedirs(join(gray_scale_path, folder_name))

    img_lst = [join(folder_,f) for f in listdir(folder_) if isfile(join(folder_,f))]
    print(img_lst)
    for img in img_lst:
        img_name = img.split('/')[-1]

        im = cv2.imread(img)

        gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(join(gray_scale_path, folder_name, img_name), gray_im)

