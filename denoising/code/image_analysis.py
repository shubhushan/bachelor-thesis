from os import listdir
from os.path import isfile, join, exists
import csv
import numpy as np
# BRISQUE Blind/Refrenceless Image Spatial Quality Evaluator (BRISQUE)
# Support Vector Regression model trained on an image database with corrensponding mean opinion score DMOS values
# the database contains images with known distortion such as compression artifacts, blurring, and noise
import imquality.brisque as brisque
import PIL.Image
from skimage import io, img_as_float, metrics

filter_names = ['gaussian_filter_', 'median_filter_', 'frost_', 'kuan_', 'lee_', 'lee_enhanced_']#'bayes_db2_',

gray_scale_path = '../grayscale'

folder_names = [join(gray_scale_path, f) for f in listdir(gray_scale_path)]

with open('results.csv', 'w') as result:
    result_row = ['maze', 'img_no','filter','BRISQUE', 'PSNR', 'NRMSE']
    writer = csv.writer(result)
    writer.writerow(result_row)

    for folder_ in folder_names:
        
        folder_name = folder_.split("/")[-1]
        maze_name = folder_name.split("constant")[0]
        # get all the base image names for brisque calculation
        img_names = [f.split('.')[0] for f in listdir(folder_)]
        # print(img_names)
        
        for img_name in img_names:
            print(f"{folder_name}, {img_name} =>\n")
            # gray scale brisque
            gray_path = join(gray_scale_path, folder_name, img_name+".jpg")
            gray_im = img_as_float(io.imread(gray_path, as_gray=True))
            # had to change line number 45 of brisque.py from the library venv/lib/python3.10/site-packages/imquality/brisque.py
            gray_score = round(brisque.score(gray_im), 5)
            # print(f"GrayScale: {gray_score}\n")
            gray_row = [maze_name, img_name,'none', gray_score, 'none', 'none']
            writer.writerow(gray_row)
            for filter in filter_names:
                filter_path = join(filter+folder_name, img_name+".jpg")
                filter_im = img_as_float(io.imread(filter_path, as_gray=True))
                # brisque score
                filter_brisque = round(brisque.score(filter_im), 5)
                # print(f"{filter}BRISQUE: {filter_brisque}")
                #psnr score
                filter_psnr = round(metrics.peak_signal_noise_ratio(filter_im, gray_im), 5)
                # print(f"{filter}PSNR: {filter_psnr}")
                #normalized root mse
                filter_nrmse = round(metrics.normalized_root_mse(filter_im, gray_im), 5)
                # print(f"{filter}NRMSE: {filter_nrmse}\n")

                filter_row = [maze_name, img_name, " ".join(filter.split("_")), filter_brisque, filter_psnr, filter_nrmse]
                writer.writerow(filter_row)
            # print(f"End of analysis of {img_name}.jpg\n")


# for folder_ in folder_names:
    
#     folder_name = folder_.split("/")[-1]
#     maze_name = folder_name.split("constant")[0]
#     # get all the base image names for brisque calculation
#     img_names = [f.split('.')[0] for f in listdir(folder_)]
#     print(img_names)
    
#     for img_name in img_names:
#         print(f"{folder_name}, {img_name} =>\n")
#         # gray scale brisque
#         gray_path = join(gray_scale_path, folder_name, img_name+".jpg")
#         gray_im = img_as_float(io.imread(gray_path, as_gray=True))
#         # had to change line number 45 of brisque.py from the library venv/lib/python3.10/site-packages/imquality/brisque.py
#         gray_score = brisque.score(gray_im)
#         print(f"GrayScale: {gray_score}\n")
        
#         for filter in filter_names:
#             filter_path = join(filter+folder_name, img_name+".jpg")
#             filter_im = img_as_float(io.imread(filter_path, as_gray=True))
#             # brisque score
#             filter_brisque = brisque.score(filter_im)
#             print(f"{filter}BRISQUE: {filter_brisque}")
#             #psnr score
#             filter_psnr = metrics.peak_signal_noise_ratio(filter_im, gray_im)
#             print(f"{filter}PSNR: {filter_psnr}")
#             #normalized root mse
#             filter_nrmse = metrics.normalized_root_mse(filter_im, gray_im)
#             print(f"{filter}NRMSE: {filter_nrmse}\n")
            
#         print(f"End of analysis of {img_name}.jpg\n")
