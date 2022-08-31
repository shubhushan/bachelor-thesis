import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator

with open('results.csv', 'r') as result:
    reader = csv.reader(result)
    # format of csv file = [maze,img_no,filter,BRISQUE,PSNR,NRMSE]
    x_axis = [i for i in range(19)]
    gray_scale = [[0 for i in range(19)] for x in range(5)]
    gaussian_filter = [{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        }]
    lee_filter = [{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        }]
    lee_enhanced_filter = [{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        }]
    median_filter = [{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        }]
    kuan_filter = [{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        }]
    frost_filter = [{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        },{
        "psnr": [0 for i in range(19)],
        "brisque": [0 for i in range(19)],
        "nrmse": [0 for i in range(19)]
        }]
    for row in reader:
        maze_name, image_no, filter_name, brisque, psnr, nrmse = row
        maze_no = int(maze_name[-1])-1
        img_no = int(image_no)
        if filter_name == 'none':
            gray_scale[maze_no][img_no] = float(brisque)
        elif filter_name == 'gaussian_filter_':
            gaussian_filter[maze_no]["psnr"][img_no] = float(psnr)
            gaussian_filter[maze_no]["brisque"][img_no] = float(brisque)
            gaussian_filter[maze_no]["nrmse"][img_no] = float(nrmse)
        elif filter_name == 'median_filter_':
            median_filter[maze_no]["psnr"][img_no] = float(psnr)
            median_filter[maze_no]["brisque"][img_no] = float(brisque)
            median_filter[maze_no]["nrmse"][img_no] = float(nrmse)
        elif filter_name == 'frost_':
            frost_filter[maze_no]["psnr"][img_no] = float(psnr)
            frost_filter[maze_no]["brisque"][img_no] = float(brisque)
            frost_filter[maze_no]["nrmse"][img_no] = float(nrmse)
        elif filter_name == 'lee_':
            lee_filter[maze_no]["psnr"][img_no] = float(psnr)
            lee_filter[maze_no]["brisque"][img_no] = float(brisque)
            lee_filter[maze_no]["nrmse"][img_no] = float(nrmse)
        elif filter_name == 'lee_enhanced_':
            lee_enhanced_filter[maze_no]["psnr"][img_no] = float(psnr)
            lee_enhanced_filter[maze_no]["brisque"][img_no] = float(brisque)
            lee_enhanced_filter[maze_no]["nrmse"][img_no] = float(nrmse)
        elif filter_name == 'kuan_':
            kuan_filter[maze_no]["psnr"][img_no] = float(psnr)
            kuan_filter[maze_no]["brisque"][img_no] = float(brisque)
            kuan_filter[maze_no]["nrmse"][img_no] = float(nrmse)
    
    # plt.plot(x_axis, gray_scale[0], label=f"Maze 1")
    # plt.plot(x_axis, gray_scale[1], label="Maze 2")
    # plt.plot(x_axis, gray_scale[2], label="Maze 3")
    # plt.plot(x_axis, gray_scale[3], label="Maze 4")
    # plt.plot(x_axis, gray_scale[4], label="Maze 5")
    #brisque plots of noisy images
    # for i in range(5):
    #     plt.plot(x_axis, gray_scale[i], label=f"Maze {i+1}")
    # plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
    # plt.gca().yaxis.set_major_locator(MultipleLocator(base = 5))
    # plt.gca().xaxis.set_major_locator(MultipleLocator(base = 1))
    # plt.legend(loc="lower right")
    # plt.title("BRISQUE of noisy gray scale images")
    # plt.savefig('grayscale.jpg')
    # plt.close()
    metric_list = ["psnr", "nrmse"]

    #kuan filter psnr plots
    # for i in range(5):
    #     plt.plot(x_axis, kuan_filter[i]["psnr"], label=f"Maze {i+1}")
    # plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
    # plt.gca().yaxis.set_major_locator(MultipleLocator(base = 5))
    # plt.gca().xaxis.set_major_locator(MultipleLocator(base = 1))
    # plt.legend(loc="lower right")
    # plt.title("PSNR of Kuan Filtered images")
    # plt.savefig('kuan_psnr.jpg')
    # plt.close()

    #kuan filter plots
    for metric in metric_list:
        for i in range(5):
            plt.plot(x_axis, kuan_filter[i][metric], label=f"Kuan Filter")
            plt.plot(x_axis, lee_filter[i][metric], label=f"Lee Filter")
            plt.plot(x_axis, lee_enhanced_filter[i][metric], label=f"Lee Enhanced Filter")
            plt.plot(x_axis, frost_filter[i][metric], label=f"Frost Filter")
            plt.plot(x_axis, gaussian_filter[i][metric], label=f"Gaussian")
            plt.plot(x_axis, median_filter[i][metric], label=f"Median")

            plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
            if metric != "nrmse":
                plt.gca().yaxis.set_major_locator(MultipleLocator(base = 5))
            else:
                plt.gca().yaxis.set_major_locator(MultipleLocator(base = 0.02))
            plt.gca().xaxis.set_major_locator(MultipleLocator(base = 1))
            plt.legend(loc="lower right", bbox_to_anchor=(1.5, 0))
            plt.title(f"{metric.upper()} of Maze {i+1} images")
            plt.savefig(f'maze{i+1}_{metric}.jpg', bbox_inches="tight")
            plt.close()

    # #frost filter plots 
    # for metric in metric_list:
    #     for i in range(5):
    #         plt.plot(x_axis, frost_filter[i][metric], label=f"Maze {i+1}")
    #     plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
    #     if metric != "nrmse":
    #         plt.gca().yaxis.set_major_locator(MultipleLocator(base = 5))
    #     else:
    #         plt.gca().yaxis.set_major_locator(MultipleLocator(base = 0.01))
    #     plt.gca().xaxis.set_major_locator(MultipleLocator(base = 1))
    #     plt.legend(loc="lower right")
    #     plt.title(f"{metric.upper()} of Frost Filtered images")
    #     plt.savefig(f'frost_{metric}.jpg')
    #     plt.close()
    
    # #lee filter plots 
    # for metric in metric_list:
    #     for i in range(5):
    #         plt.plot(x_axis, lee_filter[i][metric], label=f"Maze {i+1}")
    #     plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
    #     if metric != "nrmse":
    #         plt.gca().yaxis.set_major_locator(MultipleLocator(base = 5))
    #     else:
    #         plt.gca().yaxis.set_major_locator(MultipleLocator(base = 0.01))
    #     plt.gca().xaxis.set_major_locator(MultipleLocator(base = 1))
    #     plt.legend(loc="lower right")
    #     plt.title(f"{metric.upper()} of Lee Filtered images")
    #     plt.savefig(f'lee_{metric}.jpg')
    #     plt.close()

    # #lee_enhanced filter plots 
    # for metric in metric_list:
    #     for i in range(5):
    #         plt.plot(x_axis, lee_enhanced_filter[i][metric], label=f"Maze {i+1}")
    #     plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
    #     if metric != "nrmse":
    #         plt.gca().yaxis.set_major_locator(MultipleLocator(base = 5))
    #     else:
    #         plt.gca().yaxis.set_major_locator(MultipleLocator(base = 0.02))
    #     plt.gca().xaxis.set_major_locator(MultipleLocator(base = 1))
    #     plt.legend(loc="lower right")
    #     plt.title(f"{metric.upper()} of Lee Enhanced Filtered images")
    #     plt.savefig(f'lee_enhanced_{metric}.jpg')
    #     plt.close()

    # #frost filter plots 
    # for metric in metric_list:
    #     for i in range(5):
    #         plt.plot(x_axis, frost_filter[i][metric], label=f"Maze {i+1}")
    #     plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
    #     if metric != "nrmse":
    #         plt.gca().yaxis.set_major_locator(MultipleLocator(base = 5))
    #     else:
    #         plt.gca().yaxis.set_major_locator(MultipleLocator(base = 0.01))
    #     plt.gca().xaxis.set_major_locator(MultipleLocator(base = 1))
    #     plt.legend(loc="lower right")
    #     plt.title(f"{metric.upper()} of Frost Filtered images")
    #     plt.savefig(f'frost_{metric}.jpg')
    #     plt.close()
    
    # #gaussian filter plots 
    # for metric in metric_list:
    #     for i in range(5):
    #         plt.plot(x_axis, gaussian_filter[i][metric], label=f"Maze {i+1}")
    #     plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
    #     if metric != "nrmse":
    #         plt.gca().yaxis.set_major_locator(MultipleLocator(base = 5))
    #     else:
    #         plt.gca().yaxis.set_major_locator(MultipleLocator(base = 0.02))
    #     plt.gca().xaxis.set_major_locator(MultipleLocator(base = 1))
    #     plt.legend(loc="lower right")
    #     plt.title(f"{metric.upper()} of Gaussian Filtered images")
    #     plt.savefig(f'gaussian_{metric}.jpg')
    #     plt.close()

    # #median filter plots 
    # for metric in metric_list:
    #     for i in range(5):
    #         plt.plot(x_axis, median_filter[i][metric], label=f"Maze {i+1}")
    #     plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
    #     if metric != "nrmse":
    #         plt.gca().yaxis.set_major_locator(MultipleLocator(base = 5))
    #     else:
    #         plt.gca().yaxis.set_major_locator(MultipleLocator(base = 0.02))
    #     plt.gca().xaxis.set_major_locator(MultipleLocator(base = 1))
    #     plt.legend(loc="lower right")
    #     plt.title(f"{metric.upper()} of Median Filtered images")
    #     plt.savefig(f'median_{metric}.jpg')
    #     plt.close()