#! /usr/bin/env python3

import sys
import os
import glob
import cv2
import numpy as np


# opencv_src = '/home/takao/Documents/dev/opencv/opencv'
# cascade_dir = 'data/haarcascades'
# cascade_path = os.path.join(opencv_src, cascade_dir,
#                             'haarcascade_frontalface_default.xml')
cascade_path = os.path.join('/home/takao/Documents/dev/lbpcascade_animeface',
                            'lbpcascade_animeface.xml')


def face_detect(in_file: str, out_file: str):
    # ファイル読み込み
    image = cv2.imread(in_file)

    # GrayScale にする
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # カスケード分類機による特徴量を取得する
    cascade = cv2.CascadeClassifier(cascade_path)

    # 顔認識
    face_rect = cascade.detectMultiScale(
        image_gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(24, 24))

    # 枠の色(白)
    # color = (255, 255, 255)
    index = 1
    if len(face_rect) > 0:
        for rect in face_rect:
            l, t = rect[0:2] - 100
            r, b = rect[0:2] + rect[2:4] + 100
            l = max(0, l)
            t = max(0, t)
            r = min(image.shape[1], r)
            b = min(image.shape[0], b)
            # 正方形にする
            width = min(r-l, b-t)
            r = l + width
            b = t + width
            # cv2.rectangle(image,
            #               (l, t),
            #               (r, b),
            #               color,
            #               thickness=2)

            # Clopping
            out_dir, out_filename = os.path.split(out_file)
            out_filetitle, out_fileext = os.path.splitext(out_filename)
            clopped_out_file = os.path.join(out_dir, str(index) + '_' + out_filetitle + out_fileext)
            clopped = image[t:b, l:r]
            # print(clopped_out_file, clopped.shape, t,b, l,r)
            clopped = cv2.resize(clopped, (640, 640)) 
            cv2.imwrite(clopped_out_file, clopped)
            index = index + 1

        # 認識結果を保存
        # cv2.imwrite(out_file, image)


if __name__ == "__main__":
    files = glob.glob('./input/*.*')
    for f in files:
        print(f)
        image_path = f
        output_path = "./output/" + os.path.basename(image_path)

        face_detect(image_path, output_path)
