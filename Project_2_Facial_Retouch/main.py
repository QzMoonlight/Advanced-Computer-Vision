# -*- codeing = utf-8  -*-
# @Author : Moonlight_Qz
# @File : facial_dermabrasion.py
# @Software : PyCharm

import cv2
from PIL import Image
from PIL import ImageEnhance
def facial_dermabrasion_effect(fileName):
    img = cv2.imread(fileName)
    blur_img = cv2.bilateralFilter(img, 100, 75, 75)

    result_img = cv2.addWeighted(img, 0.3, blur_img, 0.7, 0)
    cv2.imwrite("img_1.jpg", result_img)
    image = Image.open("img_1.jpg")

    enh_img = ImageEnhance.Sharpness(image)
    image_sharped = enh_img.enhance(1.5)

    con_img = ImageEnhance.Contrast(image_sharped)
    image_con = con_img.enhance(1.15)
    image_con.save("img_2.jpg")

    img1 = cv2.imread("img_1.jpg")
    img2 = cv2.imread("img_2.jpg")
    cv2.imshow("0", img)
    cv2.imshow("1", img1)
    cv2.imshow("2", img2)
    cv2.waitKey()

if __name__ == "__main__":
    facial_dermabrasion_effect("proj2.jpg")