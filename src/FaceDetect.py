#! /usr/bin/env python3

import sys
import os
import glob
import cv2


opencv_src = '/home/takao/Documents/dev/opencv/opencv'
cascade_dir = 'data/haarcascades'
cascade_path = os.path.join(opencv_src, cascade_dir,
                            'haarcascade_frontalface_default.xml')


def face_detect(in_file: str, out_file: str):
    # ファイル読み込み
    image = cv2.imread(in_file)

    # GrayScale にする
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # カスケード分類機による特徴量を取得する
    cascade = cv2.CascadeClassifier(cascade_path)

    # 顔認識
    face_rect = cascade.detectMultiScale(
        image_gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))

    # 枠の色(白)
    color = (255, 255, 255)

    if len(face_rect) > 0:
        for rect in face_rect:
            cv2.rectangle(image, tuple(rect[0:2]), tuple(
                rect[0:2]+rect[2:4]), color, thickness=2)

        # 認識結果を保存
        cv2.imwrite(out_file, image)


if __name__ == "__main__":
    files = glob.glob('./input/*.*')
    for f in files:
        print(f)
        image_path = f
        output_path = "./output_" + os.path.basename(image_path)

        face_detect(image_path, output_path)
