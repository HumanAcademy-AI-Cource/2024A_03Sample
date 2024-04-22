#!/usr/bin/env python3

# 必要なライブラリをインポート
import cv2

# カメラの設定
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)


while True:
    success, image = cap.read()
    # 画像の表示
    cv2.imshow("USB Camera", image)
    cv2.waitKey(1)
