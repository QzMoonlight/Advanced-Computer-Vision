# -*- codeing = utf-8  -*-
# @Time : 2022/9/9 9:26
# @Author : Moonlight_Qz
# @File : main.py
# @Software : PyCharm

import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Proj1test.jpeg")
height, width, color = img.shape

# 设定插值后尺寸
dimension = (width*5, height*5)


def img_draw_subplot(subplot_position, image, title_name):
    plt.subplot(subplot_position)
    plt.axis('off')
    plt.xticks([])
    plt.title(title_name)
    plt.imshow(image)


# 最近邻插值算法
nearest_img = cv2.resize(img, dimension, cv2.INTER_NEAREST)
# 双线性插值算法
linear_img = cv2.resize(img, dimension, cv2.INTER_LINEAR)
# 三次样条插值算法
cubic_img = cv2.resize(img, dimension, cv2.INTER_CUBIC)
# 区域插值算法
area_img = cv2.resize(img, dimension, cv2.INTER_AREA)

img_draw_subplot(221, nearest_img, "Nearest interpolation")
img_draw_subplot(222, linear_img, "Linear interpolation")
img_draw_subplot(223, cubic_img, "cubic interpolation")
img_draw_subplot(224, area_img, "Area interpolation")

plt.show()