from os import listdir, makedirs
from os.path import isfile, join, exists
import shutil
import time
# median, gussian filter
import cv2
import numpy as np
# frost, lee, k
import findpeaks

import matplotlib.pyplot as plt

import skimage.io
from skimage import img_as_float, img_as_ubyte
from skimage.restoration import denoise_wavelet, estimate_sigma


base_image_path = "../grayscale"
folder_lst = [join(base_image_path,f) for f in listdir(base_image_path)]

filter_names = ['gaussian_filter_', 'median_filter_', 'bayes_db2_', 'frost_', 'kuan_', 'lee_', 'lee_enhanced_']

# filters parameters
# window size
winsize = 7
# damping factor for frost
k_value1 = 2.0
# damping factor for lee enhanced
k_value2 = 1.0
# coefficient of variation of noise
cu_value = 0.25
# coefficient of variation for lee enhanced of noise
cu_lee_enhanced = 0.523
# max coefficient of variation for lee enhanced
cmax_value = 1.73

for folder_ in folder_lst:
    # get all image file names from the folder
    img_lst = [join(folder_,f) for f in listdir(folder_) if isfile(join(folder_,f))]

    folder_name = folder_.split("/")[-1]
    # print(folder_name)

    for filter_name in filter_names:
        #if the folder exists delete the folder and all of its contents
        if exists(filter_name + folder_name):
            shutil.rmtree(filter_name + folder_name)
        #create a new directory
        makedirs(filter_name + folder_name)
    
    #convert images to gray_scale
    #filter with all the required techniques and save the image in the right folders
    for img in img_lst:
        img_name = img.split("/")[-1]

        im = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        # gaussian filter
        g_im = cv2.GaussianBlur(im, (5,5), 0)
        cv2.imwrite(join(filter_names[0]+folder_name, img_name), g_im)

        # median filter
        m_im = cv2.medianBlur(im, 3)
        cv2.imwrite(join(filter_names[1]+folder_name, img_name), m_im)

        # wavelets
        sk_im = skimage.io.imread(img, as_gray=True)
        sk_im = img_as_float(sk_im)
        
        # can specify a wavelet = 'haar', wavelet_levels=3,
        bayes_db_im = denoise_wavelet(sk_im, method='BayesShrink', wavelet='db2', wavelet_levels=3, mode='soft', rescale_sigma=True)
        plt.imshow(bayes_db_im, cmap='gray', interpolation='nearest')
        plt.axis('off')
        plt.savefig(join(filter_names[2]+folder_name, img_name), bbox_inches='tight', pad_inches=0)

        # frost filter
        f_im = findpeaks.frost_filter(im, damping_factor=k_value1, win_size=winsize)
        cv2.imwrite(join(filter_names[3]+folder_name, img_name), f_im)

        # kuan filter
        k_im = findpeaks.kuan_filter(im, win_size=winsize, cu=cu_value)
        cv2.imwrite(join(filter_names[4]+folder_name, img_name), k_im)

        # lee filter
        l_im = findpeaks.lee_filter(im, win_size=winsize, cu=cu_value)
        cv2.imwrite(join(filter_names[5]+folder_name, img_name), l_im)

        # lee enhanced filter
        l_enhanced_im = findpeaks.lee_enhanced_filter(im, win_size=winsize, k=k_value2, cu=cu_lee_enhanced, cmax=cmax_value)
        cv2.imwrite(join(filter_names[6]+folder_name, img_name), l_enhanced_im)
        print(f"{folder_name} => {img_name} complete")
        
