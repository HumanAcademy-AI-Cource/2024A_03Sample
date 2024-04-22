#!/usr/bin/env python3

# 必要なライブラリをインポート
import cv2

# 顔検出の準備
face_cascade = cv2.CascadeClassifier("/usr/share/opencv4/haarcascades/haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier("/usr/share/opencv4/haarcascades/haarcascade_eye_tree_eyeglasses.xml")

# カメラの設定
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    # カメラ画像を読み込む
    _, image = cap.read()

    # 画像をグレースケールに変換
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 顔検出開始
    faces = face_cascade.detectMultiScale(gray_image)

    # 検出された顔の数だけ繰り返し
    for x, y, w, h in faces:
        # 顔の位置に四角を描画
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)

        # 目の検出を開始
        eyes = eye_cascade.detectMultiScale(gray_image[y: y + h, x: x + w])

        # 目の位置に四角を描画
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(image[y: y + h, x: x + w], (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 1)
    
    # 画像を表示
    cv2.imshow("face_detection", image)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()