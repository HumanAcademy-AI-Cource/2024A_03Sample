#!/usr/bin/env python3

# 必要なライブラリをインポート
import cv2
import numpy as np

# 黒色の画像を作成
image = np.zeros((300, 300, 3))

# 図形の描画
cv2.circle(image, (150, 150), 100, (255, 255, 255), thickness=-1, lineType=cv2.LINE_8)
cv2.rectangle(image, (100, 100), (150, 150), (255, 0, 0), thickness=-1)

# 画像を表示
cv2.imshow("Oekaki", image)
cv2.waitKey(0)
cv2.destroyAllWindows()