#!/usr/bin/env python3

# 必要なライブラリをインポート
import cv2
import numpy as np

# 画像を読み込み
image = cv2.imread("images/banana.png")
# HSV形式に変換
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 特定の色が含まれる場所を調べる（HSVで指定）
mask_image = cv2.inRange(image, np.array([20, 0, 0]), np.array([29,255,255]))
# 特定の色が含まれていた部分だけ画像から取り出す
edited_image = cv2.bitwise_and(image, image, mask=mask_image)
# HSVからBGR形式に変換
edited_image = cv2.cvtColor(edited_image, cv2.COLOR_HSV2BGR)

# 画像を表示
cv2.imshow("Result", edited_image)
cv2.waitKey(0)
cv2.destroyAllWindows()