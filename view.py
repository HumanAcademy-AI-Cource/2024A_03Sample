#!/usr/bin/env python3

# 必要なライブラリをインポート
import cv2
import matplotlib.pyplot as plt

# 画像を読み込み
image = cv2.imread("images/huukei.png")
# BGRからRGB形式に変換
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 画像を表示
plt.imshow(image)
plt.xticks([]), plt.yticks([])
plt.show()
