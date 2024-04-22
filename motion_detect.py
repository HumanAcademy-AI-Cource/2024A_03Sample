#!/usr/bin/env python3

# 必要なライブラリをインポート
import cv2
import datetime

# カメラの設定
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# 前のフレームを保持する変数
previous_frame = None

# 動体検出のしきい値
max_score = 10000

while True:
    success, image = cap.read()

    mono = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # グレースケール変換

    # 前のフレームがないときは、現在のフレームを入れる
    if previous_frame is None:
        previous_frame = mono.copy().astype("float")  # フレームをコピー
        continue

    # 動体検出の処理
    cv2.accumulateWeighted(mono, previous_frame, 0.6)  # 加重平均の計算
    mask = cv2.absdiff(mono, cv2.convertScaleAbs(previous_frame))  # 差分画像の作成
    thresh = cv2.threshold(mask, 3, 255, cv2.THRESH_BINARY)[1]  # 差分画像を2値化
    score = cv2.countNonZero(thresh)  # 画像中の黒以外の要素を積算してスコアを算出

    # 指定したスコアを超えたら動体検出したとみなす
    if score > max_score:
        print("[{}] 動いたよ！（差の数値: {}）".format(datetime.datetime.now(), score))

    # 画像の表示
    cv2.imshow("USB Camera", image)
    cv2.waitKey(1)
